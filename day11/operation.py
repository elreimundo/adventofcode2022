class Operation:
	def __init__(self, operand, value):
		self.operand = operand
		self.value = value

	def __eq__(self, other):
		return self.operand == other.operand and self.value == other.value

	def __repr__(self) -> str:
		return f'new = old {self.operand} {self.value}'

	def get_value(self, input: int) -> int:
		return input if self.value == 'old' else int(self.value)

	def modify_worry(self, input: int) -> int: pass

	@staticmethod
	def factory(operand, value):
		match operand:
			case '+': return AdditionOperation(value)
			case '*': return MultiplicationOperation(value)

class AdditionOperation(Operation):
	def __init__(self, value):
		super().__init__('+', value)

	def modify_worry(self, input: int) -> int:
		return input + self.get_value(input)

class MultiplicationOperation(Operation):
	def __init__(self, value):
		super().__init__('*', value)

	def modify_worry(self, input: int) -> int:
		return input * self.get_value(input)
