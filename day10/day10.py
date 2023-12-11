import math
directions = {
    "|":((-1,0),(1,0)),
    "-":((0,-1),(0,1)),
    "L":((-1,0), (0,1)),
    "J":((-1,0), (0,-1)),
    "7":((1,0),(0,-1)),
    "F":((1,0), (0,1)),
    ".":()
}
reversed_directions = {v: k for k, v in directions.items()}
visited = set()
 
def is_bounds(point, grid):
    y,x = point
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0])
def convert_start(position, grid):
    y,x = position
    targets = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    correct = []
    for i, target in enumerate(targets):
        if is_bounds(target, grid):
            if position in expand(target, grid):
                correct.append(targets[i])
    for i, position in enumerate(correct):
        dy, dx = position
        correct[i] = (dy-y, dx-x)
    try:
        return reversed_directions[tuple(correct)]
    except KeyError:
        return reversed_directions[(correct[1], correct[0])]
def expand(position, grid):
    output = set()
    y,x = position
    value = grid[y][x]
    expansion = directions[value]
    for value in expansion:
        dy, dx = value
        position = (y+dy, x+dx)
        if is_bounds(position, grid):
            output.add(position)
    return output
def expand_for_pockets(position, grid):
    potential_output =set()
    y,x = position
    value = grid[y][x]
    potential_output.add((y+1, x))
    potential_output.add((y-1, x))
    potential_output.add((y, x-1))
    potential_output.add((y, x+1))
    output = set()
    for value in potential_output:
        ny, nx = value
        if is_bounds(value, grid) and not grid[ny][nx] in visited and grid[ny][nx] == ".":
            output.add(value)
    return output      
def border_tile(pos, grid):
    y,x = pos
    return x == 0 or y == 0 or y == len(grid) - 1 or x == len(grid[0]) -1
def get_points_between_pipes(grid):
    output =set()
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == ".":
                continue
            potential_points = directions[col]
            
            for point in potential_points:
                temp_point = (point[0] * -1, point[1] * -1)
                if is_bounds(temp_point, grid):
                    output.add(temp_point)     
            output.add((y,x))
          
    return output
def expand_regardless(point):
    y,x  = point
    output = {(y+1,x),(y-1,x),(y,x+1),(y,x-1)}
    return output 
def linked_pockets(pocket1, pocket2, open_grid):
    temp1 = set()
    for point in pocket1:
        temp1.update(expand_regardless(point))
    if len(temp1.intersection(open_grid)) == 0:
        return False
    temp2 = set()
    for point in pocket2:
        temp2.update(expand_regardless(point))    
    if len(temp2.intersection(open_grid)) == 0:
        return False
    temp2.intersection_update(open_grid)
    temp1.intersection_update(open_grid)
    visited = set()
    visited.update(temp2)
    visited.update(temp1)
    while True:
        temp3 = set()
        temp4 = set()
        for p in temp1:
            temp3.update(expand_regardless(p).intersection(open_grid).difference(visited))
        for p in temp2:
            temp4.update(expand_regardless(p).intersection(open_grid).difference(visited))
        if len(temp3.intersection(temp4)) > 0:
            return True
        if len(temp3) == 0 or len(temp4) == 0:
            return False
        temp1.clear()
        temp1.update(temp3)
        temp2.clear()
        temp2.update(temp4)
def display(pocket, grid):
    for y ,line in enumerate(grid):
        string = ""
        for x, value in enumerate(grid[y]):
            if (y,x) in pocket:
                string += "0"
            else:
                string += "."
        print(string)       
def solve():
    lines =  []
    grid = []
    pockets = []
    pocket_visited =set()
    with open("day10/day10.txt", "r") as file:
        lines = file.read().strip().split("\n")
    for line in lines:
        grid.append(list(line))
    
    start = False
    length = 0
    positions = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "S" and not start:
                start = True
                grid[y][x] = convert_start((y,x), grid)
                positions = [(y,x)]
                visited.add((y,x))
                while positions != []:
                    targets = set()
                    for position in positions:
                        targets.update(expand(position, grid))
                    targets.difference_update(visited)
                    visited.update(targets)
                    positions = list(targets)
                    length += 1
                    if len(positions) == 1:
                        break
                break
    for y, row in enumerate(grid):
        for x, col in enumerate(row):    
            if not (y,x) in visited:
                grid[y][x] = "."
    open_grid = get_points_between_pipes(grid)
    
    part2 = 0
    outside = set()
    
    for r, row in enumerate(grid):
        allowed = False
        going_left = None
        for c,value in enumerate(row):
            if value == "|":
                allowed = not allowed
            elif value in "LF":
                going_left = value == "L"
            elif value in "7J":
                if value == ("J" if not going_left else "7"): #this is saying that if we are going to the right and we see a "J" we will have to cross it. 
                    allowed = not allowed
                going_left = None
            elif value == ".":
                pass
            if not allowed:
                outside.add((r,c))
    part2 = len(grid) * len(grid[1]) - len(outside.union(visited))
    part1 = length
    
    return f"Part 1: {int(part1)}\nPart 2: {part2}"
   

        
        
   

print(solve())