# Rock Paper Scissors can be modeled using differences and a modulus
# if Rock=1, Paper=2, and Scissors=3, then we can simply subtract one from another:

# Rock - Paper = Paper - Scissors -1 (lose)
# Paper - Rock = Scissors - Paper = 1 (win)
# Rock - Rock = Paper - Paper = Scissors - Scissors = 0

# the only catch is the wraparound case (Scissors - Rock = 2 (lose) and Rock - Scissors = -2 (win))

# But if we recognize that the relationship is circular (which, in programming, usually means a modulus):

# (Rock - Paper) % 3 = (Paper - Scissors) % 3 = (Scissors - Rock) % 3 = 2
# (Paper - Rock) % 3 = (Scissors - Paper) % 3 = (Paper - Scissors) % 3 = 1
# (Rock - Rock) % 3 = (Paper - Paper) % 3 = (Scissors - Scissors) % 3 = 0

# We want to assign points as follows: 2 -> 6, 1 -> 0, 0 -> 3. Sure looks like (2 -> 2, 1 -> 0, 0 -> 1) * 3 to me.
# So what modular operation keeps the 2 as is but flips the 0 and the 1? Looks like (1 - X) % 3 will do the trick:
# (1 - 2) % 3 = 2
# (1 - 1) % 3 = 0
# (1 - 0) % 3 = 1

def game_points_naive_solution(their_guess: int, my_guess: int) -> int:
	return ((1 - (their_guess - my_guess)) % 3) * 3 + my_guess

# We also know that a win is worth 6 points, a tie is worth 3, and a loss is worth 0
# So for the more complicated flow, we simply need to know how many points our guess
# Would have been worth for a win/tie/loss
# +-------+--------+--------------+------+
# | input | result | ours | score | 3r - (2r - 1 - i) % 3 
# +-------+--------+------+-------+------+
# | R=1   | L=1    | S=3  | 3     | 3 - (1 - 1) % 3
# | P=2   | L=1    | R=1  | 1     | 3 - (1 - 2) % 3
# | S=3   | L=1    | P=2  | 2     | 3 - (1 - 3) % 3
# +-------+--------+------+-------+
# | R=1   | T=2    | R=1  | 4     | 6 - (3 - 1) % 3
# | P=2   | T=2    | P=2  | 5     | 6 - (3 - 2) % 3
# | S=3   | T=2    | S=3  | 6     | 6 - (3 - 3) % 3
# +-------+--------+------+-------+
# | R=1   | W=3    | P=2  | 8     | 9 - (5 - 1) % 3
# | P=2   | T=3    | S=3  | 9     | 9 - (5 - 2) % 3
# | S=3   | T=3    | R=1  | 7     | 9 - (5 - 3) % 3
# +-------+--------+------+-------+

def game_points_secret_solution(their_guess: int, result: int) -> int:
	return 3 * result - (2 * result - 1 - their_guess) % 3

def parse_input(line: str) -> (int, int):
	"""     A->1, B->2, C->3            X->1, Y->2, Z->3"""
	return ((ord(line[0]) + 1) % 3 + 1, (ord(line[2]) - 1) % 3 + 1)