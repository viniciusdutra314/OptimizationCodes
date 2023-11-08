import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
durations=np.loadtxt('duracoes.txt')
G=nx.Graph(durations)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.savefig('graph_view',dpi=400)