def encode_in_binary(line):
    binary_sequence = 0
    for c in line:
        binary_sequence *= 2
        binary_sequence += 0 if c == "." else 1
    return binary_sequence
def is_symmetrical(binary_list, part):
    if part:
        return binary_list == binary_list[::-1] and len(binary_list) % 2 == 0
    
def find_symmetry(grid, part):
    
    grid = grid.split("\n")
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
        # print(binary_left_row)
        if is_symmetrical(binary_left_row, part):
            # print(removed_left)
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
    part1 = 0
    part2 = 0
    with open("day13/day13.txt", "r") as file:
        lines = file.read().strip().split("\n\n")
    for line in lines:
        symmetry = find_symmetry(line)
        assert symmetry != -1, f"No symmetry found in\n {line}"
        part1 += find_symmetry(line)
        
    print(f"Part 1: {int(part1)}\nPart 2: {int(part2)}")
    return 

#34420 too high
if __name__ == '__main__':
    solve()