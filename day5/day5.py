def get_value(rule, position):
    for specific_rule in rule:
        source_range_start = int(specific_rule[1])
        range_length = int(specific_rule[2])
        destination_range = int(specific_rule[0])
        if source_range_start <= position < source_range_start + range_length:
            destination_index = position - source_range_start 
            destination_value = destination_range + destination_index
            return destination_value
    return position
def get_range(rule, input_range):
    output = []
    for specific_rule in rule:
        source_range_start = int(specific_rule[1])
        range_length = int(specific_rule[2])
        destination_range = int(specific_rule[0])
        source_range_end = source_range_start + range_length
        next_range = []
        while (len(input_range) > 0):
            specific_range = input_range.pop()
            specific_range_start = specific_range[0]
            specific_range_end = specific_range[1]
            
            before_range = (specific_range_start, min(source_range_start, specific_range_end))
            shared_range = (max(specific_range_start, source_range_start), min(specific_range_end, source_range_end))
            after_range = (max(source_range_end, specific_range_start),specific_range_end)
            if shared_range[0] < shared_range[1]:
                shared_range_start = shared_range[0]
                shared_range_end = shared_range[1]
                transformed_tuple = (shared_range_start - source_range_start + destination_range, shared_range_end - source_range_start + destination_range)
                output.append(transformed_tuple)
            if before_range[0] < before_range[1]:
                next_range.append(before_range)
            if after_range[0] < after_range[1]:
                next_range.append(after_range)
        input_range = next_range
        
    return output + input_range
    
    
def solve():
    lines = []
    with open("day5/input5.txt", "r") as file:
        lines = file.read().strip().split("\n\n")
    seeds = list(map(int, lines[0].split(":")[1].split()))
   
    rules = []
    for line in lines[1:]:
        newlines = line.split("\n")[1:]
        tuples = []
        for temp_rule in newlines:
            tuples.append(list(map(int, temp_rule.split(" "))))
        rules.append(tuples)
    lowest1 = -1
    for seed in seeds:
        for rule in rules:
            seed = get_value(rule, seed)
        value = seed
        if lowest1 == -1 or value < lowest1:
            lowest1 = value   
                
    lowest2 = -1
    for i in range(0,len(seeds), 2):
        possible_values = [(seeds[i], seeds[i] + seeds[i+1])]
        for rule in rules:
            possible_values = get_range(rule, possible_values)
        value = min(possible_values)
        if lowest2 == -1 or min(value) < lowest2:
            lowest2 = min(value)
    
    parts = [lowest1, lowest2]
    return parts

    


    
#5833065
print(solve())