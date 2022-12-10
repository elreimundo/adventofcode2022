import os

from crt import CRT
from crt_watcher import CRTSignalWatcher, CRTSpriteWatcher
from parser import parse, Command

from test_fixtures import test_fixtures

test_commands = parse(test_fixtures())

sprite_line_length = 40
important_cycles = set([i for i in range(20, 240, sprite_line_length)])

test_crt = CRT()
test_crt_watcher = CRTSignalWatcher(test_crt, important_cycles)
test_crt_sprite_watcher = CRTSpriteWatcher(test_crt, sprite_line_length)

for command in test_commands:
	command.apply_to(test_crt)

assert test_crt_watcher.total_signal_count == 13140
print(test_crt_sprite_watcher.print())

commands = parse(open(os.path.join(os.path.dirname(__file__), "commands.my_data"), "r").readlines())

crt = CRT()
crt_watcher = CRTSignalWatcher(crt, important_cycles)
crt_sprite_watcher = CRTSpriteWatcher(crt, sprite_line_length)

for command in commands:
	command.apply_to(crt)

print(crt_watcher.total_signal_count)
print(crt_sprite_watcher.print())