# import numpy as np
# import matplotlib.pyplot as plt
# # Open the text file
# with open('output.txt', 'r') as f:
#     # Read the lines of the file
#     lines = f.read().split("\n")

# # Create a directed graph
# G = nx.DiGraph()

# # Iterate over the lines of the file
# for line in lines:
#     # Split the line into two nodes
#     nodes = line.strip().split('->')

#     # Add the nodes to the graph
#     G.add_node(nodes[0])
#     G.add_node(nodes[1])

#     # Add an edge between the nodes
#     G.add_edge(nodes[0], nodes[1])


# nx.draw(G, pos=)
# plt.show()

