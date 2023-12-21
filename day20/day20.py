import math
from copy import deepcopy

def solve():
    global rules
    part1 = 0
    part2 = 0
    nodes = {}
    network_grid = {"broadcaster":[]}
    with open("day20/day20.txt", "r") as file:
        for line in file.read().strip().split("\n"):
            split_line =line.split("->")
            targets = split_line[1].split(",")
            inputs = None
            for i, t in enumerate(targets):
                targets[i] = t.strip()
            if split_line[0].strip() == "broadcaster":
                item_type = "broadcaster"
                name = "broadcaster"
                for i, t in enumerate(targets):
                    targets[i] = (t, False, "broadcaster")
            elif split_line[0][0] == "&":
                item_type = "conjunction"
                name = split_line[0][1:].strip()
                inputs = []
            elif split_line[0][0] == "%":
                item_type = "flip_flop"
                name = split_line[0][1:].strip()
            network_grid[name] = {"targets":targets, "type":item_type, "input":inputs}
            nodes[name] = False
    rx_feeder = ""
    for key, value in network_grid.items():
        if value["input"] is not None:
            for possible_input_source, data in network_grid.items():
                if key in data["targets"]:
                    value["input"].append(possible_input_source)
        if "rx" in value["targets"]:
            rx_feeder = key
    cycle_nodes = set()
    cycle_lengths = {}
    for key, value in network_grid.items():
        if rx_feeder in value["targets"]:
            cycle_nodes.add(key)
    high_signals = 0
    low_signals = 0
    for i in range(1000):
        queue = deepcopy(network_grid["broadcaster"]["targets"])
        low_signals += 1
        while queue:
            current_node = queue.pop()
            receiver = current_node[0]
            signal_type = current_node[1]
            sender = current_node[2]
            if receiver == rx_feeder and sender in cycle_nodes and nodes[sender]:
                if sender not in cycle_lengths:
                    cycle_lengths[sender] = i + 1
                    cycle_nodes.remove(sender)
                    print(cycle_lengths)
            if signal_type:
                high_signals += 1
            else:
                low_signals += 1
            if receiver not in network_grid:
                continue
            if network_grid[receiver]["type"] == "flip_flop":
                if signal_type:
                    continue
                nodes[receiver] = not nodes[receiver]
                output_signal = nodes[receiver]
                for target in network_grid[receiver]["targets"]:
                    queue.append((target, output_signal,receiver))
            elif network_grid[receiver]["type"] == "conjunction":
                output_signal = False
                for input_source in network_grid[receiver]["input"]:
                    if not nodes[input_source]:
                        output_signal = True
                nodes[receiver] = output_signal
                for target in network_grid[receiver]["targets"]:
                    queue.append((target, output_signal,receiver))            
    # print(f"High Signals {high_signals}")
    # print(f"Low Signals {low_signals}")
    part1 = high_signals * low_signals
    while True:
        i += 1
        # print(i)
        queue = deepcopy(network_grid["broadcaster"]["targets"])
        if i == 3929:
            print()
        while queue:
            current_node = queue.pop()
            receiver = current_node[0]
            signal_type = current_node[1]
            sender = current_node[2]
            if receiver in cycle_nodes and not signal_type:
                if receiver not in cycle_lengths:
                    cycle_lengths[receiver] = i + 1
                    cycle_nodes.remove(receiver)
            if receiver not in network_grid:
                continue
            if network_grid[receiver]["type"] == "flip_flop":
                if signal_type:
                    continue
                nodes[receiver] = not nodes[receiver]
                output_signal = nodes[receiver]
                for target in network_grid[receiver]["targets"]:
                    queue.append((target, output_signal, receiver))
            elif network_grid[receiver]["type"] == "conjunction":
                output_signal = False
                for input_source in network_grid[receiver]["input"]:
                    if not nodes[input_source]:
                        output_signal = True
                nodes[receiver] = output_signal
                for target in network_grid[receiver]["targets"]:
                    queue.append((target, output_signal,receiver))            
        if len(cycle_nodes) == 0:
            break
    part2 = (math.lcm(*cycle_lengths.values()))

    return f"Part 1: {part1}\nPart 2: {part2}"
if __name__ == "__main__":
    print(solve())