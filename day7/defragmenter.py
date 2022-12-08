from my_file_system import MyFileSystem, Directory, File
from functools import reduce

def identify_target_directories(file_system, predicate) -> list[Directory]:
	if isinstance(file_system, File):
		return []
	elif isinstance(file_system, Directory):
		return reduce(
			lambda directories, child: directories + identify_target_directories(child, predicate),
			file_system.children.values(),
			[file_system] if predicate(file_system.size()) else []
		)
	else:
		return identify_target_directories(file_system.root(), predicate)
