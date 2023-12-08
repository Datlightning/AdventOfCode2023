import math
def solve():
    lines=  []
    order_map = dict()
    with open("day8/day8.txt", "r") as file:
        lines = file.read().strip().split("\n\n")
    directions = list(lines[0])
    all_as = []
    for line in lines[1].split("\n"):
        line_list = line.split("=")
        start = line_list[0].strip()
        if start[2] == "A":
            all_as.append(start)
        end = line_list[1].strip().split(",")
        order_map[start] = (end[0][1:].strip(), end[1][:-1].strip())
    lengths = {}
    all_steps = []
    max_index = len(directions)

    for i, position in enumerate(all_as):
        initial_pos = position
        steps = 0
        index = 0
        while all_as[i][2] != "Z":
            if directions[index] == "R":
                all_as[i] = order_map[all_as[i]][1]
            else:
                all_as[i] = order_map[all_as[i]][0]
            steps += 1
            index += 1
            if index == max_index:
                index = 0
        lengths[initial_pos] = steps
        all_steps.append(steps)

    print(math.lcm(*all_steps))
solve()