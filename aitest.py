import time
from pathlib import Path

# note: this assessment answer passed the assessment

def decode(file):
    input = Path(file).read_text()
    lines = input.splitlines()
    hashmap = {}
    all_nums = []

    for entry in lines:
        spl = entry.split(' ')
        hashmap[spl[0]] = spl[1]
        all_nums.append(int(spl[0]))
    
    all_nums.sort()
    skip, skip_val = 0, 0
    word_nums = []
    for x in range(len(all_nums)):
        if skip == 0:
            word_nums.append(all_nums[x])
            skip_val += 1
            skip = skip_val
        else:
            skip -= 1

    sentence = ""
    for val in word_nums:
        v = str(val)
        if sentence == "":
            sentence += hashmap[v]
        else:
            sentence += " " + hashmap[v]

    return sentence
    

if __name__ == "__main__":
    before = time.perf_counter()
    # part 1
    print(decode("coding_qual_input.txt"))
    print(f"Time: {time.perf_counter() - before:.6f} seconds")