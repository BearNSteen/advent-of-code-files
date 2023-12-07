import time
from pathlib import Path

####### RANKS
# 1 - No matches
# 2 - 1 pair
# 3 - 2 pair
# 4 - 3 of a kind
# 5 - full house
# 6 - 4 of a kind
# 7 - 5 of a kind


def analyze_hand(value, bid):
    cards = []
    for x in range(len(value)):
        if value[x] == "T":
            to_add = 10
        elif value[x] == "J":
            to_add = 11
        elif value[x] == "Q":
            to_add = 12
        elif value[x] == "K":
            to_add = 13
        elif value[x] == "A":
            to_add = 14
        else:
            to_add = int(value[x])
        cards.append(to_add)
        cards = cards

    sort_cards = cards.copy()
    sort_cards.sort()
    prev = 0
    vals = []
    for val in sort_cards:
        if prev == 0:
            prev = val
            curr_tot = 1
        elif prev != val:
            vals.append((prev, curr_tot))
            prev = val
            curr_tot = 1
        else:
            curr_tot += 1
    vals.append((prev, curr_tot))

    sorted(vals, key=lambda x: x[1])

    hand = 1
    check_full_house = 0
    for pair in vals:
        if check_full_house != 0:
            if pair[1] != 1:
                if pair[1] == 3 and check_full_house == 2:
                    hand = 5
                elif pair[1] == 2 and check_full_house == 3:
                    hand = 5
                elif pair[1] == 2 and check_full_house == 2:
                    hand = 3
                elif pair[1] != 3 and check_full_house == 2:
                    hand = 2
                elif pair[1] != 2 and check_full_house == 3:
                    hand = 4
                check_full_house = 0
        elif pair[1] == 5:
            hand = 7
        elif pair[1] == 4:
            hand = 6
        elif pair[1] == 3:
            hand = 4
            check_full_house = 3
        elif pair[1] == 2:
            hand = 2
            check_full_house = 2
    
    return (hand, cards, bid)

def analyze_hand_joker(value, bid):
    cards = []
    joker = False
    for x in range(len(value)):
        if value[x] == "T":
            to_add = 10
        elif value[x] == "J":
            to_add = 1
            joker = True
        elif value[x] == "Q":
            to_add = 12
        elif value[x] == "K":
            to_add = 13
        elif value[x] == "A":
            to_add = 14
        else:
            to_add = int(value[x])
        cards.append(to_add)
        cards = cards


    sort_cards = cards.copy()
    sort_cards.sort()
    prev = 0
    vals = []
    for val in sort_cards:
        if prev == 0:
            prev = val
            curr_tot = 1
        elif prev != val:
            vals.append((prev, curr_tot))
            if prev == 1:
                joker_num = curr_tot
            prev = val
            curr_tot = 1
        else:
            curr_tot += 1
    vals.append((prev, curr_tot))

    sorted(vals, key=lambda x: x[1])


    if joker:
        # joker_num
        # Combinations:
        # JJJJA, JJJAA, JJAAA, JAAAA - 5 of a kind
        # JJAAK, JAAAK, JJJAK - 4 of a kind
        hand = 0
        looking_for = 0
        for pair in vals:
            if pair[0] == 1:
                if pair[1] == 5:
                    hand = 7
            else:
                c = True
                if looking_for != 0:
                    if pair[1] < 3:
                        if pair[1] == 2 and looking_for == 3:
                            # 2 pair
                            hand = 3
                            break
                        elif pair[1] == 2 and looking_for == 2:
                            # full house
                            hand = 5
                            break
                        elif pair[1] == 1 and looking_for == 2:
                            # 3oak looking for 2 finds 1 and becomes 3oak
                            hand = 4
                            break
                        elif pair[1] == 1 and looking_for == 3:
                            # 1 pair looking for three of a kind finds 1 and is 1 pair
                            hand = 2
                            break
                        c = False
                    else:
                        c = True
                if c == True:      
                    if pair[1] == 5 or pair[1] == 4:
                        hand = 7
                        break
                    elif pair[1] == 3:
                        if joker_num == 1:
                            hand = 6
                            break
                        elif joker_num == 2:
                            hand = 7
                            break
                    elif pair[1] == 2:
                        if joker_num == 2:
                            # JJ + 2
                            hand = 6
                            break
                        if joker_num == 3:
                            # JJJ + 2
                            hand = 7
                            break
                        else:
                            # J + 2
                            hand = 4
                            looking_for = 2
        if hand == 0:
            if joker_num == 1:
                hand = 2
            elif joker_num == 2:
                hand = 4
            elif joker_num == 3:
                hand = 6
            elif joker_num == 4:
                hand = 7
    else:
        hand = 1
        check_full_house = 0
        for pair in vals:
            if check_full_house != 0:
                if pair[1] != 1:
                    if pair[1] == 3 and check_full_house == 2:
                        hand = 5
                    elif pair[1] == 2 and check_full_house == 3:
                        hand = 5
                    elif pair[1] == 2 and check_full_house == 2:
                        hand = 3
                    elif pair[1] != 3 and check_full_house == 2:
                        hand = 2
                    elif pair[1] != 2 and check_full_house == 3:
                        hand = 4
                    check_full_house = 0
            elif pair[1] == 5:
                hand = 7
            elif pair[1] == 4:
                hand = 6
            elif pair[1] == 3:
                hand = 4
                check_full_house = 3
            elif pair[1] == 2:
                hand = 2
                check_full_house = 2
    
    return (hand, cards, bid)

def print_sort(sort):
    x = 1
    for line in sort:
        print(str(x) + ") " + str(line))
        x += 1

def joker_print_sort(sort):
    x = 1
    for line in sort:
        if 1 in line[1]:
            if line[0] == 7:
                hand_type = "Five of a kind"
            elif line[0] == 6:
                hand_type = "Four of a kind"
            elif line[0] == 5:
                hand_type = "Full house"
            elif line[0] == 4:
                hand_type = "Three of a kind"
            elif line[0] == 3:
                hand_type = "Two pair"
            elif line[0] == 2:
                hand_type = "One pair"
            elif line[0] == 1:
                hand_type = "No pairs"
            line[1].sort()
            print(str(x) + ") " + hand_type + " | " + str(line[1]))
        x += 1


def part_one(input):
    #print("PART 1 --------------------------")
    lines = input.splitlines()
    max_rank = len(lines)
    hands = []
    #print("Analyzing...")
    for line in lines:
        spl = line.split()
        hands.append((analyze_hand(spl[0], int(spl[1]))))
    sort = []
    
    #print("Sorting...")
    for hand_to_sort in hands:
        if len(sort) == 0:
            sort.append(hand_to_sort)
        else:
            inserted = 0
            spot = 0
            for sorted_hand in sort:
                if inserted == 1:
                    break
                if sorted_hand[0] == hand_to_sort[0]:
                    challenger = hand_to_sort[1]
                    sitting = sorted_hand[1]
                    done = False
                    for x in range(5):
                        if challenger[x] > sitting[x]:
                            spot += 1
                            done = True
                            break
                        elif challenger[x] < sitting[x]:
                            sort.insert(spot, hand_to_sort)
                            inserted = 1
                            done = True
                            break
                    if done != True:
                        sort.insert(spot, hand_to_sort)
                        inserted = 1

                elif sorted_hand[0] < hand_to_sort[0]:
                    spot += 1
                elif sorted_hand[0] > hand_to_sort[0]:
                    sort.insert(spot, hand_to_sort)
                    inserted = 1
            if inserted == 0:
                sort.append(hand_to_sort)
            else:
                pass
                #print("Inserted " + str(hand_to_sort) + " at index " + str(spot))
    #print_sort(sort)
    x = 1
    winnings = 0
    #print("Calculating winnings...")
    for hand in sort:
        #print(str(winnings) + " += " + str(hand[2]) + " * " + str(x))
        winnings += (hand[2] * x)
        x += 1
    print("Part 1 Answer: " + str(winnings))
        
def part_two(input):
    #print("PART 2 --------------------------")
    lines = input.splitlines()
    max_rank = len(lines)
    hands = []
    #print("Analyzing...")
    for line in lines:
        spl = line.split()
        hands.append((analyze_hand_joker(spl[0], int(spl[1]))))

    sort = []
    
    #print("Sorting...")
    for hand_to_sort in hands:
        if len(sort) == 0:
            sort.append(hand_to_sort)
        else:
            inserted = 0
            spot = 0
            for sorted_hand in sort:
                if inserted == 1:
                    break
                if sorted_hand[0] == hand_to_sort[0]:
                    challenger = hand_to_sort[1]
                    sitting = sorted_hand[1]
                    done = False
                    for x in range(5):
                        if challenger[x] > sitting[x]:
                            spot += 1
                            done = True
                            break
                        elif challenger[x] < sitting[x]:
                            sort.insert(spot, hand_to_sort)
                            inserted = 1
                            done = True
                            break
                    if done != True:
                        sort.insert(spot, hand_to_sort)
                        inserted = 1

                elif sorted_hand[0] < hand_to_sort[0]:
                    spot += 1
                elif sorted_hand[0] > hand_to_sort[0]:
                    sort.insert(spot, hand_to_sort)
                    inserted = 1
            if inserted == 0:
                sort.append(hand_to_sort)
            else:
                pass
                #print("Inserted " + str(hand_to_sort) + " at index " + str(spot))
    #joker_print_sort(sort)
    x = 1
    winnings = 0
    #print("Calculating winnings...")
    for hand in sort:
        #print(str(winnings) + " += " + str(hand[2]) + " * " + str(x))
        winnings += (hand[2] * x)
        x += 1
    print("Part 2 Answer: " + str(winnings))


if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day7.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")