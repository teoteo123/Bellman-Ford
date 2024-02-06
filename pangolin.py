from ast import literal_eval
import json
import requests

class Asset():
	'''
	@TODO
	'''
	def __init__(self) -> None:
		pass

class Reserve():

	asset: str
	amount: float

	def __init__(self, asset, amount):
		self.asset = asset
		self.amount = amount
	def __eq__(self, __value: object) -> bool:
		return self.asset == __value.asset and self.amount == __value.amount

class Pool():
	'''
	@TODO adapt to real pool
	'''

	reserve0: Reserve
	reserve1: Reserve

	def __init__(self, reserve0: Reserve, reserve1: Reserve):
		self.reserve0 = reserve0
		self.reserve1 = reserve1
	
	def amountOut(self, tokenIn: str, amountIn: int):
		'''
		returns the expected amount of tokens out given a proposed swap
		'''
		reserveIn = 0
		reserveOut = 0
		if self.reserve0.asset == tokenIn:
			reserveIn = self.reserve0.amount
			reserveOut = self.reserve1.amount
		elif self.reserve1.asset == tokenIn:
			reserveIn = self.reserve1.amount
			reserveOut = self.reserve0.amount
		else:
			raise ValueError("Invalid token for this pool")
		
		inWithFee = 997 * amountIn
		numerator = inWithFee * reserveOut
		denominator = reserveIn * 1000 + inWithFee
		amountOut = numerator / denominator
		return amountOut
	
	def __eq__(self, __value: object) -> bool:
		return self.reserve0 == __value.reserve0 and self.reserve1 == __value.reserve1
	
	def __str__(self) -> str:
		return "Pool(pair=[%s-%s], reserve0=%s, reserve1=%s)" % (self.reserve0.asset, self.reserve1.asset, self.reserve0.amount, self.reserve1.amount)
	
	def __hash__(self) -> int:
		hash_str = str(self.reserve0.asset) + str(self.reserve0.amount) + str(self.reserve1.asset) + str(self.reserve1.amount)
		return sum([ord(char)**i for (i, char) in zip([i for i in range(len(hash_str))], hash_str)])
	


def get_edge_weight(pool0: Pool, pool1: Pool) -> (Reserve, Reserve):
	pool0reserves = [pool0.reserve0, pool0.reserve1]
	pool1reserves = [pool1.reserve0, pool1.reserve1]
	for (i, p0reserve) in zip([0, 1], pool0reserves):
		for (j, p1reserve) in zip([0, 1], pool1reserves):
			if (p0reserve.asset == p1reserve.asset):
				ra0 = pool0reserves[(i+1) % 2].amount
				rb0 = pool0reserves[i].amount
				rb1 = pool1reserves[j].amount
				rc1 = pool1reserves[(j+1) % 2].amount
				return (rb0 * rc1) / (ra0 * rb1)
	raise ValueError("Pools %s and %s do not have an asset in common")


def getPairAddress(token0address: str, token1address: str) -> str:
	'''
	given two contract addresses, this function will return the address 
	of the pangolin pool with the two currencies as its reserves.
	'''

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
							'data': '0xe6a43905000000000000000000000000%s000000000000000000000000%s' % (token0address[2:], token1address[2:]),
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
	return '0x' + json.loads(response.content)['result'][-40:]

def getReserves(poolAddress: str) -> (int, int):
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
							'to': poolAddress, # pool address
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

	return (r0, r1)