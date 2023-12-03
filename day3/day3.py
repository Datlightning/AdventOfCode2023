def evaluate(cell, lines):
    return lines[cell[0]][cell[1]] == "."
def bounds(cell, lines):
    return cell[0] < len(lines) and cell[0] >= 0 and cell[1] < len(lines[1]) and cell[1] >= 0
def check(row, col, currentnumber, lines):

    # col -= 1
    for i in range(len(currentnumber)):
        cell = [row + 1, col - i]
        if bounds(cell, lines) and not evaluate(cell, lines):
            return True
        cell = [row - 1, col - i]
        if bounds(cell,lines) and not evaluate(cell, lines):
            return True
   
    cell = [row, col - len(currentnumber)]
    if bounds(cell,lines) and not evaluate(cell, lines):
            return True

    cell = [row, col + 1]
    if bounds(cell,lines) and not evaluate(cell, lines):
            return True
        
   

    cell = [row-1, col - len(currentnumber)]
    if bounds(cell,lines) and not evaluate(cell, lines):
            return True
       
    cell = [row-1, col + 1]
    if bounds(cell,lines) and not evaluate(cell, lines):
            return True
        
    cell = [row+1, col - len(currentnumber)]
    if bounds(cell,lines) and not evaluate(cell, lines):
            return True
        
    cell = [row+1, col + 1]
    if bounds(cell,lines) and not evaluate(cell, lines):
        
            print(row,col)
            print(cell)
            print('case 8')
            return True
    return False
def part1():
    numbers = {'0','1','2','3','4','5','6','7','8','9'}
    lines = []
    with open("day3/input3.txt", "r") as file:
        lines = file.read().split("\n")
    for i in range(len(lines)):

        lines[i] = list(lines[i])
    total_sum = 0
    for r, row in enumerate(lines):
        currentnumber = ""
        for c, col in enumerate(row):
            if col in numbers:
                currentnumber += col
            else:
                if check(r,c-1,currentnumber, lines):
                    try:
                        total_sum += int(currentnumber)
                    except:
                        pass
                currentnumber = ""
        if check(r,len(row)-1,currentnumber, lines):
            print(currentnumber)
            try:
                total_sum += int(currentnumber)
            except:
                pass
    return total_sum
def get_number(r,c,lines):
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    output = ""
    y = c
    while bounds([r,y], lines) and lines[r][y] in numbers:
        output += lines[r][y]
        y += 1
    y = c - 1
    while bounds([r,y], lines) and lines[r][y] in numbers:
        output = lines[r][y] + output
        y -= 1
    return int(output)       
def is_number(cell, lines):
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    return lines[cell[0]][cell[1]] in numbers
def identify_surroundings(r,c,lines):
    output = set()
    
    cell = [r+1,c]
    if bounds(cell, lines) and is_number(cell, lines):
        output.add(get_number(cell[0], cell[1], lines))      
    
    cell = [r-1,c]
    if bounds(cell, lines) and is_number(cell, lines):
        output.add(get_number(cell[0], cell[1], lines)) 
        
    cell = [r+1,c+1]
    if bounds(cell, lines) and is_number(cell, lines):
        output.add(get_number(cell[0], cell[1], lines)) 
        
    cell = [r-1,c+1]
    if bounds(cell, lines) and is_number(cell, lines):
        output.add(get_number(cell[0], cell[1], lines)) 
        
    
    cell = [r,c+1]
    if bounds(cell, lines) and is_number(cell, lines):
        output.add(get_number(cell[0], cell[1], lines))      
    
    cell = [r,c-1]
    if bounds(cell, lines) and is_number(cell, lines):
        output.add(get_number(cell[0], cell[1], lines)) 
        
    cell = [r-1,c-1]
    if bounds(cell, lines) and is_number(cell, lines):
        output.add(get_number(cell[0], cell[1], lines)) 
        
    cell = [r+1,c-1]
    if bounds(cell, lines) and is_number(cell, lines):
        output.add(get_number(cell[0], cell[1], lines)) 
    
    return list(output)
    
def solve():
    lines = []
    with open("day3/input3.txt", "r") as file:
        lines = file.read().split("\n")
    for i in range(len(lines)):
        lines[i] = list(lines[i])
    total_sum = 0
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if col == "*":
                surround = identify_surroundings(r,c, lines)
                if len(surround) == 2:
                    total_sum += surround[0] * surround[1]

        
    return total_sum
    
#547476
#551623
print(solve())