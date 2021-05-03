#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from Dendrogram import Dendrogram, Point
from typing import *
from math import sqrt


def d(x: Point, y: Point):
	assert len(x) == len(y), "Cannot measure distance between points of different dimensions."
	return sqrt(sum((x[i] - y[i]) ** 2 for i in range(len(x))))


def simple_linkage(sample: Mapping[str or int, Point or Tuple[float]]) -> Dendrogram:  # O(n^2 log(n))
	ddg = Dendrogram(sample)  # O(n)
	dist = [(i, j) for i in sample for j in sample if i != j]  # O(n^2)
	dist.sort(key=lambda t: d(sample[t[0]], sample[t[1]]))  # O(n^2 log(n))
	for i, j in dist:  # O(n^2)
		if ddg.find(i) is not ddg.find(j):  # O(log(n))
			ddg.join_leaves(i, j, d(sample[i], sample[j]))  # O(n) but only executed O(n) times
	return ddg
