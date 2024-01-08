def check_for_symbol(t, row, col, size):
    checked = []
    check = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
    # top left
    if 0 <= row-1 < len(t):
        if 0 <= col-1 < len(t[row-1]):
            checked.append(t[row-1][col-1])
            if t[row-1][col-1] not in check:
                return True
    # above
    if 0 <= row-1 < len(t):
        if 0 <= col+size < len(t[row-1]):
            for x in range(size):
                checked.append(t[row-1][col+x])
                if t[row-1][col+x] not in check:
                    return True
    # top right
    if 0 <= row-1 < len(t):
        if 0 <= col+size < len(t[row-1]):
            checked.append(t[row-1][col+size])
            if t[row-1][col+size] not in check:
                return True
    # left
    if 0 <= col-1 < len(t[row]):
        checked.append(t[row][col-1])
        if t[row][col-1] not in check:
            return True
    # right
    if 0 <= col+size < len(t[row]):
        checked.append(t[row][col-1])
        if t[row][col+size] not in check:
            return True
    # bottom left
    if 0 <= row+1 < len(t):
        if 0 <= col-1 < len(t[row+1]):
            if t[row+1][col-1] not in check:
                return True
    # below
    if 0 <= row+1 < len(t):
        if 0 <= col+size < len(t[row+1]):
            for x in range(size):
                checked.append(t[row+1][col+x])
                if t[row+1][col+x] not in check:
                    return True
    # bottom right
    if 0 <= row+1 < len(t):
        if 0 <= col+size < len(t[row+1]):
            if t[row+1][col+size] not in check:
                return True
    return False

def check_for_gear(t, row, col, size):
    checked = []
    check = ["*"]
    # top left
    if 0 <= row-1 < len(t):
        if 0 <= col-1 < len(t[row-1]):
            checked.append(t[row-1][col-1])
            if t[row-1][col-1] in check:
                return str(row-1)+str(col-1)
    # above
    if 0 <= row-1 < len(t):
        if 0 <= col+size < len(t[row-1]):
            for x in range(size):
                checked.append(t[row-1][col+x])
                if t[row-1][col+x] in check:
                    return str(row-1)+str(col+x)
    # top right
    if 0 <= row-1 < len(t):
        if 0 <= col+size < len(t[row-1]):
            checked.append(t[row-1][col+size])
            if t[row-1][col+size] in check:
                return str(row-1)+str(col+size)
    # left
    if 0 <= col-1 < len(t[row]):
        checked.append(t[row][col-1])
        if t[row][col-1] in check:
            return str(row)+str(col-1)
    # right
    if 0 <= col+size < len(t[row]):
        checked.append(t[row][col-1])
        if t[row][col+size] in check:
            return str(row)+str(col+size)
    # bottom left
    if 0 <= row+1 < len(t):
        if 0 <= col-1 < len(t[row+1]):
            if t[row+1][col-1] in check:
                return str(row+1)+str(col-1)
    # below
    if 0 <= row+1 < len(t):
        if 0 <= col+size < len(t[row+1]):
            for x in range(size):
                checked.append(t[row+1][col+x])
                if t[row+1][col+x] in check:
                    return str(row+1)+str(col+x)
    # bottom right
    if 0 <= row+1 < len(t):
        if 0 <= col+size < len(t[row+1]):
            if t[row+1][col+size] in check:
                return str(row+1)+str(col+size)
    return False

def find_parts(input):
    total = 0
    size = 0
    number = False
    found = []
    check = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    t = input.splitlines()
    for row in range(len(t)):
        for col in range(len(t[row])):
            if t[row][col] in check:
                if number == False:
                    number = True
                    size = 1
                    for x in range(col+1,len(t[row])):
                        if t[row][x].isnumeric():
                            size += 1 
                        else:
                            break
                    if check_for_symbol(t, row, col, size):
                        numstr = ""
                        for x in range(size):
                            numstr = numstr + t[row][col+x]
                        total += int(numstr)
                        found.append(numstr)
            else:
                if number == True:
                    number = False
    print("Part 1: " + str(total))
    #print(found)

def find_gears(input):
    gears_dict = {}
    total = 0
    size = 0
    number = False
    found = []
    check = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    t = input.splitlines()
    for row in range(len(t)):
        for col in range(len(t[row])):
            if t[row][col] in check:
                if number == False:
                    number = True
                    size = 1
                    for x in range(col+1,len(t[row])):
                        if t[row][x].isnumeric():
                            size += 1 
                        else:
                            break
                    gear = check_for_gear(t, row, col, size)
                    if gear != False:
                        numstr = ""
                        for x in range(size):
                            numstr = numstr + t[row][col+x]
                        if gear not in gears_dict.keys():
                            gears_dict[gear] = int(numstr)
                        else:
                            total += (int(numstr) * gears_dict[gear])
            else:
                if number == True:
                    number = False
    print("Part 2: " + str(total))
    #print(found)

if __name__ == "__main__":
    input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    # part 1
    find_parts(input)
    # part 2
    find_gears(input)


