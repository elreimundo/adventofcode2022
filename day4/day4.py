import os
from parser import parse

ranges_file = open(os.path.join(os.path.dirname(__file__), "ranges.my_data"), "r")
ranges_file_lines = ranges_file.readlines()

def find_total_overlaps(input: list[str]) -> int:
	count = 0
	for line in input:
		(left, right) = parse(line)
		if left.fully_contains(right) or right.fully_contains(left):
			count += 1
	return count

def test_fixtures() -> list[str]:
	return """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()

assert find_total_overlaps(test_fixtures()) == 2

print(find_total_overlaps(ranges_file_lines))

def find_partial_overlaps(input: list[str]) -> int:
	count = 0
	for line in input:
		(left, right) = parse(line)
		if left.contains(right):
			count += 1
	return count

assert find_partial_overlaps(test_fixtures()) == 4

print(find_partial_overlaps(ranges_file_lines))