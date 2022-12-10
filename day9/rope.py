class Vector:
	def __init__(self, row_offset: int, col_offset: int):
		self.row_offset = row_offset
		self.col_offset = col_offset

	def unit_like(self):
		return Vector(self.unit_preserving_sign(self.row_offset), self.unit_preserving_sign(self.col_offset))

	def is_unit_like(self):
		return (
			self.unit_preserving_sign(self.row_offset) == self.row_offset and
			self.unit_preserving_sign(self.col_offset) == self.col_offset
		)

	def is_zero(self):
		return self.row_offset == 0 and self.col_offset == 0

	def minus(self, other):
		return Vector(self.row_offset - other.row_offset, self.col_offset - other.col_offset)

	def unit_preserving_sign(self, value: int):
		match value:
			case positive if positive > 0: return 1
			case negative if negative < 0: return -1
			case 0: return 0

class Position:
	def __init__(self, row: int, col: int):
		self.row = row
		self.col = col

	def move(self, vector: Vector):
		return Position(self.row + vector.row_offset, self.col + vector.col_offset)

	def minus(self, other) -> Vector:
		return Vector(self.row - other.row, self.col - other.col)

	# override eq and hash so we can keep track of positions in a set
	def __eq__(self, other):
		return self.row == other.row and self.col == other.col

	def __hash__(self):
		return hash((self.row, self.col))

	def __repr__(self):
		return f'({self.row}, {self.col})'

	@staticmethod
	def zero():
		return Position(0, 0)

class Rope:
	def __init__(self, head_position = Position.zero(), tail_position = Position.zero()):
		self.head_position = head_position
		self.tail_position = tail_position

	def move(self, vector: Vector):
		new_head_position: Position = self.head_position.move(vector)
		new_tail_position: Position = self.tail_position.move(
			self.pull_vector(new_head_position, self.tail_position)
		)
		return Rope(new_head_position, new_tail_position)

	def pull_vector(self, position1: Position, position2: Position):
		vector = position1.minus(position2)
		return Vector(0, 0) if vector.is_unit_like() else vector.unit_like()

class LinkedRope(Rope):
	def __init__(self, ropes: list[Rope]):
		self.ropes = ropes
		self.head_position = ropes[0].head_position
		self.tail_position = ropes[-1].tail_position

	def move(self, vector: Vector):
		new_ropes = []
		for rope in self.ropes:
			next_rope = rope.move(vector)
			vector = next_rope.tail_position.minus(rope.tail_position)
			new_ropes.append(next_rope)
		return LinkedRope(new_ropes)

	@staticmethod
	def with_length(length: int):
		return LinkedRope([Rope() for i in range(length)])