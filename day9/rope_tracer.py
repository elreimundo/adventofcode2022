from rope import Rope, Position, Vector

class RopeTracer:
	def __init__(self, rope = Rope()):
		self.rope = rope
		self.tail_positions = set()

	def move(self, vector: Vector):
		while not vector.is_zero():
			this_move = vector.unit_like()
			vector = vector.minus(this_move)

			rope = self.rope.move(this_move)
			self.tail_positions.add(rope.tail_position)
			self.rope = rope

	def multi_move(self, vectors: list[Vector]):
		for vector in vectors:
			self.move(vector)
