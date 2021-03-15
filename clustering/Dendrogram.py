#!/usr/bin/python3
# -*- coding:utf-8 -*-

import abc
from typing import *


class Point(tuple):
	"""
	A class for representing points in the euclidean space.
	"""
	def __add__(self, other):
		return Point(self[i] + other[i] for i in range(len(self)))

	def __mul__(self, scalar):
		return Point(scalar * self[i] for i in range(len(self)))

	def __truediv__(self, scalar):
		return Point(self[i] / scalar for i in range(len(self)))


class Vertex:
	"""
	A class used to manipulate trees.
	"""
	__metaclass__ = abc.ABCMeta

	def __init__(self, height: float = 0) -> None:
		self.height = height
		self.parent = None

	def find(self) -> None:
		return self.parent.find() if self.parent else self

	@abc.abstractmethod
	def __call__(self, height: float) -> Generator:
		pass


class Leaf(Vertex):
	"""
	A class used to manipulate trees. A Leaf is a labelled vertex that has no child and stores a value.
	"""
	def __init__(self, label: str or int, value: Point) -> None:
		"""
		Initializes a leaf with a given value and sets its height to 0.
		"""
		Vertex.__init__(self)
		self.label = label
		self.value = value

	def __call__(self, height: float) -> Generator:
		"""
		Returns the singleton {label}.
		"""
		yield {self.label}


class Node(Vertex):
	"""
	A class used to manipulate trees. A Node is a vertex that has at least one child (i.e. is not a Leaf).
	"""
	def __init__(self, height: float, children: Collection[Vertex]) -> None:
		"""
		Initializes a new node, parent to the vertexes in children, with a positive height and optionally a value.
		"""
		assert height > 0, "Height must be positive."
		Vertex.__init__(self, height)
		assert children, "Cannot create a Node with no child."
		for child in children:
			assert child.height <= height, "Invalid height."
			assert child.parent is None, "Invalid child."
			child.parent = self
		self.children = children

	def __call__(self, height: float) -> Generator:
		"""
		Returns the partition induced by the tree rooted at self and restricted to a given height.
		"""
		if height >= self.height:
			yield set.union(*(s for child in self.children for s in child(height)))
		else:
			for child in self.children:
				for s in child(height):
					yield s


class Dendrogram:
	"""
	A class used to define and manipulate a dendrogram on a set.
	See https://fr.wikipedia.org/wiki/Dendrogramme for a formal definition.
	"""
	"""
	Initializes a new Dendrogram with singletons.
	"""
	def __init__(self, sample: Mapping[str or int, Point or Tuple[float]]) -> None:  # O(n)
		self.leaves = {label: Leaf(label, Point(value)) for label, value in sample.items()}

	def find(self, label: str or int) -> Vertex:  # O(n) in worst case, O(log(n)) expected
		"""
		Finds the root of the tree containing the Leaf label.
		"""
		return self.leaves[label].find()

	def join_leaves(self, l1: str or int, l2: str or int, height: float) -> None:  # O(n)
		"""
		Joins the roots of the trees containing the leaves v1 and v2.
		"""
		r1, r2 = self.leaves[l1].find(), self.leaves[l2].find()
		Node(height, [r1, r2])

	@property
	def root(self):
		first_leave = list(self.leaves.values())[0]
		return first_leave.find()

	def __call__(self, height: float) -> list:
		"""
		Returns the partition obtained by cutting the Dendrogram at a given height.
		"""
		return list(self.root(height))
