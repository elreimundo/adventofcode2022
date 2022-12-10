class CRT:
	def __init__(self):
		self.x = 1
		self.cycle_count = 1
		self.observers = []

	def add_observer(self, observer):
		self.observers.append(observer)

	def addx(self, x: int):
		self.cycle(2)
		self.x += x

	def noop(self):
		self.cycle(1)

	def signal_strength(self):
		return self.x * self.cycle_count

	def cycle(self, count: int):
		if count > 0:
			for observer in self.observers:
				observer(self)
			self.cycle_count += 1
			self.cycle(count - 1)
