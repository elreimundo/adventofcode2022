class Game:
	def __init__(self, crates: list[list[str]]):
		self.crates = crates

	def move(self, count: int, source: int, destination: int): # Game
		if (count > 0):
			self.crates[destination - 1].append(self.crates[source - 1].pop())
			return self.move(count - 1, source, destination)
		return self

	def move_chunk(self, count: int, source: int, destination: int): #Game
		source_index = source - 1
		chunk = self.crates[source_index][-count:]
		self.crates[source_index] = self.crates[source_index][:-count]
		self.crates[destination - 1] += chunk
		return self

	def __eq__(self, other) -> bool:
		return self.crates == other.crates

	def copy(self):
		return Game([
			[
				el for el in crate
			] for crate in self.crates
		])
