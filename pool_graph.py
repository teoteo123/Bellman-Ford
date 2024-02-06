


from graph import *
from pangolin import *


class PoolGraph():

	graph: Graph
	
	def __init__(self):
		pools_dict = load_pools()
		nodes = []

		for k, v in pools_dict.items():
			p = Node(Pool(k, v['t0']['reserve'], v['t1']['reserve'], v['t0']['address'], v['t1']['address'], v['t0']['symbol'], v['t1']['symbol']))
			nodes.append(p)
		graph = Graph()

		for i in range(len(nodes) - 1):
				for j in range(i+1, len(nodes)):
					try:
						edge = Edge([nodes[i], nodes[j]], get_edge_weight(nodes[i].value, nodes[j].value))
						graph.add_edge(edge)
						edge = Edge([nodes[j], nodes[i]], get_edge_weight(nodes[j].value, nodes[i].value))
						graph.add_edge(edge)
					except:
						pass
		
		self.graph = graph


	def refresh_nodes_edges(self):
		new_nodes = []
		for node in self.graph.nodes:
			pool_address = node.value.address
			(node.value.reserve0, node.value.reserve1) = getReserves(pool_address)
			new_nodes.append(node)
		
		graph = Graph()

		for i in range(len(new_nodes) - 1):
				for j in range(i+1, len(new_nodes)):
					try:
						edge = Edge([new_nodes[i], new_nodes[j]], get_edge_weight(new_nodes[i].value, new_nodes[j].value))
						graph.add_edge(edge)
						edge = Edge([new_nodes[j], new_nodes[i]], get_edge_weight(new_nodes[j].value, new_nodes[i].value))
						graph.add_edge(edge)
					except:
						pass
		
		self.graph = graph
