#!/usr/bin/python3
# -*- coding:utf-8 -*-

from collections.abc import Collection


class DisjointSet:
	"""
	A class that deals with partitions of a set.
	"""
	def __init__(self, points: Collection) -> None:
		"""
		Initializes a discrete partition. 
		"""
		self.parent = {p: p for p in points}
		self.depth = {p: 0 for p in points}  # depth of the tree rooted at a specific vertex

	def find(self, p):
		"""
		Finds the oldest parent of p.
		"""
		if self.parent[p] != p:
			self.parent[p] = self.find(self.parent[p])
		return self.parent[p]

	def union(self, p, q) -> None:
		"""
		Merges the classes containing p and q.
		"""
		p, q = self.find(p), self.find(q)
		if p != q:
			if self.depth[p] > self.depth[q]:  # Uses the root that has the greatest depth as the new root.
				self.parent[q] = p
			elif self.depth[p] < self.depth[q]:
				self.parent[p] = q
			else:  # If both roots have the same depth, the depth of the new root is increased by 1.
				self.parent[q] = p
				self.depth[p] += 1
