import time
from pathlib import Path

def part_one(input):
    lines = input.splitlines()
    spl = []
    for x in range(len(lines)):
        spl.append(list(lines[x]))

    # find rows with periods
    dx = []
    for x in range(len(spl)):
        if '#' not in spl[x]:
            dx.append(x)
    l = len(spl[0])
    to_insert = ['.' for _ in range(l)]
    added = 0
    for num in dx:
        spl.insert(num+added, to_insert.copy())
        added += 1

    # find columns with periods
    dy = []
    pairs = []
    for y in range(len(spl[0])):
        found = 0
        for x in range(len(spl)):
            if spl[x][y] == '#':
                found = 1
        if found == 0:
            if y not in dy:
                dy.append(y)
    #print("dy: " + str(dy))
    added = 0
    for x in range(len(dy)):
        dy[x] += added
        added += 1
    for x in range(len(spl)):
        #print(str(spl[x]))
        for y in dy:
            spl[x].insert(y, '.')

    print("==================")

    for x in range(len(spl)):
        for y in range(len(spl[0])):
            if spl[x][y] == '#':
                pairs.append((x, y))

    # find distances
    # 7,1 -> 12, 5
    # 12 - 7 = 5, 5 - 1 = 4, 5+4 = 9
    total = 0
    t_add = 0
    for x in range(len(pairs)): 
        for y in range(x+1, len(pairs)):
            pair = pairs[x]
            pair2 = pairs[y]
            if pair != pair2:
                #print(pair, pair2)
                dist = abs(pair[0] - pair2[0]) + abs(pair[1] - pair2[1])
                total += dist
                t_add += 1

    print("Part 1: " + str(total))

def part_two(input):
    lines = input.splitlines()
    spl = []
    for x in range(len(lines)):
        spl.append(list(lines[x]))

    # find rows with periods
    dx = []
    for x in range(len(spl)):
        if '#' not in spl[x]:
            dx.append(x)


    # find columns with periods
    dy = []
    pairs = []
    for y in range(len(spl[0])):
        found = 0
        for x in range(len(spl)):
            if spl[x][y] == '#':
                pairs.append((x, y))
                found = 1
        if found == 0:
            if y not in dy:
                dy.append(y)
                
    print("dx: " + str(dx))
    print("dy: " + str(dy))
    print("Pairs: " + str(pairs))
    print("==================")

    # find distances
    # 7,1 -> 12, 5
    # 12 - 7 = 5, 5 - 1 = 4, 5+4 = 9
    total = 0
    mod = 100000
    for x in range(len(pairs)): 
        for y in range(x+1, len(pairs)):
            pair = pairs[x]
            pair2 = pairs[y]
            if pair != pair2:
                #print(pair, pair2)
                dist = abs(pair[0] - pair2[0]) + abs(pair[1] - pair2[1])
                if pair[0] > pair2[0]:
                    gr_x = pair[0]
                    ls_x = pair2[0]
                else:
                    gr_x = pair2[0]
                    ls_x = pair[0]
                for value in dx:
                    if ls_x < value < gr_x:
                        dist += (10*mod - 1)
                if pair[1] > pair2[1]:
                    gr_y = pair[1]
                    ls_y = pair2[1]
                else:
                    gr_y = pair2[1]
                    ls_y = pair[1]
                for value in dy:
                    if ls_y < value < gr_y:
                        dist += (10*mod-1)
                total += dist

    print("Part 2: " + str(total))


if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day11.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")