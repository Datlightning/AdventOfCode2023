crossed = {}
def get_expected_values(sequence):
    values = []
    value = 0
    for i in sequence:
        if i == "#":
            value += 1
        elif value > 0:
            values.append(value)
            value = 0
    return values
def calculate_arrangements(sequence, expected_values):
    if sequence == "":
        if expected_values == ():
            return 1
        return 0
    if expected_values == ():
        if "#" in sequence:
            return 0
        return 1
    output = 0
    
    key = (sequence, expected_values)
    if key in crossed:
        return crossed[key]
    
    if sequence[0] in ".?":
        output += calculate_arrangements(sequence[1:], expected_values)
    if sequence[0] in "#?":
        if expected_values[0] <= len(sequence) and '.' not in sequence[:expected_values[0]] and (expected_values[0] == len(sequence) or sequence[expected_values[0]] != "#"):
            output += calculate_arrangements(sequence[expected_values[0] + 1:], expected_values[1:])
        else:
            output += 0
    crossed[key] = output   
    return output
        
def solve():
    lines = []
    with open("day12/day12.txt", "r") as file:
        lines = file.read().strip().split("\n")
    split_lines = []
    unknown_segments = {}
    for line in lines:
        splitline = line.split(" ")
        firstpart = tuple(map(int, splitline[1].split(',')))
        insertion = (splitline[0], firstpart)
        split_lines.append(insertion)
    part1 = 0
    part2 = 0
    for line, values in split_lines:
        part1 += calculate_arrangements(line, values)
        newline = "?".join([line] * 5)
        newvalues = []
        for i in range(5):
            for v in values:
                newvalues.append(v)
        newvalues = tuple(newvalues)
        part2 += calculate_arrangements(newline, newvalues)
    print(f"Part 1: {int(part1)}\nPart 2: {int(part2)}")
    return 

if __name__ == '__main__':
    solve()