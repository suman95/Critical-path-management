# Python program to plot activity network

# Author : Suman Sahu
# 		   712CS2151

# Code to be compiled in python3.x
# Required packages python3-tk, matplotlib

# import matplotlib.pyplot as plt
# import networkx as nx
from graphviz import Digraph

g = Digraph("Critical path")
g.body.extend(['rankdir=LR', 'size="8,5"'])
g.attr('node', shape='box')
no_tasks = int(input())
# g.add_nodes_from(list(range(no_tasks+2)))
edge_list = []
node_list = []

for i in range(no_tasks+2):
	temp = []
	[a,b] = str(input()).split(' ')
	temp.append(a)
	#g.add_node(a)
	g.node(str(a),str(a))
	temp.append(b)
	# g.node(str(b),str(b))
	node_list.append(temp)

while True:
	temp = []
	k = str(input())
	if(k=='quit'):
		break
	[a,b] = k.split(' ')	
	# g.edge(node_list[int(a)][0],node_list[int(b)][0])
	temp.append(a)
	temp.append(b)
	edge_list.append(temp)

temp = str(input()).strip()
temp = temp.split(' ')
comp = []
print(temp)
for x in range(1,len(temp)):
	# g.re
	g.edge(node_list[int(temp[x-1])][0],node_list[int(temp[x])][0], color='red')
	te2 = []
	te2.append(temp[x-1])
	te2.append(temp[x])
	comp.append(te2)

for x in edge_list:
	if x not in comp: 
		[a,b] = x
		g.edge(node_list[int(a)][0],node_list[int(b)][0])
# g.add_nodes_from([])
# g.add_edges_from(edge_list)
# pos = nx.spring_layout(g)
# nx.draw(g, pos, node_size=1500, with_labels=True)
# plt.show()

g.view()