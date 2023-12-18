import time
from pathlib import Path
            

def part_one(input):
    lines = input.splitlines()
    directions = []
    for line in lines:
        spl = line.split()
        directions.append((spl[0], int(spl[1]), spl[2]))
    
    # find x / y range for plots
    y,x = 0,0
    my,mx = 0,0
    # left adjust, up adjust (to avoid negative indexes)

    cx, cy = 0,0
    grid = [(cx,cy)]
    steps = 0
    for d in directions:
        #print(cx, cy)
        destx, desty = cx, cy
        if d[0] == "R":
            cx = cx + d[1]
            destx = cx
        elif d[0] == "L":
            cx = cx - d[1]
            destx = cx
        elif d[0] == "U":
            cy = cy - d[1]
            desty = cy
        elif d[0] == "D":
            cy = cy + d[1]
            desty = cy
        grid.append((destx, desty))
        steps += d[1]

    #print(grid)

    inner = 0
    for i in range(len(grid)-1):
        (a,b),(c,d) = grid[i:i+2]
        inner += (a*d)-(b*c)
    result = abs(inner) // 2 + steps // 2 + 1

    print("P1A: " + str(result))
            

def part_two(input):
    lines = input.splitlines()
    hexes = []
    for line in lines:
        spl = line.split()
        hexes.append(spl[2])

    directions = []
   
    for hexi in hexes:
        to_add = []
        if hexi[-2] == "0":
            to_add.append("R")
        elif hexi[-2] == "1":
            to_add.append("D")
        elif hexi[-2] == "2":
            to_add.append("L")
        elif hexi[-2] == "3":
            to_add.append("U")
        to_add.append(int(("0x" + hexi[2:7]), 0))
        directions.append(to_add)

    cx, cy = 0,0
    grid = [(cx,cy)]
    steps = 0
    for d in directions:
        #print(cx, cy)
        destx, desty = cx, cy
        if d[0] == "R":
            cx = cx + d[1]
            destx = cx
        elif d[0] == "L":
            cx = cx - d[1]
            destx = cx
        elif d[0] == "U":
            cy = cy - d[1]
            desty = cy
        elif d[0] == "D":
            cy = cy + d[1]
            desty = cy
        grid.append((destx, desty))
        steps += d[1]

    print(grid)

    inner = 0
    for i in range(len(grid)-1):
        (a,b),(c,d) = grid[i:i+2]
        inner += (a*d)-(b*c)
    result = abs(inner) // 2 + steps // 2 + 1

    print("P2A: " + str(result))
    if result == 63806916814808:
        print("Correct!")

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day18.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")