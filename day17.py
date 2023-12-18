import time
from pathlib import Path

grid = []
went = []

def fill_grid(lines, curr, step, last_dir, total, stack, gone=[]):
    y,x = curr[0], curr[1]
    global went
    go_step = step
    value = int(lines[y][x])
    new_total = total + value
    m = min(grid[y][x], new_total) 
    if m == new_total:
        grid[y][x] = new_total
    else:
        return
    if y == len(lines)-1 and x == len(lines[0])-1:
        went = []
        return
    if ((y,x), last_dir) not in gone:
        gone.append(((y,x), last_dir))
        cantgo = []
        dic = {"d":"u", "u": "d", "l":"r", "r":"l"}
        if last_dir != None:
            cantgo.append(dic[last_dir])  
        if go_step == 3:
            cantgo.append(last_dir)
            go_step = 0
        if x == 0 and y == 0:
            new_total = 0
        if y-1 >= 0 and "u" not in cantgo:
            if "u" == last_dir:
                fill_grid(lines, (y-1, x), 1+go_step, "u", new_total, stack, gone)
            else:
                fill_grid(lines, (y-1, x), 1, "u", new_total, stack, gone)
        if y+1 < len(lines) and "d" not in cantgo:
            if "d" == last_dir:
                fill_grid(lines, (y+1, x), 1+go_step, "d", new_total, stack, gone)
            else:
                fill_grid(lines, (y+1, x), 1, "d", new_total, stack, gone)
        if x-1 >= 0 and "l" not in cantgo:
            if "l" == last_dir:
                fill_grid(lines, (y, x-1), 1+go_step, "l", new_total, stack, gone)
            else:
                fill_grid(lines, (y, x-1), 1, "l", new_total, stack, gone)
        if x+1 < len(lines[0]) and "r" not in cantgo:
            if "r" == last_dir:
                fill_grid(lines, (y, x+1), 1+go_step, "r", new_total, stack, gone)
            else:
                fill_grid(lines, (y, x+1), 1, "r", new_total, stack, gone)
    else: return

def check_grid(lines, curr, step, last_dir, total):
    y,x = curr[0], curr[1]
    go_step = step
    value = int(lines[y][x])
    to_check = []
    global grid
    a = 100000
    b = 100000
    if y-1 > 0:
        a = value+grid[y-1][x]
    if x-1 > 0:
        b = value+grid[y][x-1]
    grid[y][x] = min(a,b)
    

def part_one(input):
    lines = input.splitlines()
    for line in lines:
        line = list(line)
    
    global grid
    grid = [[100000 for _ in lines[0]] for _ in lines]
    steps = 0
    curr = (0,0)
    total = 0
    stack = []
    fill_grid(lines, curr, steps, None, total, stack)
    for x in range(len(lines)):
        line = list(lines[x])
        for y in range(len(lines[x])):
            line[y] = int(lines[x][y])
        lines[x] = line
    for x in range(len(grid)):
        #print(list(lines[x]))
        print(grid[x])
    ans = grid[len(grid)-1][len(grid[0])-1]

    print("P1 Answer: " + str(ans))

def part_two(input):
    pass

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day17.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")