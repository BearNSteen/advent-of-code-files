import time
from pathlib import Path

p = 0

def check_columns(lines, start, stop, do=1):
    # checks if there is a pattern that a vertical line can separate
    global p

    s = stop - start

    if stop==start:
        return False
    
    if p == 0:
        not_found = 0

        if (stop - start) % 2 != 1:
            not_found = 1

        else:
           # print("COLS: " + str(start) + ", " + str(stop))
            midl = (stop - start) // 2 + start
            midr = midl+1

            for x in range(len(lines)):
                
                left = lines[x][start:midr]
                right = lines[x][midr:stop+1]
                right.reverse()

                        #print((start, stop), left, right)

                if len(left) == 0 or len(right) == 0:
                    return False
                
                #print((start, stop), left, right)

                if left != right:
                    not_found = 1
                    break
                else:
                    pass
                    

        if not_found == 1:
            
            x = check_columns(lines, start+1, stop, 0)
            y = check_columns(lines, start, stop-1, 0)
            if x != False: return x
            if y != False: return y

        else:
            midl += 1
            #print("Found at line " + str(midl))
            p = midl
            return s
    
    return False

def check_rows(lines, start, stop):
    # checks if there is a pattern that a horizontal line can separate
    global p

    s = stop - start

    if s == 0:
        return False
    
    if p == 0:
        not_found = 0

        if (stop - start) % 2 != 1:
            not_found = 1

        else:
           # print("ROWS: " + str(start) + ", " + str(stop))
            midl = (stop - start) // 2 + start
            midr = midl+1

            for x in range(len(lines[0])):
                # lines [row] [col]
                left = []
                for val in range(start, midr):
                    left.append(lines[val][x])
                
                right = []
                for val in range(midr, stop+1):
                    right.append(lines[val][x])

                right.reverse()

                if len(left) == 0 or len(right) == 0:
                    return False

                #print((start, stop), left, right)

                if left != right:
                    not_found = 1
                    break
                else:
                    pass
                    #

        if not_found == 1:
            
            x = check_rows(lines, start+1, stop)
            y = check_rows(lines, start, stop-1)
            if x != False: return x
            if y != False: return y

        else:
            midl += 1
            #print("Found at line " + str(midl))
            p = midl
            return s
    
    return False

def part_one(input):
    lines = input.splitlines()
    global p
    groups = []
    temp = []
    for line in lines:
        if line == "":
            groups.append(temp)
            temp = []
        else:
            temp.append(list(line))

    total = 0
    for group in groups:
        p = 0
        xx, yy = 0, 0
        # return the left number of the line
        #print("COLUMNS")
        y = check_columns(group, 0, len(group[0])-1)

        if p != 0:
            yy = p
        p=0

        #print("ROWS")
        x = check_rows(group, 0, len(group)-1)

        if p != 0:
            xx = p
        p=0

        #print(y, yy, x, xx)

        if y >= x:
            #print("Added y")
            total += yy
        else:
            #print("Added x")
            total += xx*100
        
    print("P1 Answer: " + str(total))
    # 22754 too low
    if total == 29130:
        print("Correct!")
    else:
        print("Incorrect!")


def part_two(input):
    pass

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day13.txt").read_text()
    # part 1
    part_one(input)
    # part 2
    part_two(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")