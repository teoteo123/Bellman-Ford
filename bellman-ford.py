from graph import *

graph = Graph()



a = Node('a')
b = Node('b')

edge1 = Edge([a, b], 0.6)
edge2 = Edge([b, a], 0.4)

graph = Graph()
graph.add_node(a)
graph.add_node(b)
graph.add_edge(edge1)
graph.add_edge(edge2)



print(graph)
