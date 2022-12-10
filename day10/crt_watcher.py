from crt import CRT

class CRTSignalWatcher:
	def __init__(self, crt: CRT, important_cycles: set[int]):
		self.total_signal_count = 0
		self.important_cycles = important_cycles
		crt.add_observer(self.update)

	def update(self, crt: CRT):
		if crt.cycle_count in self.important_cycles:
			self.total_signal_count += crt.signal_strength()

class CRTSpriteWatcher:
	def __init__(self, crt: CRT, line_length: int):
		self.pixels = []
		self.line_length = line_length
		crt.add_observer(self.update)

	def update(self, crt: CRT):
		"""TODO: Something is wrong with this logic at the final pixel of the modulus"""
		current_pixel = crt.cycle_count % self.line_length
		self.pixels.append(
			'#' if current_pixel >= crt.x and current_pixel <= crt.x + 2 else '.'
		)

	def print(self):
		lines = []
		current_line = ''
		for pixel in self.pixels:
			current_line += pixel
			if len(current_line) == self.line_length:
				lines.append(current_line)
				current_line = ''
		if (len(current_line) > 0):
			lines.append(current_line)
		return "\n".join(lines)
