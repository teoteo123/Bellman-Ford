

class Node():

	edges: []
	value: any

	def __init__(self, value):
		self.value = value
		self.edges = []

	def get_edges(self):
		return self.edges
	
	def add_edge(self, edge):
		if edge not in self.edges:
			self.edges.append(edge)

	def remove_edge(self, edge):
		if (edge in self.edges):
			self.edges.remove(edge)
	
	def __str__(self) -> str:
		return "Node(value=%s edges=%s)" % (self.value, "".join(['\n\t' + str(edge.weight) + '  ' + str(edge.nodes[1].value) for edge in self.edges]))
	
	def __eq__(self, __value: object) -> bool:
		return self.value == __value.value
	
	def __hash__(self) -> int:
		return self.value.__hash__()


'''
First node is the source node, second is dest.
                                          0.6
Edge(weight=0.6, nodes=['a', 'b']) === (a)-->(b)
'''
class Edge():

	nodes: []
	weight: float

	def __init__(self, nodes, weight):
		self.nodes = nodes
		self.weight = weight

	def nodes(self): return self.nodes

	def src(self):
		return self.nodes[0]
	
	def dest(self):
		return self.nodes[1]
	
	def update_weight(self, weight: float):
		self.weight = weight

	def update_dest(self, node: Node):
		self.nodes.pop()
		self.nodes.append(node)

	def __eq__(self, __value: object) -> bool:
		return self.nodes == __value.nodes

	def __str__(self) -> str:
		return "Edge((%s)---[%s]--->(%s))" % (self.nodes[0].value, self.weight, self.nodes[1].value)
	
'''
Collection of nodes and edges with some functions to help out
To traverse graph, iterate nodes and look for neighboring nodes via their edges
'''
class Graph():
	nodes: []
	edges: []

	def __init__(self, nodes, edges) -> None:
		if (nodes != None):
			self.nodes = nodes
		else:
			self.nodes = []
		
		self.edges = []
		if (self.edges != None):
			for edge in edges:
				self.add_edge(edge)

	def add_node(self, node: Node):
		self.nodes.append(node)

	# Works like adding to a set
	def add_edge(self, edge: Edge):
		if edge not in self.edges:
			
			self.edges.append(edge)
			edge.nodes[0].add_edge(edge)

			for node in edge.nodes:
				if node not in self.nodes:
					self.nodes.append(node)
			

	def get_head(self):
		return self.nodes[0]
	
	def get_node(self, value):
		for node in self.nodes:
			if node.value == value:
				return node
	
	def __str__(self) -> str:
		strings = []
		for edge in self.edges:
			strings.append(str(edge))
		
		return '\n'.join(strings)

