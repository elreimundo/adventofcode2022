from topography import Topography, Position
from ordered_set import ImmutableOrderedSet, MutableOrderedSet

from math import inf

class BFSPathfinder:
	def __init__(self, topography: Topography, destination: Position, path: ImmutableOrderedSet[Position]):
		self.topography = topography
		self.destination = destination
		self.path = path

	def has_visited(self, position: Position):
		return self.path.contains(position)

	def visit(self, position):
		return Pathfinder(
			self.topography,
			self.destination,
			self.path.add(position)
		)

	def explore(self):
		last_position = self.path[-1]
		pathfinder = None
		for available_position in self.topography.positions_available_from(last_position):
			if available_position == self.destination:
				return self.visit(available_position)
			if not self.has_visited(available_position):
				possible_path = self.visit(available_position).explore()
				if possible_path is not None and (pathfinder is None or len(possible_path.path) < len(pathfinder.path)):
					pathfinder = possible_path
		return pathfinder

class DijkstraNode:
	def __init__(self, distance: int = inf, previous_position: Position = None, visited: bool = False):
		self.distance = distance
		self.previous_position = previous_position
		self.visited = visited

	def __repr__(self) -> str:
		return f'{"Visited" if self.visited else "Unvisited"}({self.distance})'

class DijkstraPathfinder:
	def __init__(self, topography: Topography, destination: Position, starting_point: Position):
		self.topography = topography
		self.destination = destination
		self.starting_point = starting_point
		self.nodes = [[DijkstraNode() for _ in row] for row in topography.matrix]
		self.positions_to_visit = MutableOrderedSet()

	def copy_with_starting_point(self, starting_point: Position):
		return DijkstraPathfinder(self.topography, self.destination, starting_point)

	def at(self, position: Position) -> int:
		return self.nodes[position.row][position.col] if (
			position.row >= 0
			and position.col >= 0
			and position.row < self.row_count()
			and position.col < self.col_count(position.row)
		) else None

	def row_count(self) -> int:
		return len(self.nodes)

	def col_count(self, row: int) -> int:
		return len(self.nodes[row])

	def visit(self, position: Position):
		node = self.at(position)
		distance = node.distance + 1
		for available_position in self.topography.positions_available_from(position):
			next_node = self.at(available_position)
			if next_node is not None and not next_node.visited:
				self.positions_to_visit.add(available_position)
				if distance < next_node.distance:
					next_node.previous_position = position
					next_node.distance = distance
		node.visited = True

	def explore(self):
		self.at(self.starting_point).distance = 0
		self.visit(self.starting_point)
		while len(self.positions_to_visit) > 0:
			position = self.positions_to_visit.pop(0)
			self.visit(position)

	def get_path_length(self):
		return self.at(self.destination).distance

	def get_full_path(self):
		path = [self.destination]
		while path[0].previous_position is not None:
			path.insert(0, path[0].previous_position)
		return path
