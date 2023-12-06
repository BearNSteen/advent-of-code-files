def analyze_card(input):
    total_points = 0
    lines = input.splitlines()
    for line in lines:
        winning_numbers = 0
        winning = []
        have = []
        s = line.split()
        #print(s)
        half = 1
        for x in range(2, len(s)):
            if half == 1:
                if s[x] == "|":
                    half = 2
                else:
                    winning.append(s[x])
            elif half == 2:
                have.append(s[x])
        #print(winning)
        #print(have)
        for value in winning:
            if value in have:
                winning_numbers += 1 
        if winning_numbers > 0:
            #debug
            #print("Card " + s[1] + " has " + str(winning_numbers) + " winning numbers! This adds a score of " + str(2**(winning_numbers-1)) + "!")
            pass
        if winning_numbers > 0:
            total_points += 2**(winning_numbers-1)
    print("Part 1: " + str(total_points))

def analyze_dupes(input):
    total_cards = 0
    count = {}
    lines = input.splitlines()
    for x in range(len(lines)):
        count[x] = 1
    index = 0
    for line in lines:
        winning_numbers = 0
        winning = []
        have = []
        s = line.split()
        #print(s)
        half = 1
        for x in range(2, len(s)):
            if half == 1:
                if s[x] == "|":
                    half = 2
                else:
                    winning.append(s[x])
            elif half == 2:
                have.append(s[x])
        #print(winning)
        #print(have)
        for value in winning:
            if value in have:
                winning_numbers += 1 
        if winning_numbers > 0:
            for x in range(1, winning_numbers+1):
                count[index+x] += count[index]
        index += 1
    for x in range(len(lines)):
        total_cards += count[x]
    print(count)
    print("Part 2: " + str(total_cards))
                
                
                
    


if __name__ == "__main__":
    input = "input"
    # part 1
    analyze_card(input)
    # part 2
    analyze_dupes(input)