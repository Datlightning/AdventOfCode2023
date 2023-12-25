
def get_groups(connections):
    visited = set()
    groups = []
    for key in connections:
        current_group = set()
        queue = [key]
        if key in visited:
            continue
        while queue:
            item = queue.pop(0)
            if item in visited:
                continue
            current_group.add(item)

            visited.add(item)
            queue.extend(list(connections[item]))
        if current_group:
            groups.append(current_group)
    return groups

def remove_connection(connections, source, dest):
    connections[source].remove(dest)
    connections[dest].remove(source)
def solve(testing = False):
    part1 = 0 
    part2 = 0
    filename = "day25/day25.txt" if not testing else "day25/testing.txt"
    connections = {}
    with open(filename, "r") as file:  
        for line in file.read().strip().split("\n"):
            split_line = line.split(":")
            source = split_line[0].strip()
            linked = split_line[1].strip().split(" ")
            
            if source not in connections:
                connections[source] = set()
            connections[source].update(set(linked))
            for c in linked:
                if c not in connections:
                    connections[c] = set()
                connections[c].add(source)
    superstring = ""
    visited = set()
    for key, value in connections.items():
        for v in value:
            if (key,v) in visited:
                continue
            visited.add((key,v))
            visited.add((v,key))
            superstring += f"{key} -> {v}\n"
    # print(superstring)
    with open("output.txt", "w") as file:
        file.write(superstring)
    # ttempted = set()
   
    remove_connection(connections, "crg", "krf")      
    remove_connection(connections, "rgv", "jct")      
    remove_connection(connections, "zhg", "fmr")      
    

    groups = get_groups(connections)
    print(len(groups))
    if len(groups) == 2:
        print(len(groups[0]) * len(groups[1]))
        return
                
    
    return f"Part 1: {part1}\nPart 2: {part2}"

if __name__ == "__main__":
    print(solve(testing = False))
    # print(solve())