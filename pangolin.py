class Reserve():

	asset: str
	amount: float

	def __init__(self, asset, amount):
		self.asset = asset
		self.amount = amount
	def __eq__(self, __value: object) -> bool:
		return self.asset == __value.asset and self.amount == __value.amount

class Pool():

	reserve0: Reserve
	reserve1: Reserve

	def __init__(self, reserve0: Reserve, reserve1: Reserve):
		self.reserve0 = reserve0
		self.reserve1 = reserve1

	def __eq__(self, __value: object) -> bool:
		return self.reserve0 == __value.reserve0 and self.reserve1 == __value.reserve1
	
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
		