from ast import literal_eval
import json
from graph import *
from pangolin import *
from bellman_ford import *
import requests

from pool_graph import PoolGraph

a_reserves = [5, 7, 9, 1]
b_reserves = [4, 13, 10, 7]
c_reserves = [12, 3]
d_reserves = [6,8,13]
e_reserves = [6, 2, 5]

p0 = Pool("0x0", b_reserves[0], d_reserves[0])
p1 = Pool("0x1", c_reserves[0], b_reserves[1])
p2 = Pool("0x2", a_reserves[0], c_reserves[1])
p3 = Pool("0x3", a_reserves[1], d_reserves[1])
p4 = Pool("0x4", a_reserves[2], b_reserves[2])
p5 = Pool("0x5", a_reserves[3], e_reserves[1])
p6 = Pool("0x6", b_reserves[3], e_reserves[0])
p7 = Pool("0x7", e_reserves[2], d_reserves[2])

def test_random_vals():

	nodes = [Node(value=p0), Node(value=p1), Node(value=p2), Node(value=p3), Node(value=p4), Node(value=p5), Node(value=p6), Node(value=p7)]

	graph = Graph()
	for i in range(7):
			for j in range(i+1, 8):
				try:
					edge = Edge([nodes[i], nodes[j]], get_edge_weight(nodes[i].value, nodes[j].value))
					graph.add_edge(edge)
					edge = Edge([nodes[j], nodes[i]], get_edge_weight(nodes[j].value, nodes[i].value))
					graph.add_edge(edge)
				except:
					pass


	bellman_ford(graph, start_node=nodes[3])

def test_two_nodes():
	twoNodes = [Node(p3), Node(p7)]
	newEdges = [Edge([twoNodes[0], twoNodes[1]], get_edge_weight(twoNodes[0].value, twoNodes[1].value)), Edge([twoNodes[1], twoNodes[0]], get_edge_weight(twoNodes[1].value, twoNodes[0].value))]
	twoGraph = Graph()
	[twoGraph.add_edge(e) for e in newEdges]

	bellman_ford(twoGraph, start_node=twoNodes[1])
	bellman_ford(twoGraph, start_node=twoNodes[0])

def test_getPair():
	infura_url = 'https://avalanche-mainnet.infura.io/v3/d1e7d4e46bba461cb67651a8c5d508b8'
	headers = {
    'Content-Type': 'application/json',
	}

	json_data = {
			'jsonrpc': '2.0',
			'method': 'eth_call',
			'params': [
					{
							'from': '0xBd14F2b9813b23AF7e38C979EaDfaF17C049bEA5',
							'to': '0xefa94DE7a4656D787667C749f7E1223D71E9FD88',
							'data': '0xe6a43905000000000000000000000000B97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E000000000000000000000000B31f66AA3C1e785363F0875A1B74E27b85FD66c7',
					},
					'latest',
			],
			'id': 1,
	}

	response = requests.post(
			infura_url,
			headers=headers,
			json=json_data,
	)
	print('0x' + json.loads(response.content)['result'][-40:])
# test_getPair()

def test_getReserves():
	infura_url = 'https://avalanche-mainnet.infura.io/v3/d1e7d4e46bba461cb67651a8c5d508b8'
	headers = {
    'Content-Type': 'application/json',
	}

	json_data = {
			'jsonrpc': '2.0',
			'method': 'eth_call',
			'params': [
					{
							'from': '0xBd14F2b9813b23AF7e38C979EaDfaF17C049bEA5',
							'to': '0x0e0100ab771e9288e0aa97e11557e6654c3a9665', # pool address
							'data': '0x0902f1ac', # getReserves function selector
					},
					'latest',
			],
			'id': 1,
	}

	response = requests.post(
			infura_url,
			headers=headers,
			json=json_data,
	)
	result = json.loads(response.content)['result'][2:]
	r0 = literal_eval('0x' + result[:64][-28:])
	r1 = literal_eval('0x' + result[64:128][-28:])


	print(str(r0) + '\n' + str(r1))
# test_getReserves()

# print(getPairAddress('0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E', '0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7'))
# print(getTokenAddresses('0x0e0100ab771e9288e0aa97e11557e6654c3a9665'))



pg = PoolGraph()

pg.refresh_nodes_edges()
# why broken?
bellman_ford(pg.graph, pg.graph.nodes[0])
bellman_ford(pg.graph, pg.graph.nodes[3])