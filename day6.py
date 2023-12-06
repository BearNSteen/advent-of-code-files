import time

def find_best_boat_time(input):
    lines = input.splitlines()
    total_times = 0
    times = []
    distances = []
    timeline = lines[0].split()
    distanceline = lines[1].split()
    for value in timeline[1:]:
        times.append(int(value))
    for value in distanceline[1:]:
        distances.append(int(value))
    ends = []
    for x in range(len(times)):
        options = 0
        time = times[x]
        tot_dist = distances[x]
        for hold in range(time):
            to_go = time - hold
            speed = hold
            went = speed*to_go
            if went > tot_dist:
                total_times += 1
                options += 1
        ends.append(options)
    answer = ends[0]
    for value in ends[1:]:
        answer = answer*value
    print("PART 1 ANSWER: " + str(answer))

def find_best_boat_time_one_race(input):
    lines = input.splitlines()

    time_strings = []
    times_string = ""
    time = 0

    distances = []
    dist_string = ""
    tot_dist = 0

    timeline = lines[0].split()
    distanceline = lines[1].split()

    for value in timeline[1:]:
        time_strings.append(value)
    for s in time_strings:
        times_string += s
    time = int(times_string)

    for value in distanceline[1:]:
        distances.append(value)
    for s in distances:
        dist_string += s
    tot_dist = int(dist_string)

    options = 0
    for hold in range(time):
        went = hold * (time - hold)
        if went > tot_dist:
            options += 1

    print("PART 2 ANSWER: " + str(options))


if __name__ == "__main__":
    before = time.perf_counter()
    input = """Time:        46     68     98     66
    Distance:   358   1054   1807   1080"""
    # part 1
    find_best_boat_time(input)
    find_best_boat_time_one_race(input)
    print(f"Time: {time.perf_counter() - before:.6f} seconds")