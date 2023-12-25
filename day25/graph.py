# import networkx as nx
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
from graphviz import Graph

dot = Graph()
with open('output.txt', 'r') as file:
    for line in file.read().split("\n"):
        nodes = line.strip().split("->")
        dot.node(nodes[0])
        dot.node(nodes[1])
        dot.edge(nodes[0], nodes[1])
dot.engine = 'neato'
# dot.render('test-output/round-table.gv', view=True)
dot.render('graph')