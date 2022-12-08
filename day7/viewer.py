from my_file_system import MyFileSystem, File, Directory

def view(my_file_system: MyFileSystem, indentation_depth: int = 0) -> str:
	if isinstance(my_file_system, File):
		return f'{my_file_system.file_name} (file, size={my_file_system.file_size})'
	elif isinstance(my_file_system, Directory):
		lines = [f'{my_file_system.name} (dir)'] + [
			f'{" " * indentation_depth} - {view(child, indentation_depth + 2)}' for child in my_file_system.children.values()
		]
		return "\n".join(lines)
	else: # MyFileSystem base object?
		return f'- {view(my_file_system.root(), indentation_depth)}'
