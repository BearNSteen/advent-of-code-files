import time
from pathlib import Path
from math import lcm

def part_one(input):
    lines = input.splitlines()
    route = []
    for direction in lines[0]:
        route.append(direction)
    r_dict = {}
    for line in lines[2:]:
        spl = line.split()
        r_dict[spl[0]] = (spl[2][1:4], spl[3][:3])

    curr = 'AAA'
    step = 0
    total = 0
    while curr != 'ZZZ':
        go = route[step]
        if go == 'L':
            curr = r_dict[curr][0]
        elif go == 'R':
            curr = r_dict[curr][1]
        step += 1
        total += 1
        if step >= len(route):
            step = 0
    print("PART 1 ANSWER: " + str(total))

def part_two(input):
    # need to find the distance between "Z" node and itself in a loop
    # need to keep track of what index of directions it takes to get from "A" to "Z" initially
    # how do you keep track of all the "Z" nodes? How do you know they are reached by any of the coordinates at any time?
    lines = input.splitlines()
    route = []
    for direction in lines[0]:
        route.append(direction)
    r_dict = {}
    for line in lines[2:]:
        spl = line.split()
        r_dict[spl[0]] = (spl[2][1:4], spl[3][:3])

    curr = []
    for key in r_dict.keys():
        if key[2] == 'A':
            curr.append(key)
    step = 0
    total = 0
    on_z = 0
    loops = []
    done = 0
    while done < len(curr):
        if route[step] == 'L':
            go = 0
        else:
            go = 1
        for c in range(len(curr)):
            if curr[c] != "DONE":
                curr[c] = r_dict[curr[c]][go]
        step += 1
        total += 1
        if step == len(route):
            step = 0
        for c in range(len(curr)):
            if curr[c][2] == 'Z':
                loops.append(total)
                curr[c] = "DONE"
                done += 1
    
    print(loops)
    a, b, c, d, e, f = loops[0], loops[1], loops[2], loops[3], loops[4], loops[5]
      
    print("PART 2 ANSWER: " + str(lcm(a,b,c,d,e,f)))

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day8.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")