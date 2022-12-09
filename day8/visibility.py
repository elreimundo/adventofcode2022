from landscape import Landscape, Position, Vector, CARDINAL_DIRECTIONS

from functools import reduce

class EdgeVisibility:
	def __init__(self, landscape: Landscape):
		self.landscape = landscape

	def count_visible(self):
		current_count = 0
		for position in self.landscape.positions():
			if self.is_visible_from_edge(position):
				current_count += 1
		return current_count

	def is_visible_from_edge(self, position: Position):
		for vector in CARDINAL_DIRECTIONS:
			if (self.check_visibility(position, position.move(vector), vector)):
				return True
		return False

	def check_visibility(self, original_position: Position, next_position: Position, vector: Vector):
		match self.landscape.at(next_position):
			case None: return True # at the edge
			case blocked if blocked >= self.landscape.at(original_position): return False
			case _: return self.check_visibility(original_position, next_position.move(vector), vector)

class ScenicVisibility:
	def __init__(self, landscape: Landscape):
		self.landscape = landscape

	def maximum_scenic_score(self):
		current_max = 0
		for position in self.landscape.positions():
			score = self.scenic_score(position)
			if score > current_max:
				current_max = score
		return current_max

	def scenic_score(self, position: Position) -> int:
		return reduce(
			lambda a, b: a * b,
			[
				self.scenic_score_in_direction(position, position.move(vector), vector, 0)
				for vector in CARDINAL_DIRECTIONS
			]
		)

	def scenic_score_in_direction(self, original_position: Position, next_position: Position, vector: Vector, distance: int):
		match self.landscape.at(next_position):
			case None: return distance
			case blocked if blocked >= self.landscape.at(original_position): return distance + 1
			case _: return self.scenic_score_in_direction(original_position, next_position.move(vector), vector, distance + 1)

