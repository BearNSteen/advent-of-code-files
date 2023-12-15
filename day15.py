import time
from pathlib import Path

def part_one(input):
    lines = input.split(',')
    total = 0
    for string in lines:
        cv = 0
        for item in string:
            a = ord(item)
            cv += a
            cv = cv*17
            cv = cv%256
        total += cv

    print("P1A: " + str(total))

def hash_alg(string):
    cv = 0
    for item in string:
        a = ord(item)
        cv += a
        cv = cv*17
        cv = cv%256
    return cv

def part_two(input):
    boxes = [[] for _ in range(256)]
    lines = input.split(',')
    total = 0
    labels = []
    hashmap = {}
    for string in lines:
        # label can be more than 2 characters in actual data
        spl = string.split('=')
        spl2 = string.split('-')
        if len(spl) > len(spl2):
            label = spl[0]
            operation = "="
            num = int(spl[1])
        else:
            label = spl2[0]
            operation = "-"
        if operation == "=":
            box = hash_alg(label)
            if len(boxes[box]) == 0:
                hashmap[label] = num
                boxes[box].append(label)
                labels.append(label)
            else:
                hashmap[label] = num
                if label not in labels:
                    boxes[box].append(label)
                    labels.append(label)
        else:
            if label in labels:
                for box in range(len(boxes)):
                    if label in boxes[box]:
                        boxes[box].remove(label)
                        labels.remove(label)
                        del hashmap[label]

    #print("HASHMAP: " + str(hashmap))
    #print("LABELS: " + str(labels))
    print("BOXES: " + str(boxes))

    for label in labels:
        for box in range(len(boxes)):
            if label in boxes[box]:
                for l in range(len(boxes[box])):
                    if boxes[box][l] == label:
                        print((1+box), l+1, hashmap[label])
                        total += ((1+box) * (l+1) * hashmap[label])
                        #print(total)
                break

    print("P2A: " + str(total))
    # 24878 too low

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day15.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")