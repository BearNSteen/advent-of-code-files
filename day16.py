import time
from pathlib import Path
from copy import deepcopy
import sys

vis = []
test = []
keep = []

def light_trail(lines, start, direct):
    # global vis
    global test
    global keep
    test = []
    keep = []
    nex = [(start, direct)]
    while nex != []:
        
        start, new_dir = nex[0]
        check_x = (0 <= start[0] < len(lines))
        check_y = (0 <= start[1] < len(lines[0]))

        # if in range, and hasn't passed through tile in this direction b4
        if ((start, new_dir) not in test) and check_x and check_y:
            #print(nex)
            curr = lines[start[0]][start[1]]
            test.append((start, new_dir))

            # if tile never passed through
            if start not in keep:
                keep.append(start)

            # visualization (not necessary)
            """ if vis[start[0]][start[1]] not in ["<", ">", "^", "v"]:
                if vis[start[0]][start[1]] == ".":
                    if new_dir == "l":
                        symb = "<"
                    elif new_dir == "r":
                        symb = ">"
                    elif new_dir == "u":
                        symb = "^"
                    elif new_dir == "d":
                        symb = "v"
                    vis[start[0]][start[1]] = symb """
            
            # determine where to go next
            x, y = start[0], start[1]
            combo = None
            if (new_dir == "l" or new_dir == "r") and curr == "|":
                nex.append(((x+1, y), "d"))
                nex.append(((x-1, y), "u"))
            elif (new_dir == "u" or new_dir == "d") and curr == "-":
                nex.append(((x, y+1), "r"))
                nex.append(((x, y-1), "l")) 
            elif new_dir == "r":
                if curr == "\\":
                    combo = ((x+1, y), "d")
                elif curr == "/":
                    combo = ((x-1, y), "u")
                else:
                    combo = ((x, y+1), new_dir)
            elif new_dir == "l":
                if curr == "/":
                    combo = ((x+1, y), "d")
                elif curr == "\\":
                    combo = ((x-1, y), "u")
                else:
                    combo = ((x, y-1), "l")
            elif new_dir == "u":
                if curr == "/":
                    combo = ((x, y+1), "r")
                elif curr == "\\":
                    combo = ((x, y-1), "l")
                else:
                    combo = ((x-1, y), "u")
            elif new_dir == "d":
                if curr == "\\":
                    combo = ((x, y+1), "r")
                elif curr == "/":
                    combo = ((x, y-1), "l")
                else:
                    combo = ((x+1, y), "d")
            if combo != None:
                nex.append(combo)
        nex.remove(nex[0])
    return keep


def part_one(input, start=(0,0), direct="r", p2=0):
    lines = input.splitlines()
    """ for line in lines:
        print(line)
    print("----------------------") """
    for x in range(len(lines)):
        lines[x] = list(lines[x])
    global vis
    global keep
    total = 0

    vis = deepcopy(lines)

    keep = light_trail(lines, start, direct)

    tot = 0
    for x in range(len(vis)):
        for y in range(len(vis[x])):
            if (x, y) not in keep:
                vis[x][y] = " "

    """ print("=================")
    for line in vis:
        top = "".join(line)
        print(top) """

    total = len(keep)

    if p2 == 0:
        print("P1A: " + str(total))
        if total == 6883:
            print("Correct!")
        else:
            print("Nope!")
    # 6747 too low
    else:
        return total

def part_two(input):
    lines = input.splitlines()
    """ for line in lines:
        print(line)
    print("----------------------") """
    for x in range(len(lines)):
        lines[x] = list(lines[x])
    
    ans = 0
    x = 0
    for y in range(len(lines[x])):
        ans = max(ans, part_one(input, (x, y), "d", 1))
    x = len(lines)-1
    for y in range(len(lines[x])):
        ans = max(ans, part_one(input, (x, y), "u", 1))
    y = 0
    for x in range(len(lines)):
        ans = max(ans, part_one(input, (x, y), "r", 1))
    y = len(lines[0])-1
    for x in range(len(lines)):
        ans = max(ans, part_one(input, (x, y), "l", 1))
        
    print("P2A: " + str(ans))
    # 7228

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day16.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")