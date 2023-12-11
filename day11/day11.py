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
    for r, row in enumerate(lines):
        empty_row = True
        for c, col in enumerate(row):
            if c in empty_columns:
                empty_columns[c] += 0 if col == "." else 1
            else:
                empty_columns[c] = 0 if col == "." else 1
            if empty_columns[c] == 0:
                scalar_cols.add(c)
            else:
                try:
                    scalar_cols.remove(c)
                except:
                    pass
            if col == "#":
                all_points.add((r,c))
                distances[(r,c)] = -1
                empty_row = False
        if empty_row:
            scalar_rows.add(r)
    part1 = 0
    part2 = 0
    evaluated_pairs = set()
    for point1 in all_points:
        for point2 in all_points:
            if (point1, point2) not in evaluated_pairs:
                current_distance = calculate_taxicab(point1, point2, 2)
                part1 += current_distance
                current_distance = calculate_taxicab(point1, point2, 1000000)
                part2 += current_distance
                evaluated_pairs.add((point1, point2))
                evaluated_pairs.add((point2, point1))
    return f"Part 1: {int(part1)}\nPart 2: {int(part2)}"
