
rules = {}

def consider_rule(rule, part):
    for individual_rule in rule.split(","):
        individual_rule = individual_rule.split(":")
        if len(individual_rule) == 1:
            return individual_rule[0]
        potential_container = individual_rule[1]
        expression = individual_rule[0]
        key = expression[0]
        operator = expression[1]
        value = int(expression[2:])
        condition = f"{part[key]}{operator}{value}"
        if eval(condition):
            return potential_container
    return -1
def get_variations(rule):
    containers = []
    for individual_rule in rule.split(","):
        individual_rule = individual_rule.split(":")
        if len(individual_rule) == 1:
            containers.append(individual_rule[0])

            continue
        potential_container = individual_rule[1]
        expression = individual_rule[0]
        key = expression[0]
        operator = expression[1]
        value = int(expression[2:])
        containers.append([potential_container, key, operator, value])
        # opposite_rules.append([key, "<" if operator == ">" else ">", (value - 1) if operator == "<" else (value + 1)])
    return containers
def is_auto_accept(rule):
    for i in rule.split(","):
        if i[-1] != "A":
            return False
    return True
def get_rules_to_end(starting_rule):
    if starting_rule == "R":
        return [False]
    if starting_rule == "A":
        return [True]
    for dictionary in get_variations(starting_rule):
        for container, rule in dictionary.items():
            return [{container:rule}] + get_rules_to_end(container)
def count(ranges, name = "in"):
    global rules
    if name == "R":
        return 0
    if name == "A":
        output = 1
        for low, high in ranges.values():
            output *= high - low + 1
        return output
    new_rules = get_variations(rules[name])
    total = 0

    for target, key, operator, value in new_rules[:-1]:
        low, high = ranges[key]
        if operator == "<":
            correct = (low, value - 1)
            false = (value, high)
        else:
            correct = (value + 1, high)
            false = (low, value)
        if correct[0] <= correct[1]:
            copy = dict(ranges) 
            copy[key] = correct
            total += count(copy, target)
        if false[0] <= false[1]:
            ranges = dict(ranges)
            ranges[key] = false
        else:
            break
    else:
        total += count(ranges, new_rules[-1])
    return total
def solve():
    global rules
    part1 = 0
    part2 = 0
    parts = []
    rules = {}
    container_hits = {}
    with open("day19/day19.txt", "r") as file:
        split_file = file.read().split("\n\n")
        for part in split_file[1].split("\n"):
            part = part.replace("{", "{'")
            part = part.replace(",", ",'")
            part = part.replace("=","':")
            parts.append(eval(part))
        for rule in split_file[0].split("\n"):
            rule = rule.split("{")
            container = rule[0]
            actual_rule = rule[1][:-1]
            rules[container] = actual_rule
            container_hits[container] = 0
    #Path to A
    #Rules that need to be met to get to A
    #Sum of all values that meet those rules
    #path = [{container: rule}]
    for part in parts:
        container = "in"  
        while container != "A" and container != "R":
            container = consider_rule(rules[container], part)
        if container == "A":
            part1 += sum(part.values())
    


    part2 = count({key: (1,4000) for key in "xmas"})
    # auto_accept = set()
    # for container, rule in rules.items():
    #     if "A" not in rule:
    #         continue
    #     if is_auto_accept(rule):
    #         auto_accept.add(container)
# 
    # print(auto_accept)




    return f"Part 1: {part1}\nPart 2: {part2}"
if __name__ == "__main__":
    print(solve())