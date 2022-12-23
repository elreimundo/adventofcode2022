import os

from parser import parse
from test_fixtures import test_lines
from topography import Position
from ordered_set import ImmutableOrderedSet

topography_lines = open(os.path.join(os.path.dirname(__file__), "topography.my_data"), "r").readlines()

test_pathfinder = parse(test_lines())

test_pathfinder.explore()

assert test_pathfinder.get_path_length() == 31

pathfinder = parse(topography_lines)

pathfinder.explore()

current_min_path_length = pathfinder.get_path_length()

print(current_min_path_length)

for position in pathfinder.topography.positions_with_height('a'):
	copy = pathfinder.copy_with_starting_point(position)
	copy.explore()
	path_length = copy.get_path_length()
	if path_length < current_min_path_length:
		current_min_path_length = path_length

print(current_min_path_length)