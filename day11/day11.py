
def display(grid):
    for line in grid:
        print(line)
def calculate_taxicab(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)
def solve():
    lines =  []
    with open("day11/day11.txt", "r") as file:
        lines = file.read().strip().split("\n")
    grid = []
    
    empty_columns = {

    }
    order = []
    distances = {}
    all_points = set()
    for index, line in enumerate(lines):
        for i, r in enumerate(line):
            if i in empty_columns:
                empty_columns[i] += 0 if r == "." else 1
            else:
                empty_columns[i] = 0 if r == "." else 1
                order = [i] + order 
    superstring = ""
    for i in range(1000000):
        superstring += "."
    for item in order:
        value = empty_columns[item]
        if value == 0:
            for index, line in enumerate(lines):

                lines[index] = line[0:item] +  superstring + line[item:]
    for index, line in enumerate(lines):
        grid.append(line)
        if not "#" in line:
            for i in range(1000000):
                grid.append(line)
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "#":
                all_points.add((y,x))
                distances[(y,x)] = -1
    part1 = 0
    for point1 in all_points:
        for point2 in all_points:
           
            current_distance = calculate_taxicab(point1, point2)
            part1 += current_distance
            # if distances[point1] == -1:
            #     distances[point1] = current_distance
            # else:
            #     distances[point1] = min(current_distance, distances[point1])
    part1 //= 2
    print(part1)

    part1 = 0
    part2 = 0
    # display(grid)
        
    return f"Part 1: {int(part1)}\nPart 2: {int(part2)}"
solve()