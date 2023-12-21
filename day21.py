import time
from pathlib import Path
from copy import deepcopy

def part_one(input):
    lines = input.splitlines()
    steps = 0
    total_steps = 64

    grid = []
    for line in lines:
        new = []
        for item in line:
            new.append(item)
        grid.append(new)
    
    queue = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                queue.append([[y,x]])
    
    while steps < total_steps:
        #print(queue)
        to_add = []
        for item in queue[0]:
            #print(queue[0])
            y = item[0]
            x = item[1]
            
            if y-1 >= 0:
                if grid[y-1][x] != "#" and [y-1, x] not in to_add:
                    to_add.append([y-1, x])
            if x-1 >= 0:
                if grid[y][x-1] != "#" and [y, x-1] not in to_add:
                    to_add.append([y, x-1])
            if y+1 < len(grid):
                if grid[y+1][x] != "#" and [y+1, x] not in to_add:
                    to_add.append([y+1, x])
            if x+1 < len(grid[0]):
                if grid[y][x+1] != "#" and [y, x+1] not in to_add:
                    to_add.append([y, x+1])
        queue.append(to_add)
        queue.remove(queue[0])
        steps += 1
    
    ans = len(queue[0])
    print("P1A: " + str(ans))

def part_two(input):
    lines = input.splitlines()
    steps = 0
    total_steps = 26501365

    grid = []
    for line in lines:
        new = []
        for item in line:
            new.append(item)
        grid.append(new)
    
    queue = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                queue.append([[y,x,0,0]])
    
    dic = {}
    while steps < total_steps:
        print("============")
        print(steps)
        #print(queue)
        queue.append([])
        for item in queue[0]:
            #print(queue[0])
            y = item[0]
            x = item[1]
            wy = item[2]
            wx = item[3]
            to_add = []
            k = str(y)+str(x)+str(wy)+str(wx)

            if k not in dic.keys():
                if y-1 >= 0:
                    if grid[y-1][x] != "#" and [y-1, x, wy, wx] not in to_add:
                        to_add.append([y-1, x, wy, wx])
                else:
                    if grid[len(grid)-1][x] != "#" and [len(grid)-1, x, wy-1, wx] not in to_add:
                        to_add.append([len(grid)-1, x, wy-1, wx])

                if x-1 >= 0:
                    if grid[y][x-1] != "#" and [y, x-1] not in to_add:
                        to_add.append([y, x-1, wy, wx])
                else:
                    if grid[y][len(grid[0])-1] != "#" and [y, len(grid[0])-1, wy, wx-1] not in to_add:
                        to_add.append([y, len(grid[0])-1, wy, wx-1])

                if y+1 < len(grid):
                    if grid[y+1][x] != "#" and [y+1, x] not in to_add:
                        to_add.append([y+1, x, wy, wx])
                else:
                    if grid[0][x] != "#" and [0, x, wy+1, wx] not in to_add:
                        to_add.append([0, x, wy+1, wx])

                if x+1 < len(grid[0]):
                    if grid[y][x+1] != "#" and [y, x+1] not in to_add:
                        to_add.append([y, x+1, wy, wx])
                else:
                    if grid[y][0] != "#" and [y, 0, wy, wx+1] not in to_add:
                        to_add.append([y, 0, wy, wx+1])
                dic[k] = deepcopy(to_add)
            else:
                to_add = dic[k]
            
            for item in to_add:
                if item not in queue[1]:
                    queue[1].append(item)

        queue.append(to_add)
        queue.remove(queue[0])
        steps += 1
    
    ans = len(queue[0])
    print("P2A: " + str(ans))

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day21.txt").read_text()
    # part 1
    #part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")