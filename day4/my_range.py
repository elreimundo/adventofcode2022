class Range:
	def __init__(self, min: int, max: int):
		self.min = min
		self.max = max

	def contains(self, other) -> bool:
		return self.max >= other.min and self.min <= other.max

	def fully_contains(self, other) -> bool:
		return self.min <= other.min and self.max >= other.max

	def __repr__(self):
		return f'Range({self.min}-{self.max})'
