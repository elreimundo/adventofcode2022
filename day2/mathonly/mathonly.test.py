from mathonly import game_points_naive_solution, game_points_secret_solution

# TESTS
ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS_POINTS = 0
TIE_POINTS = 3
WIN_POINTS = 6

assert game_points_naive_solution(PAPER, ROCK), LOSS_POINTS + ROCK
assert game_points_naive_solution(SCISSORS, PAPER), LOSS_POINTS + PAPER
assert game_points_naive_solution(ROCK, SCISSORS), LOSS_POINTS + SCISSORS
assert game_points_naive_solution(ROCK, ROCK), TIE_POINTS + ROCK
assert game_points_naive_solution(PAPER, PAPER), TIE_POINTS + PAPER
assert game_points_naive_solution(SCISSORS, SCISSORS), TIE_POINTS + SCISSORS
assert game_points_naive_solution(SCISSORS, ROCK), WIN_POINTS + ROCK
assert game_points_naive_solution(ROCK, PAPER), WIN_POINTS + PAPER
assert game_points_naive_solution(PAPER, SCISSORS), WIN_POINTS + SCISSORS

LOSE = 1
TIE = 2
WIN = 3

assert game_points_secret_solution(PAPER, LOSE), LOSS_POINTS + ROCK
assert game_points_secret_solution(SCISSORS, LOSE), LOSS_POINTS + PAPER
assert game_points_secret_solution(ROCK, LOSE), LOSS_POINTS + SCISSORS
assert game_points_secret_solution(ROCK, TIE), TIE_POINTS + ROCK
assert game_points_secret_solution(PAPER, TIE), TIE_POINTS + PAPER
assert game_points_secret_solution(SCISSORS, TIE), TIE_POINTS + SCISSORS
assert game_points_secret_solution(SCISSORS, WIN), WIN_POINTS + ROCK
assert game_points_secret_solution(ROCK, WIN), WIN_POINTS + PAPER
assert game_points_secret_solution(PAPER, WIN), WIN_POINTS + SCISSORS