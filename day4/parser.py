from my_range import Range

def parse(input: str) -> (Range, Range):
	[[left_min, left_max], [right_min, right_max]] = [
		[
			int(value) for value in split_at(tuple, "-")
		] for tuple in split_at(input, ",")
	]
	return (Range(left_min, left_max), Range(right_min, right_max))

def split_at(input: str, on: str) -> (str, str):
	return [part.strip() for part in input.split(on)]
