from game import Game
from test_fixtures import starting_game, starting_instructions
from parser import parse

import os

test_game = starting_game()

test_parsed_game = parse(starting_instructions())

assert test_parsed_game == test_game

test_game.play_x_rounds(20)

assert test_game.get_monkey_business() == 10605

test_game_with_worry = starting_game(ease_worry=False)
test_game_with_worry.play_x_rounds(10000)

assert test_game_with_worry.get_monkey_business() == 2713310158

monkey_data = open(os.path.join(os.path.dirname(__file__), "monkeys.my_data"), "r").readlines()
game = parse(monkey_data)
game.play_x_rounds(20)

print(game.get_monkey_business())

worried_game = parse(monkey_data, ease_worry=False)
worried_game.play_x_rounds(10000)

print(worried_game.get_monkey_business())
