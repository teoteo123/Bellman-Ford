from graph import *
from pangolin import *

a_reserves = [Reserve('a', 5), Reserve('a', 7), Reserve('a', 9), Reserve('a', 1)]
b_reserves = [Reserve('b', 4), Reserve('b', 13), Reserve('b', 10), Reserve('b', 7)]
c_reserves = [Reserve('c', 12), Reserve('c', 3)]
d_reserves = [Reserve('d', 6), Reserve('d', 8), Reserve('d', 13)]
e_reserves = [Reserve('e', 6), Reserve('e', 2), Reserve('e', 5)]

p0 = Pool(b_reserves[0], d_reserves[0])
p1 = Pool(c_reserves[0], b_reserves[1])
p2 = Pool(a_reserves[0], c_reserves[1])
p3 = Pool(a_reserves[1], d_reserves[1])
p4 = Pool(a_reserves[2], b_reserves[2])
p5 = Pool(a_reserves[3], e_reserves[1])
p6 = Pool(b_reserves[3], e_reserves[0])
p7 = Pool(e_reserves[2], d_reserves[2])


nodes = [Node(value=p0), Node(value=p1), Node(value=p2), Node(value=p3), Node(value=p4), Node(value=p5), Node(value=p6), Node(value=p7)]

edges = []
for i in range(7):
		for j in range(i, 7):
			try:
				edges.append(Edge([nodes[i], nodes[j]], get_edge_weight(nodes[i].value, nodes[j].value)))
			except:
				pass
			try:
				edges.append(Edge([nodes[7-i], nodes[7-j]], get_edge_weight(nodes[7-i].value, nodes[7-j].value)))
			except:
				pass

g = Graph(nodes, edges)

print(g)


# def bellman_ford(graph: Graph):

