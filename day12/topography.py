class Vector:
	def __init__(self, row_offset, col_offset):
		self.row_offset = row_offset
		self.col_offset = col_offset

CARDINAL_DIRECTIONS: list[Vector] = [
	Vector(1, 0),
	Vector(-1, 0),
	Vector(0, 1),
	Vector(0, -1)
]

class Position:
	def __init__(self, row, col):
		self.row = row
		self.col = col

	def move(self, vector: Vector):
		return Position(self.row + vector.row_offset, self.col + vector.col_offset)

	def __repr__(self) -> str:
		return f'({self.row}, {self.col})'

	def __eq__(self, other):
		return self.row == other.row and self.col == other.col

	def __hash__(self):
		return hash((self.row, self.col))

class Topography:
	def __init__(self, matrix: list[list[int]]):
		self.matrix = matrix

	def at(self, position: Position) -> int:
		return self.matrix[position.row][position.col] if (
			position.row >= 0
			and position.col >= 0
			and position.row < self.row_count()
			and position.col < self.col_count(position.row)
		) else None

	def row_count(self) -> int:
		return len(self.matrix)

	def col_count(self, row: int) -> int:
		return len(self.matrix[row])

	def can_access(self, position1: Position, position2: Position):
		current_value = self.at(position1)
		target_value = self.at(position2)
		return current_value is not None and target_value is not None and target_value <= current_value + 1

	def positions_available_from(self, position: Position) -> list[Position]:
		available_positions = []
		for vector in CARDINAL_DIRECTIONS:
			position_to_check = position.move(vector)
			if self.can_access(position, position_to_check):
				available_positions.append(position_to_check)
		return available_positions

	def positions_with_height(self, height) -> list[Position]:
		if type(height) is str:
			return self.positions_with_height(ord(height))
		positions = []
		for row_index in range(self.row_count()):
			for col_index in range(self.col_count(row_index)):
				position = Position(row_index, col_index)
				if self.at(position) == height:
					positions.append(position)
		return positions
