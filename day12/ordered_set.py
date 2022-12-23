from typing import TypeVar, Generic

T = TypeVar('T')

class ImmutableOrderedSet(Generic[T]):
	def __init__(self, elements: list[T] = [], element_set: set[T] = set()):
		self.elements = elements
		self.element_set = element_set

	def contains(self, value: T) -> bool:
		return value in self.element_set

	def add(self, element: T):
		return self if self.contains(element) else ImmutableOrderedSet(
			self.elements + [element],
			self.element_set | { element }
		)

	def __repr__(self) -> str:
		return f'{{{",".join([str(el) for el in self.elements])}}}'

	def __eq__(self, other):
		return self.elements == other.elements

	def __hash__(self):
		return hash(self.elements)

	def __len__(self) -> int:
		return len(self.elements)

	def __getitem__(self, index) -> T:
		return self.elements[index]

class MutableOrderedSet(Generic[T]):
	def __init__(self):
		self.elements = []
		self.element_set = set()

	def contains(self, value: T) -> bool:
		return value in self.element_set

	def add(self, element: T):
		if element not in self.element_set:
			self.elements.append(element)
			self.element_set.add(element)

	def pop(self, index: int = -1) -> T:
		element = self.elements.pop(index)
		self.element_set.remove(element)
		return element

	def __repr__(self) -> str:
		return f'{{{",".join([str(el) for el in self.elements])}}}'

	def __eq__(self, other):
		return self.elements == other.elements

	def __len__(self) -> int:
		return len(self.elements)

	def __getitem__(self, index) -> T:
		return self.elements[index]
