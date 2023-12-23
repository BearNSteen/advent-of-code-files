import time
from pathlib import Path
from copy import deepcopy

def find_path(grid, start, tot, d, part):
    passed = {}
    ans = 0
    y = start[0]
    x = start[1]
    curr = grid[y][x]
    queue = []
    queue.append([start, tot, d, {}])
    found = []
    gone = {}


    while len(queue) > 0:
        c = queue[0]
        start = c[0]
        y = start[0]
        x = start[1]


        total = c[1]
        came_from = c[2]

        curr = grid[y][x]

        moves_made = deepcopy(c[3])

        skip = 0
        if y == len(grid)-1:
            found.append(total)
            ans = max(ans, total)
            print(found)

        if start in passed.keys():
            if total < passed[start]:
                skip = 1
            else:
                passed[start] = total
        
        # if move has already been made with a higher amount, skip
        if skip == 0:
            if str(start) in moves_made.keys():
                skip = 1
            else:
                moves_made[str(start)] = total

        if skip == 0:
            key = str(start)+came_from
            if key in gone.keys():
                if gone[key] < total:
                    gone[key] = total
                else:
                    skip = 1
            else:
                gone[key] = total

        if part == 1:
            check = curr=="."
        else:
            check = curr!="#"
        
        if skip == 0:

            # find out if it is surrounded by ><^v
            arrows = [">", "<", "^", "v"]
            a = 0
            if curr == ".":
                if y-1 > 0:
                    if grid[y-1][x] in arrows:
                        a += 1
                if y+1 < len(grid):
                    if grid[y+1][x] in arrows:
                        a += 1
                if x-1 > 0:
                    if grid[y][x-1] in arrows:
                        a += 1
                if x+1 < len(grid):
                    if grid[y][x+1] in arrows:
                        a += 1
            if a > 2:
                # it is an intersection not in keys
                passed[start] = total

            if check:
                if came_from != "N":
                    if y-1 > -1:
                        if grid[y-1][x] != "#":
                            queue.append([(y-1, x), total+1, "S", moves_made])
                if came_from != "S":
                    if y+1 < len(grid):
                        if grid[y+1][x] != "#":
                            queue.append([(y+1, x), total+1, "N", moves_made])
                if came_from != "E":
                    if x+1 < len(grid[0]):
                        if grid[y][x+1] != "#":
                            queue.append([(y, x+1), total+1, "W", moves_made])
                if came_from != "W":
                    if x-1 > -1:
                        if grid[y][x-1] != "#":
                            queue.append([(y, x-1), total+1, "E", moves_made])

            elif part == 1:
                if curr == ">":
                    if came_from != "E":
                        if grid[y][x+1] != "#":
                            queue.append([(y, x+1), total+1, "W", moves_made])
                elif curr == "<":
                    if came_from != "W":
                        if grid[y][x-1] != "#":
                            queue.append([(y, x-1), total+1, "E", moves_made])
                elif curr == "v":
                    if came_from != "S":
                        if grid[y+1][x] != "#":
                            queue.append([(y+1, x), total+1, "N", moves_made])
                elif curr == "^":
                    if came_from != "N":
                        if grid[y-1][x] != "#":
                            queue.append([(y-1, x), total+1, "S", moves_made])
        
        queue.remove(queue[0])
    print(found)
    return ans
        


def part_one(input):
    lines = input.splitlines()
    grid = []
    for line in lines:
        grid.append(list(line))

    start = (0,1)
    ans = find_path(grid, start, 0, "N", 1)

    print("P1A: " + str(ans))


def part_two(input):
    lines = input.splitlines()
    grid = []
    for line in lines:
        grid.append(list(line))

    start = (0,1)
    ans = find_path(grid, start, 0, "N", 2)

    print("P2A: " + str(ans))

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day23.txt").read_text()
    # part 1
    #part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")