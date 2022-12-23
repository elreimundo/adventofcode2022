from pathfinder import DijkstraPathfinder
from topography import Topography, Position
from ordered_set import ImmutableOrderedSet

class TopographyBuilder:
	def __init__(self):
		self.matrix = []

	def add_at_position(self, value: int, position: Position):
		if position.row >= len(self.matrix):
			self.matrix.insert(position.row, [])
		self.matrix[position.row].insert(position.col, value)

	def build(self) -> Topography:
		return Topography(self.matrix)

class PathfinderBuilder:
	def __init__(self):
		self.start_position = None
		self.end_position = None
		self.topography_builder = TopographyBuilder()

	def build(self) -> DijkstraPathfinder:
		return DijkstraPathfinder(self.topography_builder.build(), self.end_position, self.start_position)

def parse(lines: list[str]) -> DijkstraPathfinder:
	builder = PathfinderBuilder()
	for row_index, line in enumerate(lines):

		for col_index, character in enumerate(line.strip()):
			position = Position(row_index, col_index)
			match character:
				case 'S':
					builder.start_position = position
					builder.topography_builder.add_at_position(ord('a'), position)
				case 'E':
					builder.end_position = position
					builder.topography_builder.add_at_position(ord('z'), position)
				case _:
					builder.topography_builder.add_at_position(ord(character), position)
	return builder.build()
