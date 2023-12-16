def get_value(string):
    running_value = 0
    for i in string:
        running_value += ord(i)
        running_value *= 17
        running_value %= 256
    return running_value
def score(boxes):
    output = 0
    for box_number, lenses in boxes.items():
        position = 0
        lense_position = 1
        box_powers = []
        for key, powers in lenses.items():
            if len(box_powers) == 0:
                box_powers.append(powers)
                continue
            position = powers["position"]
            insertion = False
            for index, i in enumerate(box_powers):
                current_position = i["position"]
                if position < current_position:
                    insertion = True
                    box_powers.insert(index, powers)
                    break
            if not insertion:
                box_powers.append(powers)
        # print(box_powers)
        for position, box in enumerate(box_powers, start = 1):
           power = int(box['power'])
        #   print(f"{position} x {power} x {box_number+1}")
           output += position * power * int(box_number + 1)
    return output
def solve():
    strings = []
    part1 = 0
    with open("day15/day15.txt", "r") as file:
        strings = file.read().split("\n")[0].split(",")
    for s in strings:
        current_value = get_value(s)
        part1 += current_value
    part2 = 0
    #{BoxID: name: focusing_power}
    boxes = {}
    end_positions = {}
    for instruction in strings:
        split = instruction.split("=")
        if len(split) == 2:
            name = split[0]
            focusing_power = split[1]
            box_id = get_value(name)
            if not box_id in boxes:
                boxes[box_id] = {}
                end_positions[box_id] = 1
            end_positions[box_id] += 1
            position = end_positions[box_id]
            if not name in boxes[box_id]:
                boxes[box_id][name] = {}
                boxes[box_id][name]["position"] = position
            boxes[box_id][name]["power"] = focusing_power

        else:
            split = instruction.split("-")
            name = split[0]
            box_id = get_value(name)
            if box_id in boxes:
                if name in boxes[box_id]:
                    del boxes[box_id][name]
    part2 = score(boxes)
    return f"Part 1: {part1}\nPart 2: {part2}"
if __name__ == "__main__":
    print(solve())