import os

from landscape import Landscape, Position, Vector, CARDINAL_DIRECTIONS
from parser import parse
from visibility import EdgeVisibility, ScenicVisibility

def test_fixtures() -> list[str]:
	return """30373
25512
65332
33549
35390""".splitlines()

test_trees = parse(test_fixtures())
test_edge_visibility = EdgeVisibility(test_trees)
print(test_edge_visibility.count_visible())

trees = parse(open(os.path.join(os.path.dirname(__file__), "trees.my_data"), "r").readlines())
edge_visibility = EdgeVisibility(trees)

print(edge_visibility.count_visible())

test_scenic_visibililty = ScenicVisibility(test_trees)

assert test_scenic_visibililty.maximum_scenic_score() == 8

print(ScenicVisibility(trees).maximum_scenic_score())