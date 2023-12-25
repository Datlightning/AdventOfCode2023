#Reverse djkstra works when there are no loops

from heapq import heappop, heappush


h = 0
w = 0
slopes = {
    ">":(0,1),
    "<":(0,-1),
    "^":(-1,0),
    "v":(1,0)
}

def move(start, grid, part2):
    length,y,x,dy,dx = start
    output = []
    for ny,nx in [(1,0),(0,1),(-1,0),(0,-1)]:
        if (dy,dx) != (-ny, -nx):
            newpoint = (length - (1 if part2 else 1), y+ny, x+nx, ny, nx)
            if not is_bounds(newpoint):
                continue
            ty = y + ny
            tx = x + nx
            if (ty,tx) == (dy,dx):
                if grid[ty][tx] in slopes:
                    if (ny,nx) == slopes[grid[ty][tx]] or part2:
                        output.append(newpoint)
                elif grid[ty][tx] != "#":
                    output.append(newpoint)
                    
            elif grid[ty][tx] != "#":
                if grid[ty][tx] in slopes:
                    if (ny,nx) == slopes[grid[ty][tx]] or part2:
                        output.append(newpoint)
                else:
                    output.append(newpoint)
    return output
def is_bounds(point):
    _,y,x,_,_ = point
    return 0<=y<h and 0<=x<w
def solve():
    global w,h
    part1 = 0 
    part2 = 0
    grid = []
    visual_grid = []
    visual_grid_part2 = []
    #y,x,dy,dx
    start = (0,0,0,0,0)
    end = (0,0)
    with open("day23/day23.txt", "r") as file:  
        data = file.read().strip().split("\n")
        length= len(data)
        for index, line in enumerate(data, start = 0):
            grid.append([])
            visual_grid.append([])
            visual_grid_part2.append([])
            for c, value in enumerate(line):
                visual_grid[index].append(100)
                visual_grid_part2[index].append(100)
                grid[index].append(value)
                if index == 0 and value == ".":
                    start = (0,index, c, 1, 0)
                if index == length - 1 and value == ".":
                    end = (index,c)
                    # print(end)
        # print(index)
    h = length
    w = len(grid[0])
    visited = {(0,0)}
    queue = [start]
    while queue:
        point = heappop(queue)
        distance,y,x,dy,dx = point
        if (y,x, -dy, -dx) in visited:
            continue
        visual_grid[y][x] = min(distance, visual_grid[y][x])
            

        next_moves = move(point, grid, part2 = False)
        for p in next_moves:
            heappush(queue, p)
        visited.add((y,x, dy ,dx))

    y,x = end
    part1 = -visual_grid[y][x]
    print(part1)
                                      

    #114542 is too high
    return f"Part 1: {part1}\nPart 2: {part2}"

if __name__ == "__main__":
    print(solve())