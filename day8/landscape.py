from typing import Generator

class Vector:
	def __init__(self, row_offset: int, col_offset: int):
		self.row_offset = row_offset
		self.col_offset = col_offset

CARDINAL_DIRECTIONS: list[Vector] = [
	Vector(1, 0),
	Vector(-1, 0),
	Vector(0, 1),
	Vector(0, -1)
]

class Position:
	def __init__(self, row: int, col: int):
		self.row = row
		self.col = col

	def move(self, vector: Vector):
		return Position(self.row + vector.row_offset, self.col + vector.col_offset)

class Landscape:
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

	def positions(self) -> Generator[Position, None, None]:
		for row_index in range(self.row_count()):
			for col_index in range(self.col_count(row_index)):
				yield Position(row_index, col_index)
