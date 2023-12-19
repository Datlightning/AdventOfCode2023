from heapq import heappush


def rgb_to_number(text):
    text = text[1:-1].replace("#", "0x")
    length = int(text[0:7], 16)
    direction = text[-1]
    # print(direction)
    # print(length)
    return [length, direction]

def solve():

    direction = {
        "R":(0,1), 
        "L":(0,-1), 
        "D":(1,0), 
        "U":(-1,0),

    
    }
    letters = {
        "0":"R",
        "1":"D",
        "2":"L",
        "3":"U"
    }
    instructions = []
    p2_instructions = []

    part1 = 0
    part2 = 0
    with open("day18/day18.txt", "r") as file:
        for i, line in enumerate(file.read().strip().split("\n")):
            insertion = line.split(" ")
            insertion[2] = rgb_to_number(insertion[2])
            insertion[1] = int(insertion[1])
            insertion[0] = direction[insertion[0]]
            
            instructions.append(insertion)
            p2insertion =  insertion[2]
            p2insertion[1] = direction[letters[p2insertion[1]]]
            p2_instructions.append(p2insertion)
    points = [(0,0)]
    path_length = 0
    y = 0
    x = 0
    rows = {}
    for move, scalar, _ in instructions:
        dy,dx = move
        for i in range(scalar):
            y_value = y + (i * dx)
            x_value = x + (i * dx)
            if y_value not in rows:
                rows[y_value] = []
            heappush(rows[y_value],x_value)
            
        y += dy * scalar
        x += dx * scalar
        path_length += scalar
        points.append((y,x))
        
    #shoelace theorem
    A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
    
    interior_points = A-path_length//2 + 1 #Pick's Theorem
    part1 = path_length + interior_points
    

    
    points = [(0,0)]
    path_length = 0
    y = 0
    x = 0
    for scalar, move in p2_instructions:
        dy,dx = move
        y += dy * scalar
        x += dx * scalar
        path_length += scalar
        points.append((y,x))
    
    A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2

                
            
                
    interior_points = A-path_length//2 + 1 #Pick's Theorem
    part2 = path_length + interior_points
    
    
    return f"Part 1: {part1}\nPart 2: {part2}"
if __name__ == "__main__":
    print(solve())