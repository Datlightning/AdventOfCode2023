scalar_rows = set()
scalar_cols = set()
def display(grid):
    for line in grid:
        print(line)
def calculate_taxicab(point1, point2, scalar):
    y1, x1 = point1
    y2, x2 = point2
    xrange = range(min(x1, x2), max(x1,x2))
    yrange = range(min(y1, y2), max(y1,y2))
    xdist = 0
    ydist = 0
    for x in xrange:
        if x in scalar_cols:
            xdist += scalar
        else:
            xdist += 1
    for y in yrange:
        if y in scalar_rows:
            ydist += scalar
        else:
            ydist += 1
    return xdist + ydist
def solve():
    lines =  []
    with open("day11/day11.txt", "r") as file:
        lines = file.read().strip().split("\n")
    
    empty_columns = {

    }

    distances = {}
    all_points = set()
    for index, line in enumerate(lines):
        if not "#" in line:
            scalar_rows.add(index)
        for i, r in enumerate(line):
            if i in empty_columns:
                empty_columns[i] += 0 if r == "." else 1
            else:
                empty_columns[i] = 0 if r == "." else 1
            if empty_columns[i] == 0:
                scalar_cols.add(i)
            else:
                try:
                    scalar_cols.remove(i)
                except:
                    pass
            if r == "#":
                all_points.add((index,i))
                distances[(index,i)] = -1

    part1 = 0
    part2 = 0
    for point1 in all_points:
        for point2 in all_points:
           
            current_distance = calculate_taxicab(point1, point2, 2)
            part1 += current_distance
            current_distance = calculate_taxicab(point1, point2, 1000000)
            part2 += current_distance
           
    part1 //= 2
    part2 //= 2
   

    return f"Part 1: {int(part1)}\nPart 2: {int(part2)}"
print(solve())