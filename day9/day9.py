import os

from rope import LinkedRope
from rope_tracer import RopeTracer
from parser import parse

def test_fixtures() -> list[str]:
	return """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()

test_moves = parse(test_fixtures())

test_tracer = RopeTracer()
test_tracer.multi_move(test_moves)

assert len(test_tracer.tail_positions) == 13

rope_moves = parse(open(os.path.join(os.path.dirname(__file__), "rope_moves.my_data"), "r").readlines())

tracer = RopeTracer()
tracer.multi_move(rope_moves)

print(len(tracer.tail_positions))

test_linked_tracer = RopeTracer(LinkedRope.with_length(9))
test_linked_tracer.multi_move(test_moves)

assert len(test_linked_tracer.tail_positions) == 1

linked_tracer = RopeTracer(LinkedRope.with_length(9))
linked_tracer.multi_move(rope_moves)

print(len(linked_tracer.tail_positions))

