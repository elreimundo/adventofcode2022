import os

def traverse_for_unique_subset(string: str, depth: int = 4) -> int:
	seen_indices: dict[str, int] = {}
	current_index = 0
	while current_index < len(string) - depth:
		if len(set(string[current_index:current_index + depth])) == depth:
			return current_index + depth
		current_index += 1

assert traverse_for_unique_subset("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
assert traverse_for_unique_subset("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert traverse_for_unique_subset("nppdvjthqldpwncqszvftbrmjlhg") == 6
assert traverse_for_unique_subset("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
assert traverse_for_unique_subset("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

assert traverse_for_unique_subset("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
assert traverse_for_unique_subset("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
assert traverse_for_unique_subset("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
assert traverse_for_unique_subset("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
assert traverse_for_unique_subset("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26

input = open(os.path.join(os.path.dirname(__file__), "signal.my_data"), "r").read()

print(traverse_for_unique_subset(input))
print(traverse_for_unique_subset(input, 14))