from graph import *





def bellman_ford(g: Graph, start_node: Node):
	distances = {node: float('inf') for node in g.nodes}
	distances[start_node] = 1
	predecessors = {node: None for node in g.nodes}
	# relax edges... tf?
	for _ in range(len(g.nodes) - 1):
			for edge in g.edges:
				u = edge.nodes[0]
				v = edge.nodes[1]
				weight = edge.weight
				if distances[u] * weight < distances[v]:
					distances[v] = distances[u] * weight
					predecessors[v] = u

	print("Start: " + start_node.value.reserve0.asset + "/" + start_node.value.reserve1.asset + "\n\t" + "\n\t".join([k.value.reserve0.asset + "/" + k.value.reserve1.asset + ": " + str(v) for k, v in distances.items()]))

