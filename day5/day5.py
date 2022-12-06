import os

from game import Game
from parser import parse

from functools import reduce

def test_fixtures() -> str:
	return """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def test_crates() -> list[list[str]]:
	return [
		['Z', 'N'],
		['M', 'C', 'D'],
		['P']
	]

def test_moves() -> list[(int, int, int)]:
	return [
		(1,2,1),
		(3,1,3),
		(2,2,1),
		(1,1,2)
	]

def test_game() -> Game:
	return Game(test_crates())

game, moves = parse(test_fixtures().splitlines())
assert game == test_game()
assert moves == test_moves()

def get_final_boxes(game: Game, moves: list[(int, int, int)]) -> str:
	return ''.join([
		crate[-1] for crate in reduce(
			lambda game_state, move: game_state.move(*move),
			moves,
			game.copy()
		).crates
	])

def get_final_chunked_boxes(game: Game, moves: list[(int, int, int)]) -> str:
	return ''.join([
		crate[-1] for crate in reduce(
			lambda game_state, move: game_state.move_chunk(*move),
			moves,
			game.copy()
		).crates
	])

crates_file = open(os.path.join(os.path.dirname(__file__), "crates.my_data"), "r")
crates_file_lines = crates_file.readlines()

actual_game, actual_moves = parse(crates_file_lines)

print(get_final_boxes(actual_game, actual_moves))
print(get_final_chunked_boxes(actual_game, actual_moves))
