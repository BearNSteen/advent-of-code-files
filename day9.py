import time
from pathlib import Path

def part_one(input):
    lines = input.splitlines()
    total = 0
    for x in range(len(lines)):
        values = [[]]
        xs = lines[x].split()
        for value in xs:
            values[0].append(int(value))
        added = 1
        y = 0
        while added != 0:
            values.append([])
            added = 0
            for z in range(len(values[y])-1):
                diff = values[y][z+1] - values[y][z]
                values[y+1].append(diff)
                if diff != 0:
                    added = 1
            y+=1
        print(values)
        values[-1].append(0)
        for z in range(len(values)-2, -1, -1):
            new = values[z][-1] + values[z+1][-1]
            values[z].append(new)
        total += values[0][-1]
    print("Part 1: " + str(total))


def part_two(input):
    # part 1 backwards
    lines = input.splitlines()
    total = 0
    for x in range(len(lines)):
        values = [[]]
        xs = lines[x].split()
        for value in xs:
            values[0].append(int(value))
        added = 1
        y = 0
        while added != 0:
            values.append([])
            added = 0
            for z in range(len(values[y])-1):
                diff = values[y][z+1] - values[y][z]
                values[y+1].append(diff)
                if diff != 0:
                    added = 1
            y+=1
        values[-1].insert(0, 0)
        for z in range(len(values)-2, -1, -1):
            new = values[z][0] - values[z+1][0]
            values[z].insert(0, new)
        print(values)
        total += values[0][0]
    print("Part 2: " + str(total))
    # 19551 is too high

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day8.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")