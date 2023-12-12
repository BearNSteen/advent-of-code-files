import time
from pathlib import Path

routes = []

def p(a, b, n):
    a.append((b, n))
    return a

def print_p(path):
    print(path)


def check_recursive(lst, nums, path):
    npath = path.copy()
    new = lst.copy()

    if len(nums) != 0:
        if nums[0] > len(lst):
            return
    if len(nums) == 0 and '#' in lst:
        return
    elif len(lst) == 0:
        if len(nums) == 0 and len(lst) == 0:
            #print(npath, nums)
            if npath not in routes:
                routes.append(npath)
            return
        else:
            return
    elif lst[0] == ".":
        npath.append(new[0])
        new.remove(new[0])
        check_recursive(new, nums, npath)
    elif lst[0] == "#":
        l = nums[0]
        fail = 0
        nums2 = nums.copy()
        if l-1 < len(new):
            for x in range(1, l):
                if lst[x] == ".":
                    fail = 1
        else:
            fail = 1
        if fail == 0:
            if l < len(lst):
                if lst[l] != "#":
                    for x in range(0, l):
                        npath.append("#")
                        new.remove(new[0])
                    nums2.remove(nums2[0])
                    if len(new) > 0:
                        new[0] = "."
                else:
                    springs = 0
                    for item in new:
                        if item == "#":
                            springs += 1
                    if springs > sum(nums):
                        return
                    npath.append(".")
                    new.remove(new[0])
            else:
                for x in range(0, l):
                    npath.append("#")
                    new.remove(new[0])
                nums2.remove(nums2[0])
                if len(new) > 0:
                    new[0] = "."
        else:
            npath.append(".")
            new.remove(new[0])
        check_recursive(new, nums2, npath)
    elif lst[0] == "?":
        new[0] = "."
        check_recursive(new, nums, npath)
        new[0] = "#"
        check_recursive(new, nums, npath)
    return routes
            

def part_one(input):
    lines = input.splitlines()
    total = 0
    which = 1
    for line in lines:
        global routes
        routes = []
        spl = line.split()
        nums = []
        s = spl[1].split(",")
        for num in s: 
            nums.append(int(num))
        lst = list(spl[0])
        #print("=================")
        #print(lst, nums)
        #print("=================")

        path = []
        routes = check_recursive(lst, nums, path)
        result = len(routes)
        """
        print("=================")
        print(result, line)
        print(lst)
        for route in routes:
            print(route)
        print("=================")
        """
        
        total += result
        print(total)
        which += 1
    
    print("P1: " + str(total))
    if total == 7939:
        print("P1 Correct!")
    else:
        print("P1 Incorrect!")

def part_two(input):
    pass

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day12.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")