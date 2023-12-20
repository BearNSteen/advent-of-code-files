import time
from pathlib import Path
from copy import deepcopy

def process_beam(routes, on, cnj):
    low = 0
    high = 0
    to_send = 1000
    prev = None 
    queue = []
    cnj_check = deepcopy(cnj)
    on_check = deepcopy(on)
    while to_send != 0:
        #print(to_send)
        queue.append(("broadcaster", "low", None))
        while len(queue) != 0:
            if to_send == 1000:
                print(queue)
            #print(queue)
            src = queue[0][0]
            a = routes[src]
            effect = a[0]
            targets = a[1]
            cbeam = queue[0][1]
            #print(src, effect, targets, cbeam)

            if effect == None:
                for target in targets:
                    low += 1
                    queue.append((target, "low", src))

            elif effect == "%" and cbeam == "low":
                if on[src] == "off":
                    on[src] = "on"
                    for target in targets:
                        high += 1
                        queue.append((target, "high", src))
                else:
                    on[src] = "off"
                    for target in targets:
                        low += 1
                        queue.append((target, "low", src))

            elif effect == "&":
                curr = cnj[src]
                curr[input] = cbeam
                send = "high"
                for key in curr.keys():
                    if curr[key] == "low":
                        send = "low"
                        break
                if send == "low":
                    low += 1
                else:
                    high += 1
                for target in targets:
                    queue.append((target, send, src))

            queue.remove(queue[0])
        to_send -= 1
        if on == on_check and cnj == cnj_check:
            cycle = 1000 - to_send
            until = 1000//cycle
            to_send = 1000 - cycle*until
            print("Cycle found of length " + str(cycle) + " setting to_send to value " + str(to_send))
    print(low, high)
    return low * high

                

def part_one(input):
    on = {}
    cnj = {}
    lines = input.splitlines()
    routes = {}
    for line in lines:
        spl = line.split(' -> ')
        src = spl[0]
        targets = spl[1].split(', ')
        if src != "broadcaster":
            routes[src[1:]] = (src[0], targets)
            if src[0] == "%":
                on[src[1:]] = "off"
            elif src[0] == "&":
                memory = {}
                for target in targets:
                    memory[target] = "low"
                cnj[src[1:]] = deepcopy(memory)
        else:
            routes["broadcaster"] = (None, targets)

    ans = process_beam(routes, on, cnj)

    print("P1A: " + str(ans))
    global sample
    if sample == 1:
        print("Sample answer: 32000000")

def part_two(input):
    pass

if __name__ == "__main__":
    before = time.perf_counter()
    global sample
    sample = 1
    if sample == 0:
        input = Path("input_day20.txt").read_text()
    else:
        input = Path("input_day20sample.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")