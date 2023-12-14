def slide(direction, stationary_rocks, rocks_to_be_moved, width, height):
    dy, dx = direction
    changes = 0
    for i, rock in enumerate(rocks_to_be_moved):
        y,x = rock
        nextposition = (y + dy, x + dx)
        changes += 1
        while is_bounds(nextposition, height, width) and not nextposition in stationary_rocks:
           
            y,x = nextposition
            nextposition = (y + dy, x + dx)
            changes += 1
        y,x = nextposition  
        nextposition = (y - dy, x - dx)
        changes -= 1
        rocks_to_be_moved[i] = nextposition
        stationary_rocks.add(nextposition)
    return rocks_to_be_moved, changes, stationary_rocks
def calculate_score(rocks, height):
    score = 0
    for rock in rocks:
        y,x = rock
        score += height - y
    return score

def is_bounds(point, y, x):
    y1, x1 = point
    return 0<=y1<y and 0<=x1<x
def display(rocks, y, x):
    for r in range(y):
        string = ""
        for c in range(x):
            if (r,c) in rocks:
                string+="O"
            else:
                string+="."
        print(string)
def solve():
    lines = []
    parts = [0,0]
    with open("day14/day14.txt", "r") as file:
        lines = file.read().strip().split("\n")
    stationary_rocks = set()
    rocks_to_be_moved = list()
    for r, line in enumerate(lines):
        for c, rock in enumerate(line):
            match rock:
                case "O":
                    rocks_to_be_moved.append((r,c))
                case ".":
                    pass
                case "#":
                    stationary_rocks.add((r,c))
    height = r+1
    width = c+1
    # display(stationary_rocks, height, width)

    print()
    changes = -1
    for i in range(1000000000):
        display(rocks_to_be_moved, height, width)
        for direction in [[-1,0],[0,-1],[1,0],[0,1]]:
            rocks_to_be_moved, changes, stationary_rocks = slide(direction, stationary_rocks, rocks_to_be_moved, width, height)
            
        if changes == 0:
                break
        # display(stationary_rocks, height, width )

    print(calculate_score(rocks_to_be_moved, height))
    part1 = parts[0]
    part2 = parts[1]
    print(f"Part 1: {int(part1)}\nPart 2: {int(part2)}")
    return 
#106648
if __name__ == '__main__':
    solve()
