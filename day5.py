import time

def find_lowest_location(input):
    lines = input.splitlines()
    spl = lines[0].split()
    seeds = []
    src = []
    dst = []
    for line in range(1, len(spl)):
        seeds.append(int(spl[line]))
    for line in lines:
        if line[0:5] == "seeds":
            pass
        elif line == "":
            if dst != [] and src != []:
                #print("DATA SPLIT ========================")
                for seed in range(len(seeds)):
                    dist = 0
                    for r in range(len(dst)):
                        #print(str(src[r][0]) + " < " + str(seeds[seed]) + " < " + str(src[r][1]))
                        if src[r][0] < seeds[seed] < src[r][1]:
                            dist = seeds[seed] - src[r][0]
                            stop = r
                            break
                    if dist != 0:
                        save = seeds[seed]
                        seeds[seed] = dst[r][0] + dist
                        #print(str(save) + " -> " + str(dst[r][0]+dist))

                dst = []
                src = []
        else:
            if line[0].isnumeric():
                # create current range
                spl = line.split()
                dst.append((int(spl[0]), int(spl[0]) + int(spl[2])))
                src.append((int(spl[1]), int(spl[1]) + int(spl[2])))
    #print("PART 1 ANSWER")
    #print(min(seeds))

def find_lowest_among_seed_ranges(input):
    lines = input.splitlines()
    spl = lines[0].split()
    rng = []
    seeds = []
    src = []
    dst = []
    current = ""

    for line in range(1, len(spl)-1, 2):
        rng.append((int(spl[line]), int(spl[line]) + int(spl[line+1])))

    seeds = rng

    for line in lines:
        to_add = []
        if line[0:5] == "seeds":
            pass
        elif line == "":
            if dst != [] and src != []:
                #print("Current Section: " + current + " | ========================")

                x = 0
                while x < len(seeds):
                    seed_s = seeds[x][0]
                    seed_e = seeds[x][1]
                    c = False

                    for t in range(len(src)):
                        if c == True:
                            #print("Converted (" + str(seed_s) + ", " + str(seed_e) + ") to " + str(seeds[x]) + ".")
                            break
                        src_s = src[t][0]
                        src_e = src[t][1]
                        dst_s = dst[t][0]
                        dst_e = dst[t][1]
                        
                        # if both seed endpoints are within src range
                        if src_s <= seed_s <= seed_e <= src_e:
                            seeds[x] = ((seed_s - src_s + dst_s), 
                                            (seed_e - src_s + dst_s))
                            c = True

                        # if seed start in source range
                        elif src_s <= seed_s <= src_e:                            

                            # if seed end NOT in source range
                            new = (src_e+1, seed_e)
                            to_add.append(new)

                            seeds[x] = ((seed_s - src_s + dst_s),
                                            (src_e - src_s + dst_s))
                            c = True                                
                        
                        # if seed end in source range, but seed start is NOT in source range
                        elif src_s <= seed_e <= src_e:

                            new = (seed_s, src_s-1)
                            to_add.append(new)

                            seeds[x] = ((dst_s),
                                            (seed_e - src_s + dst_s))
                            c = True
                            
                        # if source range is between seed start and end
                        elif seed_s < src_s <= src_e < seed_e:

                            to_add.append(
                                (seed_s, src_s)
                            )
                            to_add.append(
                                (src_e+1, seed_e)
                            )
                            seeds[x] = (
                                (dst_s),
                                (dst_e)
                            )
                            c = True
                    
                    if to_add != []:
                        for pair in to_add:
                            seeds.append(pair)
                    #print("Size: " + str(size) + " | Length of Seeds: " + str(len(seeds)))
                    #print(seeds)
                    to_add = []
                    x+= 1
                dst = []
                src = []

                #print(to_add)

        else:
            if line[0].isnumeric():
                # create current range
                spl = line.split()
                # add the ranges in tuples to dst/src (start, stop)
                dst.append((int(spl[0]), int(spl[0]) + int(spl[2])-1))
                src.append((int(spl[1]), int(spl[1]) + int(spl[2])-1))
            else:
                words = line.split()
                current = words[0]

    # separate out the starts and then find the lowest one
    alist = []
    for seed in seeds:
        alist.append(seed[0])
    #print("PART 2 ANSWER: " + str(min(alist)))

    answer = 24261545
    if min(alist) != answer:
        #print(str(answer)+" != "+str(min(alist))+"! WRONG ANSWER!")
        if answer in alist:
            #print("The answer list contains the correct answer, but it was not the minimum value!")
            pass
    else:
        pass
        #print(str(answer)+" == "+str(min(alist))+"! CORRECT ANSWER!")
    

if __name__ == "__main__":
    input = "input"
    before = time.perf_counter()
    # part 1
    find_lowest_location(input)
    # part 2 - would work with a supercomputer but the processing time just kills it
    find_lowest_among_seed_ranges(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")