from crt import CRT

class Command:
	def apply_to(self, crt: CRT):
		pass

class NoopCommand(Command):
	def apply_to(self, crt: CRT):
		crt.noop()

	def __repr__(self):
		return 'noop'

class AddxCommand(Command):
	def __init__(self, x: int):
		self.x = x

	def apply_to(self, crt: CRT):
		crt.addx(self.x)

	def __repr__(self):
		return f'addx {self.x}'

def parse(input: list[str]) -> list[Command]:
	return [parse_line(line) for line in input]

def parse_line(line: str) -> Command:
	match line.strip().split():
		case ['addx', x]: return AddxCommand(int(x))
		case ['noop']: return NoopCommand()
