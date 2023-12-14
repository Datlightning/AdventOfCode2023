def encode_in_binary(line):
    binary_sequence = 0
    for c in line:
        binary_sequence *= 2
        binary_sequence += 0 if c == "." else 1
    return binary_sequence



def is_symmetrical(binary_list, part):
    if part:
        return binary_list == binary_list[::-1] and len(binary_list) % 2 == 0
def find_single_error(grid):
    length = len(grid)
    for row_symmetry in range(len(grid)-1):
        error = 0
        for r, row in enumerate(grid):
            up = row_symmetry - r 
            down = row_symmetry + r + 1
            if 0<= up<down<length:
                for c, col in enumerate(grid[0]):
                    if grid[up][c] != grid[down][c]:
                        error += 1
        if error == 1:
            return 100 * (row_symmetry + 1)
    for col_symmetry in range(len(grid[0])-1):
        error = 0
        for c in range(len(grid[0])):
            left = col_symmetry - c 
            right = col_symmetry + c + 1
            if 0<=left<right<len(grid[0]):
                for r in range(length):
                    if grid[r][left] != grid[r][right]:
                        error += 1
        if error == 1:
            return col_symmetry + 1     

    return -1
def find_symmetry(grid, part):
    grid = grid.split("\n")
    if part == False:
        return find_single_error(grid)
    columns = {}
    binary_left_row = []
    binary_right_row = []
    binary_left_col = []
    binary_right_col = []
    for i, g in enumerate(grid, start = 1):     
        binary_value = encode_in_binary(g)
        binary_left_row.append(binary_value)
        binary_right_row = [binary_value] + binary_right_row
        for index, c in enumerate(g):
            if index in columns:
                columns[index].append(c)
            else:
                columns[index] = [c]
                
    for key, value in columns.items():
        binary_value = encode_in_binary(value)
        binary_left_col.append(binary_value)
        binary_right_col = [binary_value] + binary_right_col
        
    removed_left = 0
    while len(binary_left_row) > 1:
        if is_symmetrical(binary_left_row, part):
            return 100 * (removed_left + len(binary_left_row)//2)
        else:
            removed_left += 1
            del binary_left_row[0]

    while len(binary_right_row) > 1:
        if is_symmetrical(binary_right_row, part):
            return 100 * (len(binary_right_row)//2)
        else:
            del binary_right_row[0]
             
    removed_left = 0
    while len(binary_left_col) > 1:
        if is_symmetrical(binary_left_col, part):
            return (removed_left + len(binary_left_col)//2)
        else:
            removed_left += 1
            del binary_left_col[0]
            
    while len(binary_right_col) > 1:
        if is_symmetrical(binary_right_col, part):
            return (len(binary_right_col)//2 )
        else:
            del binary_right_col[0]
    return -1

def solve():
    lines = []
    parts = [0,0]
    with open("day13/day13.txt", "r") as file:
        lines = file.read().strip().split("\n\n")
        for part1 in [True, False]:
            for line in lines:
                    symmetry = find_symmetry(line, part1)
                    assert symmetry != -1, f"No symmetry found in\n {line}"
                    parts[0 if part1 else 1] += symmetry
    part1 = parts[0]
    part2 = parts[1]
    print(f"Part 1: {int(part1)}\nPart 2: {int(part2)}")
    return 

#87700
if __name__ == '__main__':
    solve()