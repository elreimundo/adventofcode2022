from landscape import Landscape

def parse(input: list[str]) -> Landscape:
	return Landscape([[ int(character) for character in line.strip() ] for line in input])
