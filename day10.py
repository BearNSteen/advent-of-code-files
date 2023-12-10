import time
from pathlib import Path
from colorama import Fore

def get_type_pipe(pipe):
    if pipe == "F":
        d = ["r", "d"]
    elif pipe == "L":
        d = ["u", "r"]
    elif pipe == "J":
        d = ["l", "u"]
    elif pipe == "7":
        d = ["l", "d"]
    elif pipe == "|":
        d = ["u", "d"]
    elif pipe == "-":
        d = ["l", "r"]
    elif pipe == "S":
        d = ["u", "d", "l", "r"]
    return d

def find_pipe(x, y, prev, lines):
    curr = lines[x][y]

    # get directions of current pipe
    d = get_type_pipe(curr)
    if "u" in d:
        if x-1 >= 0:
            pipe = lines[x-1][y]
            if (x-1, y) != prev:
                if pipe in ["F", "|", "7", "S"]:
                    return x-1, y
    if "d" in d:
        if x+1 < len(lines):
            pipe = lines[x+1][y]
            if (x+1, y) != prev:
                if pipe in ["J", "L", "|", "S"]:
                    return x+1, y
    if "l" in d:
        if y-1 >= 0:
            pipe = lines[x][y-1]
            if (x, y-1) != prev:
                if pipe in ["L", "F", "-", "S"]:
                    return x, y-1
    if "r" in d:
        if y+1 < len(lines[x]):
            pipe = lines[x][y+1]
            if (x, y+1) != prev:
                if pipe in ["7", "J", "-", "S"]:
                    return x, y+1

def part_one(input):
    lines = input.splitlines()
    s = (0, 0)

    # find S
    for x in range(len(lines)):
        curr = lines[x]
        for y in range(len(curr)):
            if curr[y] == "S":
                s = (x, y)
                break
        if s[1] == "S":
            break

    x = s[0]
    y = s[1]
    start = (x, y)
    prev = (x, y)
    # traverse the pipes
    x, y = find_pipe(x, y, prev, lines)
    total = 1
    while (x, y) != start:
        tempx, tempy = x, y
        x, y = find_pipe(x, y, prev, lines)
        prev = (tempx, tempy)
        total += 1
    print("P1 Answer: " + str(total/2))    

def check_for_o(lines, x, y):
    if x-1 >= 0:
        if lines[x-1][y] == "O":
            return True
    if x+1 < len(lines):
        if lines[x+1][y] == "O":
            return True
    if y-1 >= 0:
        if lines[x][y-1] == "O":
            return True
    if y+1 < len(lines):
        if lines[x][y+1] == "O":
            return True
    return False

def check_for_p(lines, x, y, exempt=[]):
    touching = []
    nop = []
    top = 4
    if x-1 >= 0:
        if lines[x-1][y] == "P" or (x-1, y) in exempt:
            touching.append((x-1, y))
        else:
            nop.append((x-1, y))
    else:
        top -= 1
    if x+1 < len(lines):
        if lines[x+1][y] == "P" or (x+1, y) in exempt:
            touching.append((x+1, y))
        else:
            nop.append((x+1, y))
    else:
        top -= 1
    if y-1 >= 0:
        if lines[x][y-1] == "P" or (x, y-1) in exempt:
            touching.append((x, y-1))
        else:
            nop.append((x, y-1))
    else:
        top -= 1
    if y+1 < len(lines):
        if lines[x][y+1] == "P" or (x, y+1) in exempt:
            touching.append((x, y+1))
        else:
            nop.append((x, y+1))
    else:
        top -= 1
    if top != 4:
        return False
    if len(touching) == 4:
        return True
    if touching == 3 and top == 4:
        if (nop[0][0], nop[0][1]) in exempt:
            return True
        exempt.append((x,y))
        if check_for_p(lines, nop[0][0], nop[0][1], exempt):
            return True
    elif touching == 2 and top == 4:
        exempt.append((x,y))
        if (nop[0][0], nop[0][1]) in exempt:
            if check_for_p(lines, nop[1][0], nop[1][1], exempt):
                return True
        elif (nop[1][0], nop[1][1]) in exempt:
            if check_for_p(lines, nop[0][0], nop[0][1], exempt):
                return True
        else:
            one = check_for_p(lines, nop[1][0], nop[1][1], exempt)
            two = check_for_p(lines, nop[0][0], nop[0][1], exempt)
            if one and two:
                return True
    else:
        return False

def find_route_p2(input):
    lines = input.splitlines()
    s = (0, 0)

    # find S
    for x in range(len(lines)):
        curr = lines[x]
        for y in range(len(curr)):
            if curr[y] == "S":
                s = (x, y)
                break
        if s[1] == "S":
            break

    x = s[0]
    y = s[1]
    start = (x, y)
    prev = (x, y)
    # traverse the pipes
    x, y = find_pipe(x, y, prev, lines)
    total = 1
    route = []
    while (x, y) != start:
        route.append(prev)
        tempx, tempy = x, y
        x, y = find_pipe(x, y, prev, lines)
        prev = (tempx, tempy)
        total += 1
    
    new_lines = []
    for x in range(len(lines)):
        spl = list(lines[x])
        for y in range(len(spl)):
            if (x, y) not in route:
                spl[y] = "X"
            """else:
                if spl[y] == "7":
                    spl[y] = "┑"
                if spl[y] == "L":
                    spl[y] = "┕"
                if spl[y] == "J":
                    spl[y] = "┙"
                if spl[y] == "F":
                    spl[y] = "┍"
                    """
        new_lines.append(''.join(spl))
    
    return new_lines

def check_boundary(lines, x, y):
    cx = x
    cy = y
    if x > 123:
        d = 1
        s = "x"
    elif x < 13:
        d = -1
        s = "x"
    elif y < 20:
        d = -1
        s = "y"
    elif y > 117:
        d = 1
        s = "y"
    else:
        d = 1
        s = "y"

    crossed = 0
    while cx >= 0 and cx < len(lines) and cy >= 0 and cy < len(lines[0]):
        if lines[cx][cy] in ["-", "F", "J", "7", "L"]:
            crossed += 1
        cx += d
        
    if crossed % 2 == 1:
            return True

    cx = x
    while cx >= 0 and cx < len(lines) and cy >= 0 and cy < len(lines[0]):
        if lines[cx][cy] in ["-", "F", "J", "7", "L"]:
            crossed += 1
        cy += d

    if crossed % 2 == 1:
        return True
    return False

    

def part_two(input):
    lines = input.splitlines()
    total = 0

    new_lines = find_route_p2(input)
    new_lines2 = []

    # 87 - 117
    # 32 - 104

    for x in range(len(new_lines)):
        spl = list(new_lines[x])
        for y in range(len(spl)):
            if spl[y] == "X":
                if check_boundary(new_lines, x, y):
                    spl[y] = "I"
                    total += 1
                else:
                    if spl[y] != "P":
                        spl[y] == "O"
                """
                if check_for_p(new_lines, x, y):
                    spl[y] = "I"
                    total += 1
                else:
                    if spl[y] != "P":
                        spl[y] = "O"
                """
        new_lines2.append(''.join(spl))

    """

    # replace all outer periods with Os
    for val in [0, len(lines)-1]:
        spl = list(lines[val])
        for y in range(len(spl)):
            if spl[y] == ".":
                spl[y] = "O"
        lines[val] = ''.join(spl)

    for x in range(len(lines)):
        spl = list(lines[x])
        for val in [0, len(lines[0])-1]:
            if spl[val] == ".":
                spl[val] = "O"
        lines[x] = ''.join(spl)

    for x in range(len(lines)):
        spl = list(lines[x])
        for y in range(len(spl)):
            if spl[y] == ".":
                if check_for_o(lines, x, y):
                    spl[y] = "O"
        
    # find what periods are within the route
    """

    for line in new_lines2:
        print(line)
    print("P2 Answer: " + str(total))
    if 575 < total < 647:
        print("Try this answer!")
    # 647 is too high
    # 575 is too low

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day10.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")