import os
from functools import reduce

def find_duplicate_item(inputs: list[str]) -> str:
	character_sets = [set(input) for input in inputs]
	return list(reduce(lambda set1, set2: set1 & set2, character_sets))[0]

def find_duplicate_item_in_single_rucksack(input: str) -> (str, str):
	length = len(input)
	compartment_size = int(length / 2)
	return find_duplicate_item([input[:compartment_size], input[compartment_size:]])

def test_fixtures() -> list[str]:
	return """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()

def test_targets() -> list[str]:
	return ["p", "L", "P", "v", "t", "s"]

def test_priority_targets() -> list[int]:
	return [16, 38, 42, 22, 20, 19]

def priority(letter: str) -> int:
	char = ord(letter)
	if char >= 97: # lowercase a
		return char - 96
	else:
		return char - 38 # A (ord=65) should be priority 27

def priority_sum_of_all_duplicate_items(lines: list[str]) -> int:
	priority_sum = 0
	for line in lines:
		priority_sum += priority(find_duplicate_item_in_single_rucksack(line.strip()))
	return priority_sum


assert [find_duplicate_item_in_single_rucksack(fixture) for fixture in test_fixtures()] == test_targets()
assert [priority(find_duplicate_item_in_single_rucksack(fixture)) for fixture in test_fixtures()] == test_priority_targets()
assert priority_sum_of_all_duplicate_items(test_fixtures()) == 157

rucksacks = open(os.path.join(os.path.dirname(__file__), "rucksacks.my_data"), "r")
rucksack_lines = rucksacks.readlines()

print(priority_sum_of_all_duplicate_items(rucksack_lines))

def chunked(inputs: list[str], count: int) -> list[str]:
	buffer = []
	for input in inputs:
		buffer.append(input.strip())
		if len(buffer) == count:
			yield buffer
			buffer = []

def priority_sum_of_elf_triplets(lines: list[str]) -> int:
	priority_sum = 0
	for chunk in chunked(lines, 3):
		priority_sum += priority(find_duplicate_item(chunk))
	return priority_sum

assert priority_sum_of_elf_triplets(test_fixtures()) == 70

print(priority_sum_of_elf_triplets(rucksack_lines))