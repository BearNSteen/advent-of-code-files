input = "input"

# possible with 12 red, 13 green, 14 blue
# part 1 solution

total = 0
split = input.splitlines()
lines = []
for line in split:
    skip = False
    dic = {"r":12, "g":13, "b":14}
    elim = False
    split_list = line.split()
    for x in range(2, len(split_list), 2):
        num = int(split_list[x])
        color = split_list[x+1]
        if dic[color[0]] < num:
            skip = True
    if skip == False:
        total += int(split_list[1][:-1])

#print(total)

# part 2 solution

total = 0
split = input.splitlines()
lines = []
for line in split:
    dic = {"r":0, "g":0, "b":0}
    split_list = line.split()
    for x in range(2, len(split_list), 2):
        num = int(split_list[x])
        color = split_list[x+1]
        if dic[color[0]] < num:
            dic[color[0]] = num
    print(dic)
    total += (dic["r"] * dic["g"] * dic["b"])

print(total)