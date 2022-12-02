from piece import Piece, Rock, Paper, Scissors

# abstract class for a strategy
class StrategyInterface:
	# we know a priori how the input representing their piece (A/B/C) gets converted
	def convert_to_their_piece(self, input: str) -> Piece:
		match input:
			case "A": return Rock
			case "B": return Paper
			case "C": return Scissors
			case _: raise Exception("unexpected input: " + input)

	# we know the rules for RPS
	def points_for_game(self, opponent_guess: Piece, my_guess: Piece) -> int:
		if (my_guess.would_beat() == opponent_guess):
			return 6
		elif (my_guess.would_lose_to() == opponent_guess):
			return 0
		else:
			return 3

	# we know how that the points are (points for a win/draw) + (points for our guess)
	def determine_point_total_from(self, line: str) -> int:
		opponent_guess = self.convert_to_their_piece(line[0])
		my_guess = self.determine_my_piece(opponent_guess, line[2])
		return self.points_for_game(opponent_guess, my_guess) + my_guess.value

	# the only difference is what the X/Y/Z mean
	def determine_my_piece(self, opponent_guess, input: str): pass

class NaiveStrategy(StrategyInterface):
	def determine_my_piece(self, opponent_guess: Piece, input: str) -> Piece:
		match input:
			case "X": return Rock
			case "Y": return Paper
			case "Z": return Scissors
			case _: raise Exception("unexpected input: " + input)

class SecretStrategy(StrategyInterface):
	def determine_my_piece(self, opponent_guess: Piece, input: str) -> Piece:
		match input:
			case "X": return opponent_guess.would_beat()
			case "Y": return opponent_guess
			case "Z": return opponent_guess.would_lose_to()
			case _: raise Exception("unexpected input: " + input)