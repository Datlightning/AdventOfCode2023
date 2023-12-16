class Pose:
    def __init__(self, y, x, heading, grid):
        self.y = y
        self.x = x
        self.value = grid[y][x]
        self.powered = False
        self.heading = heading
        self.max_y = len(grid)
        self.max_x = len(grid[0])
        self.grid = grid
    def get_powered(self):
        return self.powered
    def move(self):
        self.heading %= 360
        dx = 0
        dy = 0
        
        
directions = {
    "|":{
        0: [(1,0, 270),(-1,0, 90)],
        180: [(1,0, 270), (-1,0, 90)],
        270: [(1,0, 270)],
        90: [(-1,0, 90)]
    },
    ".":{
        0: [(0,1,0)],
        90: [(-1,0,90)],
        180:[(0,-1,180)],
        270:[(1,0,270)]
    },
    "-":{
        0: [(0,1,0)],
        90: [(0,1, 0),(0,-1, 180)],
        180:[(0,-1,180)],
        270:[ (0,-1, 180),(0,1, 0)]
    },
    "/":{
        0:[ (-1,0, 90)],
        90: [ (0,1, 0)],
        180: [(1,0, 270)],
        270: [ (0,-1, 180)]
    },
    "\\":{
        0:[ (1,0, 270)],
        90: [ (0,-1, 180)],
        180: [(-1,0, 90)],
        270: [ (0,1, 0)]
    }
}
max_y = None
max_x = None
visited = {}
visited_headings = set()

def is_bounds(point):
    y,x,_ = point
    return 0<=y<max_y and 0<=x<max_x
def expand(point, grid):
    global visited
    y,x,heading = point
    value = grid[y][x]
    moves = directions[value][heading]
    output = []
    for dy, dx, heading in moves:
        potential_point = (y + dy, x + dx, heading)
        xypoint = (y+dy, x+dx)
        if is_bounds(potential_point) and not potential_point in visited_headings:
            output.append(potential_point)
    # print(f"Initial Point: {point}")
    # print(f"Output Points: {output}")
    # print()
    return output
def display(visited, grid):
    display_dict = {
        0: ">",
        90:"^",
        180:"<",
        270:"v"
    }
    for y, row in enumerate(grid):
        string =""
        for x, col in enumerate(row):
            if col == "." and (y,x) in visited:
                string += display_dict[visited[(y,x)]]
            else:
                string += col
        print(string)
def solve():
    global max_x
    global max_y
    global visited_headings
    global visited
    part1 = 0
    part2 = 0
    #(y,x,heading)
    grid = []
    with open("day16/day16.txt", "r") as file:
        for line in file.read().strip().split("\n"):
            grid.append(list(line))
    max_y = len(grid)
    max_x = len(grid[0])
    possible_starting_points = [(0,0,0),(0,0,270),(0, max_x - 1, 270), (0, max_x -1, 180), (max_y - 1, 0, 90),(max_y - 1,0 , 0), (max_y - 1, max_x-1, 90),(max_y - 1,max_x -1 , 180)]
    for x in range(1, max_x):
        possible_starting_points.append((0,x,270))
        possible_starting_points.append((max_y-1,x,90))
    for y in range(1, max_y):
        possible_starting_points.append((y,0,0))
        possible_starting_points.append((y,max_x-1,180))
    # print(possible_starting_points)
    # print()
    starting_lengths = {}
    max_length = 0
    best_point = (0,0,0)
    best_visited_heading = set()
    best_visited_display = {}
    part1 = -1
    for starting_point in possible_starting_points:
                queue = [starting_point]
                while len(queue) > 0:
                    point = queue.pop(0)
                    y, x, heading = point
                    if not heading is None:
                        queue.extend(expand(point, grid))
                        # print(queue)
                    visited_headings.add(point)
                    visited[(y,x)] = heading
                    # display(visited, grid)
                    # print(f"Queue: {queue}")
                if part1 == -1:
                    part1 = len(visited)
                if len(visited) > max_length:
                    max_length = len(visited)
                    best_point = starting_point
                    best_visited_heading.clear()
                    best_visited_heading.update(visited_headings)
                    best_visited_display = visited
                visited_headings.clear()
                visited = {}

    part2 = max_length
    # print(best_point)
    # display(best_visited_display, grid)
    # print(best_visited_heading)
    return f"Part 1: {part1}\nPart 2: {part2}"

if __name__ == "__main__":
    print(solve())