# Python program to plot activity network

# Author : Suman Sahu
# 		   712CS2151

# Code to be compiled in python3.x
# Required packages python3-tk, matplotlib

import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()
no_tasks = int(input())
# g.add_nodes_from(list(range(no_tasks+2)))
edge_list = []
node_list = []

for i in range(no_tasks+2):
	temp = []
	[a,b] = str(input()).split(' ')
	temp.append(a)
	g.add_node(a)
	temp.append(b)
	node_list.append(temp)

for i in range(no_tasks+2):
	temp = []
	[a,b] = str(input()).split(' ')
	temp.append(node_list[int(a)][0])
	temp.append(node_list[int(b)][0])
	edge_list.append(temp)


# g.add_nodes_from([])
g.add_edges_from(edge_list)
pos = nx.spring_layout(g)
nx.draw(g, pos, node_size=1500, with_labels=True)
plt.show()