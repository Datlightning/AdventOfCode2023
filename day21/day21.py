def expand(start, walls, max_y, max_x, restrict):
    y,x = start
    output_points = []
    for dy, dx in [(0,1), (1,0),(-1,0),(0,-1)]:
        ny = y + dy
        nx = x + dx
        if not restrict:
            ty = ny % max_y
            tx = nx % max_x
            if (ty, tx) not in walls:
                output_points.append((ny, nx))
        else:
            if 0<=ny<max_y and 0<=nx<max_x and (ny, nx) not in walls:
                output_points.append((ny, nx))
    return output_points

def solve():
    grid = []
    start = (0,0)
    walls = set()
    with open("day21/day21.txt", "r") as file:  
        for row, line in enumerate(file.read().strip().split("\n")):
            grid.append([])
            for col, char in enumerate(line):
                grid[row].append(char)
                if char == "S":
                    start = (row, col)
                if char == "#":
                    walls.add((row, col))
    sr, sc = start    

    max_y = len(grid)
    max_x = len(grid[0])
    parts = []
    for part, data in enumerate([(start,64), #part 1
                                 (start,max_x*2 + 1), (start,max_x*2), #even and odd counts
                                 ((sr,0), max_x - 1), ((0,sc), max_x - 1), ((max_x - 1, sc), max_x - 1), ((sr, max_x - 1), max_x - 1), #corner counts
                                 ((max_x - 1 ,0), max_x // 2-1), ((0,max_x - 1), max_x // 2-1), ((max_x - 1 , max_x - 1), max_x // 2-1), ((0,0), max_x // 2-1), # small spaces
                                ((max_x - 1 ,0), (3 * max_x) // 2-1), ((0,max_x - 1), (3 * max_x) // 2-1), ((max_x - 1 , max_x - 1), (3 * max_x )// 2-1), ((0,0), (3 * max_x) // 2-1)]): #big spaces
        steps = data[1]
        start = data[0]
        odd = steps % 2 == 1
        queue = [start]
        # bfs_grid[start[0]][start[1]] = 0
        resulting_points = set()
        visited = set()
        for i in range(1,steps+1):
            new_queue = set()
            while queue:
                point = queue.pop()
                for expansion in expand(point, walls, max_y, max_x, restrict=True):
                    if expansion in visited:
                        continue
                    if i%2 == (1 if odd else 0):
                        resulting_points.add(expansion)
                    visited.add(expansion)
                    new_queue.add(expansion)
            queue = list(new_queue)
        
        resulting_length = len(resulting_points)
        parts.append(resulting_length)
        # print(resulting_length)
    
                
    part1 = parts[0]

    part2 = 0
    steps = 26501365
    grid_width = steps//max_x - 1
    odd_tiles = (grid_width // 2 * 2 + 1)**2
    even_tiles = ((grid_width + 1)//2 * 2) ** 2
    odd_points = parts[1]
    even_points = parts[2]
    corners = sum(parts[3:8])
    small_segments = sum(parts[8:13]) * (grid_width + 1)
    large_segments = sum(parts[13:18]) * grid_width
    full_tiles = odd_tiles * odd_points + even_tiles * even_points
    part2 = corners + full_tiles + small_segments + large_segments
    #618259906474270 is too low
    #618261433623748 is too high
    return f"Part 1: {part1}\nPart 2: {part2}"

if __name__ == "__main__":
    print(solve())