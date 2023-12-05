def get_value(destination_range, source_range_start, range_length, position, first):
    if position >= source_range_start and position < source_range_start + range_length:
        destination_index = position - source_range_start 
        desination_value = destination_range + destination_index
        return desination_value
    if first:
        return position
    return -1

def solve():
    lines = []
    with open("day5/input5.txt", "r") as file:
        lines = file.read().split("\n")
    seed_ranges = list(map(int, lines[0].split(":")[1].split(" ")[1:]))
    seeds = set()
    for i in range(0,len(seed_ranges), 2):
        seeds.union(set(range(seed_ranges[i], seed_ranges[i] + seed_ranges[i+1])))
        print(i)
    seed_dict = {
        
    }
    lowest = -1
    for seed in seeds:
        seed_dict[seed] = seed
    for seed in seeds:
        temp_value = seed_dict[seed]
        for line in lines[1:]:
            initial_seed = seed_dict[seed]
            if line != "" and not "map" in line:
                line_list = line.split(" ")
                destination_range = int(line_list[0])
                source_range = int(line_list[1])
                range_length = int(line_list[2])
              
                
                current_value = get_value(destination_range, source_range, range_length, initial_seed, initial_seed == temp_value)             
                if (current_value != -1):
                    temp_value = current_value
                
            elif "map" in line:
                seed_dict[seed] = temp_value  
             
        seed_dict[seed] = temp_value
        if (lowest == -1 or temp_value < lowest):
            lowest = temp_value
    return lowest

    


    
#5833065
print(solve())