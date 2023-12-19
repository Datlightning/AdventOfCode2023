from heapq import heappop, heappush
#point = (heat_loss, y, x, dy, dx, point_length)
max_x = None
max_y = None
def is_bounds(point):
    _, y,x ,_,_,_ = point
    return 0<=y<max_y and 0<=x<max_x
def get_moves(point, grid):
    heat_loss, y, x, dy, dx, point_length = point
    moves = []
    if point_length < 3 and not (dy,dx) == (0,0):
        new_y = y+dy
        new_x = x + dx
        if is_bounds((0, new_y, new_x, 0,0,0)):
            point = (heat_loss+grid[new_y][new_x],new_y, new_x, dy,dx, point_length + 1)
            moves.append(point)
    for possible_dy, possible_dx in [(0,1), (1,0), (0,-1), (-1,0)]:
        if not (possible_dy, possible_dx) == (dy, dx) and not (possible_dy, possible_dx) == (-dy, -dx):
            new_y = y + possible_dy
            new_x = x + possible_dx
            if is_bounds((0, new_y, new_x, 0,0,0)):
                point = (heat_loss+grid[new_y][new_x], new_y, new_x, possible_dy,possible_dx, 1)
                moves.append(point)
    return moves
def get_moves_part2(point, grid):
    heat_loss, y, x, dy, dx, point_length = point
    moves = []
    if point_length < 10 and not (dy,dx) == (0,0):
        new_y = y+dy
        new_x = x + dx
        if is_bounds((0, new_y, new_x, 0,0,0)):
            point = (heat_loss+grid[new_y][new_x],new_y, new_x, dy,dx, point_length + 1)
            moves.append(point)
    if point_length >= 4 or (dy,dx) == (0,0):
        for possible_dy, possible_dx in [(0,1), (1,0), (0,-1), (-1,0)]:
            if not (possible_dy, possible_dx) == (dy, dx) and not (possible_dy, possible_dx) == (-dy, -dx):
                new_y = y + possible_dy
                new_x = x + possible_dx
                if is_bounds((0, new_y, new_x, 0,0,0)):
                    point = (heat_loss+grid[new_y][new_x], new_y, new_x, possible_dy,possible_dx, 1)
                    moves.append(point)
    return moves
       
def solve():
    global max_y
    global max_x
    grid = []
    with open("day17/day17.txt", "r") as file:
        for i, line in enumerate(file.read().strip().split("\n")):
            insertion = list(map(int, list(line)))
            grid.append(insertion)

    max_y = len(grid)
    max_x = len(grid[0])
    queue = [(0,0,0,0,0,0)]
    visited = set()
    part1 = 0
    while queue:
        # set_queue.remove(point)
        point = heappop(queue) 
        heat,y,x,dy,dx, point_length = point
        if (y,x,dy,dx,point_length) in visited:
            continue
        if y == max_y - 1 and x == max_x - 1:
            part1 = heat 
            break
        
        
            
        next_moves = get_moves(point, grid)
        for p in next_moves:
            heappush(queue, p)
        visited.add((y,x,dy,dx,point_length))
    
    
    part2 = 0
    queue = [(0,0,0,0,0,0)]
    visited.clear()
    while queue:
        # set_queue.remove(point)
        point = heappop(queue) 
        heat,y,x,dy,dx, point_length = point
        if (y,x,dy,dx,point_length) in visited:
            continue
        if y == max_y - 1 and x == max_x - 1 and point_length >= 4:
            part2 = heat 
            break     
        next_moves = get_moves_part2(point, grid)
        for p in next_moves:
            heappush(queue, p)
        visited.add((y,x,dy,dx,point_length))

    return f"Part 1: {part1}\nPart 2: {part2}"
#1151 is too low
if __name__ == "__main__":
    print(solve())