from graph import *





def bellman_ford(graph: Graph, start_node: str):
	distances = {node: float('inf') for node in graph.nodes}
	distances[start_node] = 0
	predecessors = {node: None for node in graph.nodes}
	# relax edges... tf?
	for _ in range(len(graph.nodes)):
		for u in graph.nodes:
			for edge in u.edges:
				v = edge.nodes[1]
				weight = edge.weight
				if distances[u] + weight < distances[v]:
					distances[v] = distances[u] + weight
					predecessors[v] = u

		# Check for negative cycles... works sorta i think
		# @TODO test with real rates
		for u in graph.nodes:
			for edge in u.edges:
				v = edge.nodes[1]
				weight = edge.weight
				if distances[u] + weight < distances[v]:
					print("Negative cycle: " + str(v) + "\n" + '\n'.join([str(edge) for edge in v.edges]))

