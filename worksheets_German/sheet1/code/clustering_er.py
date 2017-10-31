# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 13:10:39 2016

@author: Florian
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

p_vec=np.linspace(0,1,100)
n=100
clustering_out=[]

for p in p_vec:
    # create a random network of this size
    ER=nx.erdos_renyi_graph(n, p, seed=1, directed=False)
    # Compute clustering
    c=nx.clustering(ER)
    # save it
    clustering_out.append(np.mean(c.values()))
    
plt.plot(p_vec,clustering_out)