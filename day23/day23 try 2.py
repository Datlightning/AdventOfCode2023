from collections import deque
from heapq import heappop, heappush



h = 0
w = 0
slopes = {
    ">":[(0,1)],
    "<":[(0,-1)],
    "^":[(-1,0)],
    "v":[(1,0)],
    ".":[(1,0),(0,1),(-1,0),(0,-1)],
    "#":[]
}

def move(start, grid, part2):
    y,x = start
    output = []
    position = slopes["."] if part2 else slopes[grid[y][x]]
    for ny,nx in position:
            ty = y + ny
            tx = x + nx
            if is_bounds((ty,tx)) and grid[ty][tx] != "#":
                output.append((ty,tx))
    return output
def is_bounds(point):
    y,x = point
    return 0<=y<h and 0<=x<w
visited =  set()
end = (0,0)
def calculate_distances(point, grid):
    if point == end:
        return 0
    m = -float('inf')
    visited.add(point)
    for p in grid[point]:
        if p not in visited:
            m = max(m, calculate_distances(p, grid) + grid[point][p])
    visited.remove(point)
    return m
def solve():
    global w,h
    global end
    part1 = 0 
    part2 = 0
    grid = []
    visual_grid = []
    visual_grid_part2 = []
    #y,x,dy,dx
    start = (0,0)
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
                    start = (index, c)
                if index == length - 1 and value == ".":
                    end = (index,c)
                    # print(end)
        # print(index)
    points_of_interest = [start, end]
    h = length
    w = len(grid[0])

    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "#":
                continue
            surround = 0
            for ny, nx in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
                if is_bounds((ny,nx)) and grid[ny][nx] != "#":
                    surround += 1
            if surround >= 3:
                points_of_interest.append((y,x))

    # print(len(points_of_interest))
    parts = []
    for part2 in [False, True]:
        point_lengths = {point:{} for point in points_of_interest}
        for point in point_lengths:
            queue = deque([point])
            visited = {point}
            distance = 0
            while queue: 
                for _ in range(len(queue)):
                    p = queue.popleft()
                    if p != point and p in visited:
                        continue
                    if p != point and p in point_lengths:
                        point_lengths[point][p] = distance
                        continue
                    for m in move(p, grid, part2 = part2):
                        queue.append(m)           
                    visited.add(p)
                distance += 1
        # print(point_lengths)
        parts.append(calculate_distances(start, point_lengths))
    
    # for l in visual_grid_part2:
    #     print(l)

    
    part1 = parts[0]
    part2 = parts[1]
    

                
                    
 
  

    
    
    
        
    #114542 is too high
    return f"Part 1: {part1}\nPart 2: {part2}"

if __name__ == "__main__":
    print(solve())