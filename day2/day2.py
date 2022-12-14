import os
from piece import Piece, Rock, Paper, Scissors
from strategy import StrategyInterface, NaiveStrategy, SecretStrategy, MathOnlyNaiveStrategy, MathOnlySecretStrategy

def points_for_tournament(lines: list[str], strategy: StrategyInterface) -> int:
	point_total = 0
	for line in lines:
		point_total += strategy.determine_point_total_from(line.strip())
	return point_total

strategy_file = open(os.path.join(os.path.dirname(__file__), "strategy.my_data"), "r")
strategy_file_lines = strategy_file.readlines()

test_lines = """A Y
B X
C Z""".splitlines()

for strategy in [NaiveStrategy(), SecretStrategy(), MathOnlyNaiveStrategy(), MathOnlySecretStrategy()]:
	print(points_for_tournament(test_lines, strategy))
	print(points_for_tournament(strategy_file_lines, strategy))
