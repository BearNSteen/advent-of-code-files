import time
from pathlib import Path
import re

total = 0
m = []

def part_one(input):
    lines = input.splitlines()
    ins = {}
    groups = []
    mode = 1
    
    for x in range(len(lines)):
        if mode == 1:
            if lines[x] == "":
                mode = 2
            else:
                curr,spl = [], []
                temp = lines[x][0:len(lines[x])-1]
                temp = temp.split('{')
                for x in range(len(temp)):
                    temp2 = temp[x].split(',')
                    for item in temp2:
                        spl.append(item)
                name = spl[0]
                for item in range(1, len(spl)):
                    if len(spl[item]) > 3:
                        items = spl[item].split(":")
                        curr.append((items[0][0], items[0][1], int(items[0][2:]), items[1]))
                    else:
                        curr.append(spl[item])
                ins[name] = curr
        elif mode == 2:
            temp = lines[x][1:len(lines[x])-1]
            spl = temp.split(',')
            curr = {}
            for line in spl:
                spl2 = line.split('=')
                curr[spl2[0]] = int(spl2[1])
            groups.append(curr)

    total = 0
    for group in groups:
        curr = ins["in"]
        name = "in"
        state = None
        while state != "A" and state != "R":
            for instruction in curr:
                if not isinstance(instruction, str):
                    variable = instruction[0]
                    comparison = instruction[1]
                    num = instruction[2]
                    dest = instruction[3]
                    to_comp = group[variable]
                    if comparison == ">":
                        if to_comp > num:
                            if dest != "A" and dest != "R":
                                curr = ins[dest]
                                break
                            else:
                                state = dest
                                break
                    else:
                        if to_comp < num:
                            if dest != "A" and dest != "R":
                                curr = ins[dest]
                                break
                            else:
                                state = dest
                                break
                else:
                    if len(instruction) == 1:
                        state = instruction
                    else:
                        curr = ins[instruction]
                        name = instruction
                        break
        if state == "A":
            total += group["x"] + group["m"] + group["a"] + group["s"]
    
    print("P1A: " + str(total))

def pick_num(v, c, x1, x2, m1, m2, a1, a2, s1, s2):
    if v == "x":
        if c == "<":
            return "x2", x2
        else:
            return "x1", x1
    elif v == "m":
        if c == "<":
            return "m2", m2
        else:
            return "m1", m1
    elif v == "a":
        if c == "<":
            return "a2", a2
        else:
            return "a1", a1
    elif v == "s":
        if c == "<":
            return "s2", s2
        else:
            return "s1", s1

def add_to_total(x1, x2, m1, m2, a1, a2, s1, s2, nudge):
    global total
    print(nudge + "(" + str(x2 - x1+1) + "*" + str(m2-m1+1) + "*" + str(a2-a1+1) + "*" + str(s2-s1+1) + ") + " + str(total))
    total += (x2 - x1+1) * (m2 - m1+1) * (a2 - a1+1) * (s2 - s1+1)

def navigate(ins, step, x1, x2, m1, m2, a1, a2, s1, s2, nudge):
    global total
    global m
    state = None
    curr = ins[step]
    n_add = "   "
    nx1, nx2, nm1, nm2, na1, na2, ns1, ns2 = x1, x2, m1, m2, a1, a2, s1, s2
    print(nudge + str(step))
    while (state != "A" and state != "R"):
        s = [nx1, nx2, nm1, nm2, na1, na2, ns1, ns2]
        print(nudge + str(s))
        print(nudge + str(curr))
        for x in range(len(curr)):
            instruction = curr[x]
            if not isinstance(instruction, str):
                variable = instruction[0]
                comparison = instruction[1]
                num = instruction[2]
                dest = instruction[3]
                pick, to_comp = pick_num(variable, comparison, nx1, nx2, nm1, nm2, na1, na2, ns1, ns2)
                if comparison == ">":
                    if to_comp > num:
                        if dest != "A" and dest != "R":
                            print(nudge + "Jumping from " + step + " to " + dest)
                            navigate(ins, dest, nx1, nx2, nm1, nm2, na1, na2, ns1, ns2, nudge+n_add)
                        elif dest == "A":
                            n = (nx1, nx2, nm1, nm2, na1, na2, ns1, ns2)
                            if n not in m:
                                add_to_total(nx1, nx2, nm1, nm2, na1, na2, ns1, ns2, nudge)
                                m.append((nx1, nx2, nm1, nm2, na1, na2, ns1, ns2))
                    else:
                        if pick == "x1":
                            temp = nx1
                            nx1 = num + 1
                            ch, ch2 = nx1, nx2
                        elif pick == "m1":
                            temp = nm1
                            nm1 = num + 1
                            ch, ch2 = nm1, nm2
                        elif pick == "a1":
                            temp = na1
                            na1 = num + 1
                            ch, ch2 = na1, na2
                        elif pick == "s1":
                            temp = ns1
                            ns1 = num + 1
                            ch, ch2 = ns1, ns2
                        if ch < ch2:
                            if dest != "A" and dest != "R":
                                print(nudge + "Jumping from " + step + " to " + dest)
                                navigate(ins, dest, nx1, nx2, nm1, nm2, na1, na2, ns1, ns2, nudge+n_add)
                            elif dest == "A":
                                n = (nx1, nx2, nm1, nm2, na1, na2, ns1, ns2)
                                if n not in m:
                                    add_to_total(nx1, nx2, nm1, nm2, na1, na2, ns1, ns2, nudge)
                                    m.append((nx1, nx2, nm1, nm2, na1, na2, ns1, ns2))
                        if pick == "x1":
                            nx1 = temp
                            nx2 = num
                        elif pick == "m1":
                            nm1 = temp
                            nm2 = num
                        elif pick == "a1":
                            na1 = temp
                            na2 = num
                        elif pick == "s1":
                            ns1 = temp
                            ns2 = num

                            
                else:
                    if to_comp < num:
                        if dest != "A" and dest != "R":
                            print(nudge + "Jumping from " + step + " to " + dest)
                            navigate(ins, dest, nx1, nx2, nm1, nm2, na1, na2, ns1, ns2, nudge+n_add)
                        elif dest == "A":
                            n = (nx1, nx2, nm1, nm2, na1, na2, ns1, ns2)
                            if n not in m:
                                add_to_total(nx1, nx2, nm1, nm2, na1, na2, ns1, ns2, nudge)
                                m.append((nx1, nx2, nm1, nm2, na1, na2, ns1, ns2))
                    else:
                        # if num == 500:
                        # range1 == [0, 499]
                        # range2 == [500, 4000]

                        if pick == "x2": 
                            temp = nx2
                            nx2 = num - 1
                            ch, ch2 = nx1, nx2
                        elif pick == "m2":
                            temp = nm2
                            nm2 = num - 1
                            ch, ch2 = nm1, nm2
                        elif pick == "a2":
                            temp = na2
                            na2 = num - 1
                            ch, ch2 = na1, na2
                        elif pick == "s2":
                            temp = ns2
                            ns2 = num - 1
                            ch, ch2 = ns1, ns2

                        if ch < ch2:
                            if dest != "A" and dest != "R":
                                print(nudge + "Jumping from " + step + " to " + dest)
                                navigate(ins, dest, nx1, nx2, nm1, nm2, na1, na2, ns1, ns2, nudge+n_add)
                            elif dest == "A":
                                n = (nx1, nx2, nm1, nm2, na1, na2, ns1, ns2)
                                if n not in m:
                                    add_to_total(nx1, nx2, nm1, nm2, na1, na2, ns1, ns2, nudge)
                                    m.append((nx1, nx2, nm1, nm2, na1, na2, ns1, ns2))
                        if pick == "x2":
                            nx2 = temp
                            nx1 = num
                        elif pick == "m2":
                            nm2 = temp
                            nm1 = num
                        elif pick == "a2":
                            na2 = temp
                            na1 = num
                        elif pick == "s2":
                            ns2 = temp
                            ns1 = num

            else:
                if len(instruction) == 1:
                    if instruction == "A":
                        n = (nx1, nx2, nm1, nm2, na1, na2, ns1, ns2)
                        if n not in m:
                            add_to_total(nx1, nx2, nm1, nm2, na1, na2, ns1, ns2, nudge)
                            m.append((nx1, nx2, nm1, nm2, na1, na2, ns1, ns2))
                        return
                    else:
                        return
                else:
                    print(nudge + "Jumping from " + step + " to " + instruction)
                    navigate(ins, instruction, nx1, nx2, nm1, nm2, na1, na2, ns1, ns2, nudge+n_add)
                    return
        return

def part_two(input):
    lines = input.splitlines()
    ins = {}
    groups = []
    mode = 1
    global total
    
    # put only comparison routes, ignore xmas values
    for x in range(len(lines)):
        if mode == 1:
            if lines[x] == "":
                break
            else:
                curr,spl = [], []
                temp = lines[x][0:len(lines[x])-1]
                temp = temp.split('{')
                for x in range(len(temp)):
                    temp2 = temp[x].split(',')
                    for item in temp2:
                        spl.append(item)
                name = spl[0]
                for item in range(1, len(spl)):
                    if len(spl[item]) > 3:
                        items = spl[item].split(":")
                        curr.append((items[0][0], items[0][1], int(items[0][2:]), items[1]))
                    else:
                        curr.append(spl[item])
                ins[name] = curr

    ranges = {}
    x1, x2 = (1, 4000)
    m1, m2 = (1, 4000)
    a1, a2 = (1, 4000)
    s1, s2 = (1, 4000)

    nudge = ""
    
    step = "in"
    navigate(ins, step, x1, x2, m1, m2, a1, a2, s1, s2, nudge)

    sample = 0

    print("P2A: " + str(total))
    if sample == 1:
        print(total)
        print(167409079868000)
        if total == 167409079868000:
            print("Correct (sample)")
        elif total > 167409079868000:
            print("Too high (sample)")
        elif total < 167409079868000:
            print("Too low (sample)")
    else:
        ans = 127675188176682
        if total == ans:
            print("Correct")
        elif total > ans:
            print("Too high")
        elif total < ans:
            print("Too low")


if __name__ == "__main__":
    before = time.perf_counter()

    sample = 0

    if sample == 1:
        input = Path("input_day19sample.txt").read_text()
    else:
        input = Path("input_day19.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")