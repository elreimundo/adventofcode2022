import os

from my_file_system import MyFileSystem
from parser import parse
from viewer import view
from defragmenter import identify_target_directories

def test_fixtures() -> list[str]:
	return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()

test_file_system = parse(test_fixtures())

# print(view(test_file_system))

less_than_100000 = lambda x: x <= 100000

def total_target_file_size(file_system: MyFileSystem, predicate) -> int:
	return sum([directory.size() for directory in identify_target_directories(file_system, predicate)])

assert total_target_file_size(test_file_system, less_than_100000) == 95437

io_lines = open(os.path.join(os.path.dirname(__file__), "io.my_data"), "r").readlines()
file_system = parse(io_lines)

# print(view(file_system))

print(total_target_file_size(file_system, less_than_100000))

def determine_space_to_free_up(file_system: MyFileSystem, maximum_allowed_usage: int):
	return file_system.root().size() - maximum_allowed_usage

maximum_allowed_usage = 70000000 - 30000000 # need at least 30M, capacity is 70M

assert determine_space_to_free_up(test_file_system, maximum_allowed_usage) == 8381165

frees_up_at_least = lambda x: lambda y: y >= x

assert frees_up_at_least(5)(10)

def find_smallest_directory_to_delete(file_system: MyFileSystem, maximum_allowed_usage: int):
	directories = identify_target_directories(
		file_system,
		frees_up_at_least(
			determine_space_to_free_up(file_system, maximum_allowed_usage)
		)
	)
	directories.sort(key=lambda directory: directory.size())
	return directories[0]

assert find_smallest_directory_to_delete(test_file_system, maximum_allowed_usage).size() == 24933642

print(find_smallest_directory_to_delete(file_system, maximum_allowed_usage).size())