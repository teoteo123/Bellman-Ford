from graph import *





def bellman_ford(graph: Graph, start_node: Node):
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

	print("Start: " + start_node.value.reserve0.asset + "/" + start_node.value.reserve1.asset + "\n\t" + "\n\t".join([k.value.reserve0.asset + "/" + k.value.reserve1.asset + ": " + str(v) for k, v in distances.items()]))

