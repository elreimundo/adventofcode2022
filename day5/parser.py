from re import search
from functools import reduce

from game import Game

def parse(input: list[str]) -> (Game, list[(int, int, int)]):
	game_builder = reduce(
		lambda builder, line:
			builder.add_move_line(line) if builder.game else
			builder.add_setup_line(line) if line.strip() else
			builder.finalize_setup(),
		input,
		GameBuilder()
	)
	return (game_builder.game, game_builder.move_commands)

def parse_setup(input: list[str]) -> Game:
	copy = input[:]
	last_line = copy.pop()
	crate_indices = [i for i in range(len(last_line)) if not (last_line[i] == ' ' or last_line[i] == "\n")]
	crates = [[] for _ in crate_indices]
	copy.reverse()
	for line in copy:
		for (crate_number, crate_string_index) in enumerate(crate_indices):
			if line[crate_string_index] != ' ':
				crates[crate_number].append(line[crate_string_index])
	return Game(crates)

MOVE_LINE_REGEXP = r"move (\d+) from (\d+) to (\d+)"

def parse_move_line(input: str) -> (int, int, int):
	groups = search(MOVE_LINE_REGEXP, input)
	return (int(groups.group(1)), int(groups.group(2)), int(groups.group(3)))	

class GameBuilder:
	def __init__(self):
		self.setup_lines = []
		self.game = None
		self.move_commands = []

	def finalize_setup(self):
		self.game = parse_setup(self.setup_lines)
		return self

	def add_setup_line(self, line: str):
		self.setup_lines.append(line)
		return self

	def add_move_line(self, line: str):
		self.move_commands.append(parse_move_line(line))
		return self
