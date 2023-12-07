import time
from pathlib import Path

class Hand():
    def __init__(self, value, bid):
        _value = value
        _bid = bid
        _rank = 0
        _highs = []
        self.hand = 0
        self.cards = []
        self.analyze_hand(value)

    def analyze_hand(self, value):
        cards = []
        for x in range(len(value)):
            if value[x] == "T":
                to_add = "11"
            elif value[x] == "J":
                to_add = "12"
            elif value[x] == "Q":
                to_add = "13"
            elif value[x] == "K":
                to_add = "14"
            elif value[x] == "A":
                to_add = "15"
            else:
                to_add = value[x]
            cards.append(to_add)
            self.cards = cards

        sort_cards = cards
        sort_cards.sort()
        prev = 0
        vals = []
        for val in sort_cards:
            if prev == 0:
                prev = val
                curr_tot = 1
            if prev != val:
                vals.append((prev, curr_tot))
                prev = val
                curr_tot = 1
            else:
                curr_tot += 1
        vals.append((prev, curr_tot))

        check_full_house = 0
        for pair in vals:
            if check_full_house != 0:
                if pair[1] != 1:
                    if pair[1] == 3 and check_full_house == 2:
                        self.hand = 5
                    elif pair[1] == 2 and check_full_house == 3:
                        self.hand = 5
                    elif pair[1] == 2 and check_full_house == 2:
                        self.hand = 3
                    elif pair[1] != 3 and check_full_house == 2:
                        self.hand = 4
                    check_full_house = 0
            elif pair[1] == 5:
                self.hand = 7
            elif pair[1] == 4:
                self.hand = 6
            elif pair[1] == 3:
                check_full_house = 3
            elif pair[1] == 2:
                check_full_house = 2

        
       

    def get_hand(self):
        return self.hand
    
    def get_highs(self):
        return self._highs
    
    def get_cards(self):
        return self.cards
    
    def get_bid(self):
        return self._bid
    
    def set_rank(self, val):
        self.rank = val


def part_one(input):
    print("PART 1 --------------------------")
    lines = input.splitlines()
    max_rank = len(lines)
    hands = []
    print("Analyzing...")
    for line in lines:
        spl = line.split()
        hands.append(Hand(spl[0], int(spl[1])))
    sorting_by_hand = []
    print("Sorting...")
    for hand in hands:
        if len(sorting_by_hand) == 0:
            sorting_by_hand.append(hand)
        else:
            spot = 0
            for h in sorting_by_hand:
                if h.get_hand() == hand.get_hand():
                    challenger = hand.get_cards()
                    sitting = h.get_cards()
                    done = False
                    for x in range(5):
                        if challenger[x] > sitting[x]:
                            spot += 1
                            done = True
                            break
                        elif challenger[x] < sitting[x]:
                            sorting_by_hand.insert(spot, hand)
                            done = True
                            break
                    if done != True:
                        sorting_by_hand.insert(spot, hand)

                elif h.get_hand() < hand.get_hand():
                    spot += 1
                elif h.get_hand() > hand.get_hand():
                    sorting_by_hand.insert(spot, hand)
    x = 1
    winnings = 0
    print("Calculating winnings...")
    for hand in sorting_by_hand:
        winnings += (hand.get_bid() * x)
        x += 1
        


def part_two(input):
    pass


if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day7.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")