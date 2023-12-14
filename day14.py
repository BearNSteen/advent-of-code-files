import time
from pathlib import Path
from copy import deepcopy

def part_one(input):
    lines = input.splitlines()
    mountain = []
    for line in lines:
        mountain.append(list(line))

    total = 0
    for x in range(len(mountain)):
        for y in range(len(mountain[x])):
            pos = x
            take = 0
            if mountain[x][y] == "O":
                while pos != -2 and pos-1 >= 0:
                    if mountain[pos-1][y] != ".":
                        take = pos
                        pos = -2
                    else:
                        mountain[pos-1][y] = "O"
                        mountain[pos][y] = "."
                        pos = pos-1
                total += len(mountain[x])-1 - take + 1
    
    if total == 108759:
        state = "Correct"
    else:
        state = "Incorrect"
    print("P1 Output: " + str(total) + " (" + state + ")")   

def tilt_north(mountain2):
    mountain = mountain2.copy()
    for x in range(len(mountain)):
        for y in range(len(mountain[x])):
            pos = x
            take = 0
            if mountain[x][y] == "O":
                while pos != -2 and pos-1 >= 0:
                    if mountain[pos-1][y] != ".":
                        take = pos
                        pos = -2
                    else:
                        mountain[pos-1][y] = "O"
                        mountain[pos][y] = "."
                        pos = pos-1
#                 total += len(mountain[x])-1 - take + 1
    return mountain

def tilt_south(mountain2):
    mountain = mountain2.copy()
    for x in range(len(mountain)-1, -1, -1):
        for y in range(len(mountain[x])):
            pos = x
            if mountain[x][y] == "O":
                while pos != -2 and pos+1 < len(mountain):
                    if mountain[pos+1][y] != ".":
                        pos = -2
                    else:
                        mountain[pos+1][y] = "O"
                        mountain[pos][y] = "."
                        pos = pos+1
    return mountain

def tilt_left(mountain2):
    mountain = mountain2.copy()
    for x in range(len(mountain)):
        for y in range(len(mountain[x])):
            pos = y
            if mountain[x][y] == "O":
                while pos != -2 and pos-1 >= 0:
                    if mountain[x][pos-1] != ".":
                        pos = -2
                    else:
                        mountain[x][pos-1] = "O"
                        mountain[x][pos] = "."
                        pos = pos-1
    return mountain

def tilt_right(mountain2):
    mountain = mountain2.copy()
    for x in range(len(mountain)):
        for y in range(len(mountain[x])-1, -1, -1):
            pos = y
            if mountain[x][y] == "O":
                while pos != -2 and pos+1 < len(mountain[x]):
                    if mountain[x][pos+1] != ".":
                        pos = -2
                    else:
                        mountain[x][pos+1] = "O"
                        mountain[x][pos] = "."
                        pos = pos+1
    return mountain

def mountain_in_arrangements(arrangements, mountain, curr_loop):
    if mountain in arrangements:
        #copies = []
        #for x in range(len(arrangements)):
        #    if arrangements[x] == mountain:
        #        copies.append(x)
        #copies.append(curr_loop)
        #print(copies)
        return (arrangements.index(mountain), curr_loop, deepcopy(mountain))
    return False

def tilt(mountain2, tilts, need_a):
    arrangements = [[]]
    a = []
    mountain = deepcopy(mountain2)
    for x in range(1, tilts):
        mountain = tilt_north(mountain)
        mountain = tilt_left(mountain)
        mountain = tilt_south(mountain)
        mountain = tilt_right(mountain)
        if need_a == True:
            a = mountain_in_arrangements(arrangements, mountain, x)
            if not a:
                mtn = deepcopy(mountain)
                arrangements.append(mtn)
            else:
                #mtn = deepcopy(mountain)
                #arrangements.append(mtn)
                return a
    if need_a == False:
        return mountain          
                    
def part_two(input):
    lines = input.splitlines()
    mountain = []
    for line in lines:
        mountain.append(list(line))
    arrangements = []

    loops = []
    total = 0
    
    a = tilt(mountain, 10000, True)
    
    if a:
        print("Loop found")
        print(a[0], a[1])

    else:
        print("Error. Loop not found.")
        return
    
    # the number of spin cycles
    num = 1000000000
    # the length of the cycle
    loop_length = a[1] - a[0]
    # the number of times the loop length goes into the amount of space between the end of the spin cycle and the start of the loop
    div = (num-a[0]) // loop_length 
    # the number of times the loop cycles before hitting num
    closer = div * loop_length
    # how many more spin cycles are needed to hit num
    additional_spins_needed = num - (a[0] + closer)+1

    print(additional_spins_needed)
    
    total = 0
    # run the spin cycle the number of times required left
    final = tilt(a[2], additional_spins_needed, False)
    # calculate the north support value
    for x in range(len(final)):
        for y in range(len(final[x])):
            if final[x][y] == "O":
                #print("("+str(x) + ", " + str(y) + ") value: " + str(len(final)-x))
                total += len(final) - x
    print(total)

    if total == 64:
        state = "Correct"
    else:
        state = "Incorrect"
    print("P2 Output: " + str(total) + " (" + state + ") (Answer: 64)")

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day14.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")