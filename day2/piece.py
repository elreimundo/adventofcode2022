class Piece:
	# we define `would_beat` and `would_lose_to` as "by reference" lambdas so that
	# Rock can be defined as "beating" Scissors and "losing to" Paper
	# even before the Scissors and Paper singletons have been defined.
	# note that we can't provide a type hint here because the Piece type
	# only gets defined in its entirety once the class has finished loading
	def __init__(self, value: int, would_beat, would_lose_to):
		self.value = value
		self.would_beat = would_beat
		self.would_lose_to = would_lose_to

Rock = Piece(1, would_beat=lambda: Scissors, would_lose_to=lambda: Paper)
Paper = Piece(2, would_beat=lambda: Rock, would_lose_to=lambda: Scissors)
Scissors = Piece(3, would_beat=lambda: Paper, would_lose_to=lambda: Rock)