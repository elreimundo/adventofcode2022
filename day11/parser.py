from game import Game, Item, ThrowRule, Monkey
from operation import Operation
from collections.abc import Callable

class ThrowRuleBuilder:
	def __init__(self):
		self.reset()

	def reset(self):
		self.dividend = None
		self.monkey_a_index = None
		self.monkey_b_index = None

	def is_ready_to_build(self) -> bool:
		return (
			self.dividend is not None and
			self.monkey_a_index is not None and
			self.monkey_b_index is not None
		)

	def build(self) -> ThrowRule:
		throw_rule = ThrowRule(self.dividend, self.monkey_a_index, self.monkey_b_index)
		self.reset()
		return throw_rule

class MonkeyBuilder:
	def __init__(self, ease_worry = True):
		self.throw_rule_builder = ThrowRuleBuilder()
		self.ease_worry = ease_worry
		self.reset()

	def reset(self):
		self.items = None
		self.operation = None

	def is_ready_to_build(self) -> bool:
		return (
			self.items is not None and
			self.operation is not None and
			self.throw_rule_builder.is_ready_to_build()
		)

	def build(self) -> Monkey:
		monkey = Monkey(self.items, self.operation, self.throw_rule_builder.build(), self.ease_worry)
		self.reset()
		return monkey

def parse_line(line: str, monkey_builder: MonkeyBuilder):
	match line.strip().split():
		case ['Starting', 'items:', *items]:
			monkey_builder.items = [Item(int(item.replace(',',''))) for item in items]
		case ['Operation:', 'new', '=', 'old', operand, value]:
			monkey_builder.operation = Operation.factory(operand, value)
		case ['Test:', 'divisible', 'by', dividend]:
			monkey_builder.throw_rule_builder.dividend = int(dividend)
		case ['If', 'true:', 'throw', 'to', 'monkey', monkey_a_index]:
			monkey_builder.throw_rule_builder.monkey_a_index = int(monkey_a_index)
		case ['If', 'false:', 'throw', 'to', 'monkey', monkey_b_index]:
			monkey_builder.throw_rule_builder.monkey_b_index = int(monkey_b_index)

def parse(lines: list[str], ease_worry = True) -> Game:
	monkeys = []
	monkey_builder = MonkeyBuilder(ease_worry)
	for line in lines:
		parse_line(line, monkey_builder)
		if monkey_builder.is_ready_to_build():
			monkeys.append(monkey_builder.build())
	return Game(monkeys)

