from rope import Vector

def parse(input: list[str]) -> list[Vector]:
	return [parse_line(line) for line in input]

def parse_line(line: str) -> Vector:
	match line.split():
		case ['R', distance]: return Vector(int(distance), 0)
		case ['L', distance]: return Vector(-int(distance), 0)
		case ['U', distance]: return Vector(0, int(distance))
		case ['D', distance]: return Vector(0, -int(distance))
