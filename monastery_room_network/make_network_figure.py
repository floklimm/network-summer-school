import numpy as np
import networkx as nx
import matplotlib.pyplot as pl

def get_pos(G, labels,iterations=200):
    new_G = G.copy()
    new_G.add_edges_from([ (a,'_'+b) for a,b in labels.items()])
    lab_vals = set(['_'+b for b in labels.values()])
    labels_reversed = { b: a for a,b in labels.items() }

    label_pos = {}
    pos = nx.drawing.layout.spring_layout(new_G, iterations=iterations)
    for n in lab_vals:
        position = pos.pop(n)
        l = labels_reversed[n[1:]]
        label_pos[n[1:]] = position

    return pos, label_pos

G = nx.read_graphml('./monastery_room_network.graphml')

#pos = nx.drawing.layout.spring_layout(G, iterations=2000)
labels = {
        'Y': 'Y',
        'E': 'E',
        'A35': 'A35',
        }
pos, label_pos = get_pos(G,labels,iterations=2000)
#pos = nx.drawing.layout.spectral_layout(G)

d = { n: G.degree(n) for n in G.nodes()}

colors = { 
        'Y': np.array((148,0,211.))/255.,
        'N1': np.array((144,238,144.))/255.,
        'N2': np.array((144,238,144.))/255.,
        'E': np.array((144,238,144.))/255.,
        'W': np.array((144,238,144.))/255.,
        'S': np.array((144,238,144.))/255.,
        'A35': np.array((200,10,10))/255.,
     }

fig, ax = pl.subplots(1,1)
nx.draw_networkx_edges(
        G, 
        pos=pos, 
        edge_color='grey',
        ax=ax,
        mew=1,
        )
ax.axis('equal')
ax.axis('off')

for l in label_pos.keys():
    x = [ label_pos[l][0], pos[l][0] ]
    y = [ label_pos[l][1], pos[l][1] ]
    ax.plot(x,y,':k',lw=1)
    ax.plot(x[:-1],y[:-1],
            'w',
            marker='o',
            mew=0,
            mfc='w',
            alpha=1,
            ms=15,
            )

for n in G.nodes():

    if n not in colors:
        col = 'w'
        label = ''
    else:
        col = colors[n]
        label = n

    if n == 'A35':
        label = 'A35'

    if n in label_pos:
        ax.text(label_pos[n][0],
                label_pos[n][1],
                label,
                family = 'Arial',
                fontsize='medium',
                #backgroundcolor = 'w',
                ha='center',
                va='center',
                )

    ax.plot([pos[n][0]],[pos[n][1]],
            marker = 'o',
            markersize = np.sqrt(8*d[n]),
            color = col,
            mec = 'k',
            mew = 1,
            )
    
"""
nx.draw_networkx_nodes(
        G, 
        pos=pos, 
        node_size=d*10,
        linewidths=2.0,
        node_color='w',
        mec='k',
        mew=10.0,
        ax=ax,
        )
"""

B = nx.betweenness_centrality(G)


B_ = sorted([(a,b) for a,b in B.items()],key=lambda x: -x[1])

for n,b in B_:
    print n, b

fig.savefig('./monastery_network.pdf')

pl.show()
#print G.relabel_node('A0','Yard')

