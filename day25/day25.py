from graphviz import CalledProcessError, Graph
import networkx as nx

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
            
    
    dot = Graph()
    G = nx.Graph()
    visited = set()
    for key, value in connections.items():
        dot.node(key)
        for v in value:
            if (key,v) in visited:
                continue
            visited.add((key,v))
            visited.add((v,key))
            dot.node(v)
            dot.edge(key, v)
            G.add_edge(key, v)
            G.add_edge(v, key)

    dot.engine = 'neato'
    # dot.render('test-output/round-table.gv', view=True)

    try:
        dot.render('day25/graph')
    except CalledProcessError:
        print('Delete "graph.pdf" from "day25" for a visualization.')
        
    to_remove = nx.minimum_edge_cut(G)
   
    for connection in to_remove:
        remove_connection(connections, connection[0], connection[1])          
    

    groups = get_groups(connections)
    # print(len(groups))
    if len(groups) == 2:
        part1 = len(groups[0]) * len(groups[1])
        
                
    
    return f"Part 1: {part1}"

if __name__ == "__main__":
    print(solve(testing = False))
    # print(solve())