from game import Game

def view(game: Game) -> str:
	crates = game.crates
	base = ' '.join([f' {i + 1} ' for i in range(len(crates))])
	lines = [base]
	depth = max([len(crate) for crate in crates])
	for row_index in range(depth):
		lines.append(
			' '.join(
				f'[{crate[row_index]}]'
					if row_index < len(crate)
					else '   '
					for crate in crates
			)
		)
	lines.reverse()
	return "\n".join(lines)