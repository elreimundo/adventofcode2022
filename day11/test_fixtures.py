from game import Game, Monkey, Item, ThrowRule
from operation import AdditionOperation, MultiplicationOperation

def starting_game(ease_worry = True) -> Game:
	return Game([
		Monkey(
			[
				Item(79),
				Item(98)
			],
			MultiplicationOperation('19'),
			ThrowRule(23, 2, 3),
			ease_worry
		),
		Monkey(
			[
				Item(54),
				Item(65),
				Item(75),
				Item(74)
			],
			AdditionOperation('6'),
			ThrowRule(19, 2, 0),
			ease_worry
		),
		Monkey(
			[
				Item(79),
				Item(60),
				Item(97)
			],
			MultiplicationOperation('old'),
			ThrowRule(13, 1, 3),
			ease_worry
		),
		Monkey(
			[
				Item(74)
			],
			AdditionOperation('3'),
			ThrowRule(17, 0, 1),
			ease_worry
		)
	])

def starting_instructions() -> list[str]:
	return """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".splitlines()