class MyFileSystem:
	def __init__(self):
		self.root_directory = Directory('/')

	def root(self):
		return self.root_directory

	def size(self) -> int: pass

class Directory(MyFileSystem):
	def __init__(self, name: str, parent_directory = None, children = []):
		self.name = name
		self.children = { child.file_name: child for child in children }
		self.parent_directory = parent_directory

	def add_child_directory(self, dirname: str):
		self.children[dirname] = Directory(dirname, parent_directory=self)

	def chdir(self, dirname):
		match dirname:
			case "/": return self.root()
			case "..": return self.parent_directory
			case _:  return self.children[dirname]

	def add_child_file(self, file_name: str, file_size: int):
		self.children[file_name] = File(file_name, file_size)

	def size(self) -> int:
		return sum([child.size() for child in self.children.values()])

	def root(self):
		return self if self.parent_directory is None else self.parent_directory.root()

	def full_path(self):
		return f'{"" if self.parent_directory is None else self.parent_directory.full_path() + "."}{self.name}'

class File(MyFileSystem):
	def __init__(self, file_name: str, file_size: int):
		self.file_name = file_name
		self.file_size = file_size

	def size(self) -> int:
		return self.file_size
