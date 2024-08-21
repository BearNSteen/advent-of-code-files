"""
Advent of Code 2023 - Day 2 Solution

This script solves the Day 2 puzzle of Advent of Code 2023.
It calculates the sum of valid game IDs in Part 1 and the sum of power of minimum cube sets in Part 2.

Problem Description:
The puzzle involves analyzing games where colored cubes are drawn from a bag.
Part 1: Determine which games would have been possible with a specific number of cubes.
Part 2: Calculate the minimum number of cubes of each color needed for each game.

Author: Dan
Date: December 2, 2023
"""

import time
from pathlib import Path

def parse_input(input_string):
    """Parse the input string into a list of lines."""
    return input_string.splitlines()

def part_one(data):
    """Solve part one of the puzzle."""
    total = 0
    for line in data:
        skip = False
        dic = {"r": 12, "g": 13, "b": 14}
        split_list = line.split()
        for x in range(2, len(split_list), 2):
            num = int(split_list[x])
            color = split_list[x+1]
            if dic[color[0]] < num:
                skip = True
                break
        if not skip:
            total += int(split_list[1][:-1])
    return total

def part_two(data):
    """Solve part two of the puzzle."""
    total = 0
    for line in data:
        dic = {"r": 0, "g": 0, "b": 0}
        split_list = line.split()
        for x in range(2, len(split_list), 2):
            num = int(split_list[x])
            color = split_list[x+1]
            if dic[color[0]] < num:
                dic[color[0]] = num
        total += (dic["r"] * dic["g"] * dic["b"])
    return total

if __name__ == "__main__":
    input_file = "input_day2.txt"  # Change this to your input file name
    
    try:
        input_data = Path(input_file).read_text().strip()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        exit(1)

    parsed_data = parse_input(input_data)

    start_time = time.perf_counter()

    print("Part One Result:", part_one(parsed_data))
    print("Part Two Result:", part_two(parsed_data))

    end_time = time.perf_counter()
    print(f"Time taken: {end_time - start_time:.6f} seconds")