import numpy as np
import networkx as nx
import matplotlib.pyplot as pl

G = nx.read_edgelist('./monastery_room_network.txt')

mapping = {
        'O' : 'E',
        'A0': 'Y',
        'CB1': 'C43',
        'CB2': 'C44',
        'CB3': 'C45',
        'CB4': 'C46',
        'CB5': 'C47',
        'CB6': 'C48',
        'CB7': 'C49',
        'CB8': 'C50',
        'CB9': 'C51',
        'CB10': 'C52',
        'BF1': 'B29',
        'BF2': 'B30',
        'BF3': 'B31',
        'BF4': 'B32',
        }

G = nx.relabel_nodes(G,mapping)

nx.write_graphml(G,'./monastery_room_network.graphml')
nx.write_edgelist(G,'./monastery_room_network.edgelist')

