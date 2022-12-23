import json
import os

from functools import cmp_to_key

def parse(input: list[str]): # returns a list of tuples to compare
	match input:
		case []:
			return []
		case ['', *more]:
			return parse(more)
		case [line1, line2, *rest]:
			return [(json.loads(line1), json.loads(line2))] + parse(rest)

def clean(raw_input: list[str]) -> list[str]:
	return [line.strip() for line in raw_input]

def test_fixtures() -> list[str]:
	return """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".splitlines()

def test_pairs():
	return [
		([1,1,3,1,1],[1,1,5,1,1]),
		([[1],[2,3,4]],[[1],4]),
		([9],[[8,7,6]]),
		([[4,4],4,4],[[4,4],4,4,4]),
		([7,7,7,7],[7,7,7]),
		([],[3]),
		([[[]]],[[]]),
		([1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9])
	]

assert parse(clean(test_fixtures())) == test_pairs()

def compare(a, b) -> int:
	if type(a) is int:
		if type(b) is int:
			return -1 if a < b else 1 if a > b else 0
		else:
			return compare([a], b)
	if type(b) is int:
		return compare(a, [b])
	i = 0
	while i < len(a):
		if i >= len(b):
			return 1
		comparison = compare(a[i], b[i])
		if comparison != 0:
			return comparison
		i += 1
	return -1 if i < len(b) else 0


def score(input: list[tuple]) -> int:
	total = 0
	for (i, pair) in enumerate(input):
		if compare(*pair) < 0:
			total += (i + 1)
	return total


assert score(test_pairs()) == 13
pairs_lines = open(os.path.join(os.path.dirname(__file__), "pairs.my_data"), "r").readlines()
pairs = parse(clean(pairs_lines))

print(score(pairs))

def untuple(input: list[tuple]) -> list:
	untupled = []
	for tuple in input:
		for el in tuple:
			untupled.append(el)
	return untupled

fully_sorted = sorted(untuple(pairs) + [[[2]],[[6]]], key=cmp_to_key(compare))

prod = 1
for i in range(len(fully_sorted)):
	if fully_sorted[i] == [[2]] or fully_sorted[i] == [[6]]:
		prod *= (i + 1)
print(prod)