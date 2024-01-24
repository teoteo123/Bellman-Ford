

class Node():

	edges: []

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
		return "Node(value=%s edges=%s)" % (self.value, self.edges)
	
	def __eq__(self, __value: object) -> bool:
		return self.value == __value.value


'''
First node is the source node, second is dest.
                                          0.6
Edge(weight=0.6, nodes=['a', 'b']) === (a)-->(b)
'''
class Edge():

	nodes: []

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
		return "Edge((%s)---%s--->(%s))" % (self.nodes[0].value, self.weight, self.nodes[1].value)
	
'''
Collection of nodes and edges with some functions to help out
'''
class Graph():
	nodes: []
	edges: []

	def __init__(self) -> None:
		self.nodes = []
		self.edges = []

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

