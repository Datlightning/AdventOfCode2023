def encode_in_binary(line):
    binary_sequence = 0
    for c in line:
        binary_sequence *= 2
        binary_sequence += 0 if c == "." else 1
    return binary_sequence
def is_symmetrical(binary_list):
    return binary_list == binary_list[::-1]
def find_symmetry(grid):
    grid = grid.split("\n")
    binary_left = []
    binary_right = []
    for i, g in enumerate(grid, start = 1):     
        binary_value = encode_in_binary(g)
        binary_left.append(binary_value)
        binary_right = [binary_value] + binary_right
    removed_left = 0
    while len(binary_left) != 0:
        if is_symmetrical(binary_left):
            return 100 * (removed_left + len(binary_left)//2 )
        else:
            removed_left += 1
            del  binary_left[0]
    removed_right = 0
    while len(binary_right) != 0:
        if is_symmetrical(binary_right):
            return 100 * (binary_right + len(binary_right)//2 )
        else:
            removed_right += 1
            del binary_right[0]
    return -1
def solve():
    lines = []
    part1 = 0
    part2 = 0
    with open("day13/day13.txt", "r") as file:
        lines = file.read().strip().split("\n\n")
    for line in lines:
        print(find_symmetry(line))

    


    print(f"Part 1: {int(part1)}\nPart 2: {int(part2)}")
    return 

if __name__ == '__main__':
    solve()