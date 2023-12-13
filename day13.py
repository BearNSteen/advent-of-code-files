import time
from pathlib import Path

a = 0
b = 0

def check_columns(lines, start, stop):
    # checks if there is a pattern that a vertical line can separate
    global a
    
    not_found = 0

    midl = (stop - start) // 2 + start
    midr = midl+1

    for x in range(len(lines)):
        
        left = lines[x][start:midr]
        right = lines[x][midr:stop+1]
        right.reverse()
        
        print((start, stop), left, right)

        if left != right:
            not_found = 1
            break                

    if not_found != 1:
        #print("Found at line " + str(midl))
        if a < midl+1:
            a = midl+1


def check_rows(lines, start, stop):
    # checks if there is a pattern that a horizontal line can separate
    global b
    
    not_found = 0

    # print("ROWS: " + str(start) + ", " + str(stop))
    midl = (stop - start) // 2 + start
    midr = midl+1

    for x in range(len(lines[0])):
        # lines [row] [col]
        left = []
        for val in range(start, midr):
            left.append(lines[val][x])
        
        right = []
        for val in range(midr, stop+1):
            right.append(lines[val][x])

        right.reverse()

        print((start, stop), left, right)

        if left != right:
            not_found = 1
            break

    if not_found != 1:
        #print("Found at line " + str(midl))
        if b < midl+1:
            b = midl+1
    
    return

def part_one(input):
    lines = input.splitlines()
    global a
    global b
    groups = []
    temp = []
    for line in lines:
        if line == "":
            groups.append(temp)
            temp = []
        else:
            temp.append(list(line))

    total = 0
    for group in groups:
        a = 0
        b = 0
        s1 = len(group[0])-1
        s2 = len(group)-1
        print("COLS")
        for x in range(s1):
            if (s1-x) % 2 == 1:
                check_columns(group, x, s1)
                if a != 0:
                    break
        save = a
        a = 0
        for x in range(s1):
            if (s1-x) % 2 == 1:
                check_columns(group, 0, s1-x)
                if a != 0:
                    break  
        a = max(a, save)
        print("ROWS")
        for x in range(s2):
            if (s2-x) % 2 == 1:
                check_rows(group, x, s2)
                if b != 0:
                    break
        save = b
        b = 0
        for x in range(s2):
            if s2-x >= 0:
                if (s2-x) % 2 == 1:
                    check_rows(group, 0, s2-x)
                    if b != 0:
                        break
        b = max(save, b)
        # may need if a > b stuff
        if a > b:
            total += a
        elif b > a:
            total += b*100
        
        
    print("P1 Answer: " + str(total))
    if total == 29130:
        print("Correct!")
    else:
        print("Incorrect! (Answer = 29130)")
        print("Distance to answer: " + str(abs(29130-total)))


def part_two(input):
    pass

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day13.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")