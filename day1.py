# Note: this day does not include the answer to part 1

input = "input"

split = input.splitlines()
total = 0

for line in split:
    print(line)
    first = None
    last = None
    l_l = len(line)
    nums = []
    for x in range(l_l):
        character = line[x]
        if str.isnumeric(character):
            nums.append(int(character))
        else:
            if x + 2 < l_l:
                # one two six
                check = line[x] + line[x+1] + line[x+2]
                if check == "one":
                    nums.append(1)
                if check == "two":
                    nums.append(2)
                if check == "six":
                    nums.append(6)
            if x + 3 < l_l:
                # four five nine
                check = line[x] + line[x+1] + line[x+2] + line[x+3]
                if check == "four":
                    nums.append(4)
                if check == "five":
                    nums.append(5)
                if check == "nine":
                    nums.append(9)
            if x + 4 < l_l:
                # three seven eight 
                check = line[x] + line[x+1] + line[x+2] + line[x+3] + line[x+4]
                if check == "three":
                    nums.append(3)
                if check == "seven":
                    nums.append(7)
                if check == "eight":
                    nums.append(8)

    first = nums[0]
    last = nums[-1]
    num = int(str(first) + str(last))
    print("nums: " + str(nums) + " | " + str(num) + " + " + str(total) + " = " + str(total+num))
    total = num + total

print(total)