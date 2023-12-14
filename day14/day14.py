from copy import deepcopy
def slide(direction, grid):
    dy, dx = direction
    height = len(grid)
    width = len(grid[0])    
    if dy == -1:
        for c in range(width):
            for _ in range(height):
                for r in range(height):
                    if grid[r][c] == "O" and r>0 and grid[r-1][c] == ".":
                        grid[r-1][c] = "O"
                        grid[r][c] = "."
    elif dy == 1:
        for c in range(width):
            for _ in reversed(range(height)):
                for r in reversed(range(height)):
                    if grid[r][c] == "O" and r<height-1 and grid[r+1][c] == ".":
                        grid[r+1][c] = "O"
                        grid[r][c] = "."
    elif dx == -1:
        for r in range(height):
            for _ in range(width):
                for c in range(width):
                    if grid[r][c] == "O" and c>0 and grid[r][c-1] == ".":
                        grid[r][c-1] = "O"
                        grid[r][c] = "."
    elif dx == 1:
        for r in range(height):
            for _ in reversed(range(width)):
                for c in reversed(range(width)):
                    if grid[r][c] == "O" and c<width-1 and grid[r][c+1] == ".":
                        grid[r][c+1] = "O"
                        grid[r][c] = "."
    return grid
def calculate_score(v):
    score = 0
    height = len(v)
    for r, row in enumerate(v):
        for col in row:
            if col == "O":
                score += height - r 
    return score

def is_bounds(point, y, x):
    y1, x1 = point
    return 0<=y1<y and 0<=x1<x
def display(grid):
    for r in grid:
        string = ""
        for c in r:
            string += c
        print(string)
def tostring(grid):
    output = ""
    for r in grid:
        for c in r:
            output += c
    return output
def solve():
    lines = []
    parts = [-1,0]
    with open("day14/day14.txt", "r") as file:
        lines = file.read().strip().split("\n")
    grid = []
    for r, line in enumerate(lines):
        grid.append([])
        for c, rock in enumerate(line):
            grid[r].append(rock)
            
    height = r+1
  
    rock_history = dict()
    cycle_history = dict()
    iter = 0
    while True:
        iter += 1
        for direction in [[-1,0],[0,-1],[1,0],[0,1]]:
            grid = slide(direction, grid)
            if parts[0] == -1:
                parts[0] = calculate_score(grid)
    
        key = tostring(grid)
        if key in rock_history:
            break
        else:
            rock_history[key] = iter
            cycle_history[iter] = deepcopy(grid)
    cycle_length = iter - rock_history[key]
    target = ((1000000000 - rock_history[key]) % cycle_length) + rock_history[key]

    parts[1] = (calculate_score(cycle_history[target]))
    part1 = parts[0]
    part2 = parts[1]
    print(f"Part 1: {int(part1)}\nPart 2: {int(part2)}")
    return 
if __name__ == '__main__':
    solve()
