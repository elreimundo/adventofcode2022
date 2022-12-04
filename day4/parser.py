from my_range import Range

def parse(input: str) -> (Range, Range):
	return [
		Range(*[
			int(value) for value in split_at(tuple, "-")
		]) for tuple in split_at(input, ",")
	]

def split_at(input: str, on: str) -> (str, str):
	return [part.strip() for part in input.split(on)]
