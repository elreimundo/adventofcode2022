import os

def parse(lines: list[str]) -> list[int]:
	elves = []
	current_total = 0
	for line in lines:
		if line:
			current_total += int(line)
		elif current_total > 0:
			elves.append(current_total)
			current_total = 0
	elves.sort(reverse=True)
	return elves

def calorieTotalOfTopN(elves: list[int], n: int) -> int:
	return sum(elves[0:n])

elves_file = open(os.path.join(os.path.dirname(__file__), "elves.my_data"), "r")
elves_lines = [line.strip() for line in elves_file.readlines()]

elves = parse(elves_lines)
answer_1 = calorieTotalOfTopN(elves, 1)
answer_2 = calorieTotalOfTopN(elves, 3)

print(answer_1, answer_2)
