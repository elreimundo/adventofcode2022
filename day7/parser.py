from my_file_system import MyFileSystem

def parse(lines: list[str]) -> MyFileSystem:
	file_system = MyFileSystem()
	cwd = file_system.root()
	for line in lines:
		match line.strip().split():
			case ['$', 'cd', dirname]:
				cwd = cwd.chdir(dirname)
			case ['$', 'ls']:
				pass
			case ['dir', dirname]:
				cwd.add_child_directory(dirname)
			case [size, file_name]:
				cwd.add_child_file(file_name, int(size))
	return file_system


