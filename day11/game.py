from operation import Operation

from collections.abc import Callable, Generator
from functools import reduce

class Item:
	def __init__(self, worry_level: int):
		self.worry_level = worry_level

	def sigh_with_relief(self):
		self.worry_level //= 3

	def update_worry_level(self, operation: Callable[[int], int]):
		self.worry_level = operation(self.worry_level)

	def is_worry_divisible_by(self, dividend: int) -> bool:
		return self.worry_level % dividend == 0

	def copy(self):
		return Item(self.worry_level)

	def __eq__(self, other) -> bool:
		return self.worry_level == other.worry_level

	def __repr__(self) -> str:
		return f'Item({self.worry_level})'

class ThrowRule:
	def __init__(self, dividend: int, monkey_a_index: int, monkey_b_index: int):
		self.dividend = dividend
		self.monkey_a_index = monkey_a_index
		self.monkey_b_index = monkey_b_index
		self.monkey_to_throw_to = (
			lambda item:
				monkey_a_index if item.is_worry_divisible_by(dividend) else monkey_b_index
		)

	def monkey_to_throw_to(self, item) -> int:
		return self.monkey_a_index if item.is_worry_divisible_by(self.dividend) else self.monkey_b_index

	def __eq__(self, other):
		return (
			self.dividend == other.dividend and
			self.monkey_a_index == other.monkey_a_index and
			self.monkey_b_index == other.monkey_b_index
		)

	def __repr__(self) -> str:
		return f'If divisible by {self.dividend} then {self.monkey_a_index} else {self.monkey_b_index}'

class Monkey:
	def __init__(self, items: list[Item], operation: Operation, throw_rule: ThrowRule, ease_worry = True):
		self.inspection_count = 0
		self.items = items
		self.operation = operation
		self.throw_rule = throw_rule
		self.ease_worry = ease_worry

	def handle_and_throw_items(self) -> Generator[(Item, int), None, None]:
		while len(self.items) > 0:
			self.inspection_count += 1
			item = self.items.pop(0)
			item.update_worry_level(self.operation.modify_worry)
			if self.ease_worry:
				item.sigh_with_relief()
			yield (item, self.throw_rule.monkey_to_throw_to(item))

	def catch(self, item: Item):
		self.items.append(item)

	def copy(self):
		copied_monkey = Monkey([item.copy() for item in self.items], self.operation, self.throw_rule, self.ease_worry)
		copied_monkey.inspection_count = self.inspection_count
		return copied_monkey

	def __eq__(self, other) -> bool:
		return (
			self.items == other.items and
			self.operation == other.operation and
			self.throw_rule == other.throw_rule
		)

	def __repr__(self) -> str:
		return f'Monkey({self.operation}, {self.throw_rule}) holding items {self.items}'

class Game:
	def __init__(self, monkeys: list[Monkey]):
		self.monkeys = monkeys
		self.lowest_common_multiple = reduce(
			lambda a, b: a * b,
			[monkey.throw_rule.dividend for monkey in monkeys]
		)

	def optimize_bytespace(self, num: int) -> int:
		return num % self.lowest_common_multiple

	def play_a_round(self):
		for monkey in self.monkeys:
			for item, monkey_index in monkey.handle_and_throw_items():
				item.update_worry_level(self.optimize_bytespace)
				self.monkeys[monkey_index].catch(item)

	def play_x_rounds(self, x: int):
		while x > 0:
			self.play_a_round()
			x -= 1

	def get_top_x_most_active_monkeys(self, x: int) -> list[Monkey]:
		sortable_monkeys = self.monkeys[:]
		sortable_monkeys.sort(reverse=True, key=lambda monkey: monkey.inspection_count)
		return sortable_monkeys[0:x]

	def get_monkey_business(self, top_x_monkeys = 2) -> int:
		return reduce(
			lambda a, b: a.inspection_count * b.inspection_count,
			self.get_top_x_most_active_monkeys(top_x_monkeys)
		)

	def copy(self):
		return Game([monkey.copy for monkey in self.monkeys])

	def __eq__(self, other) -> bool:
		return self.monkeys == other.monkeys
