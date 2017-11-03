# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx

# import the function path_graph from the file pathgraph.py
from pathgraph import path_graph

# calls the path_graph function
# afterwards the varibale path10
# contains the adjacency matrix
# of a P_10 graph
path10 = path_graph(10)

# convert matrix to a networkx graph
G = nx.from_numpy_matrix(pfad10)

# draw the graph
nx.draw(G)
