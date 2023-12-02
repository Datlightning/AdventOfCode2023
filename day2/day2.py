#13:37
def part1(line):  
    limits = {
        "red":12,
        "green":13,
        "blue":14
    }
    output = {"red":0, "blue":0, "green":0, "id":0}
    first_split = line.split(":")
    for round in first_split[1].split(";"):
        temp = {"red":0, "blue":0, "green":0, "id":0}
        for number_color in round.split(","):
            data = number_color.split(" ")
            color = data[2]
            number = int(data[1])
            temp[color] += number
            if(temp[color] > limits[color]):
                return 0
    return int(first_split[0].split(" ")[1])
def part2(line):
    maxs = {
        "red":0,
        "blue":0,
        "green":0
    }
    first_split = line.split(":")
    for round in first_split[1].split(";"):
        temp = {"red":0, "blue":0, "green":0, "id":0}
        for number_color in round.split(","):
            data = number_color.split(" ")
            color = data[2]
            number = int(data[1])
            temp[color] += number
        maxs["red"] = max(maxs["red"], temp["red"])
        maxs["green"] = max(maxs["green"], temp["green"])
        maxs["blue"] = max(maxs["blue"], temp["blue"])
    return maxs["red"] * maxs["blue"] * maxs["green"]
def solve():
    lines = []
    with open("day2/input2.txt", "r") as file:
        lines = file.read().split("\n")
    ids = []
    
    return sum(list(map(part2, lines)))