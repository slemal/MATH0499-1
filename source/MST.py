#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import networkx as nx
from UnionFind import DisjointSet


def kruskal_sg(g: nx.Graph) -> None:  # O(E log(V))
	"""
	Finds a minimum weight spanning tree in the simple graph g using Kruskal's algorithm.
	Edges that are part of the spanning tree have a "spanning" value set to true.
	"""
	ds = DisjointSet(g.nodes)  # O(V)
	edges = sorted(g.edges, key=lambda t: g[t[0]][t[1]]["weight"])  # Edges are sorted by weight. O(E log(E))
	for u, v in edges:  # O(E) iterations
		if ds.find(u) != ds.find(v):  # O(log(V))
			g[u][v]["spanning"] = True
			ds.union(u, v)
		else:
			g[u][v]["spanning"] = False


def boruvka_sg(g: nx.Graph) -> None:
	"""
	Finds a minimum weight spanning tree in the simple graph g using Boruvka's algorithm.
	Edges that are part of the spanning tree have a "spanning" value set to true.
	"""
	ds = DisjointSet(g.nodes)  # O(V)
	edges = list(g.edges())  # O(E)
	while edges:  # O(log(V)) iterations
		lightest_edges = dict()  # For each component, we will store its edge of minimal weight in this variable.

		for i in reversed(range(len(edges))):  # O(E)
			u, v = edges[i]
			if ds.find(u) == ds.find(v):  # O(V) overall
				edges.pop(i)
				if g[u][v].get("spanning") is None:
					g[u][v]["spanning"] = False

			else:  # O(1)
				# Checks whether the current edge is lighter than the lightest edge of the component containing u.
				if not lightest_edges.get(ds.find(u)) or lightest_edges[ds.find(u)][2] > g[u][v]["weight"]:
					lightest_edges[ds.find(u)] = (u, v, g[u][v]["weight"])

				if not lightest_edges.get(ds.find(v)) or lightest_edges[ds.find(v)][2] > g[u][v]["weight"]:
					lightest_edges[ds.find(v)] = (u, v, g[u][v]["weight"])

		for u, v, w in lightest_edges.values():  # O(V)
			g[u][v]["spanning"] = True
			ds.union(u, v)


def kruskal_mg(g: nx.MultiGraph) -> None:
	"""
	Finds a minimum weight spanning tree in the multigraph g using Kruskal's algorithm.
	Edges that are part of the spanning tree have a "spanning" value set to true.
	"""
	ds = DisjointSet(g.nodes)  # O(V)
	edges = sorted(g.edges, key=lambda t: g[t[0]][t[1]][t[2]]["weight"])  # O(E log(E))
	for u, v, m in edges:  # O(E) iterations
		if ds.find(u) != ds.find(v):  # O(log(V))
			g[u][v][m]["spanning"] = True
			ds.union(u, v)
		else:
			g[u][v][m]["spanning"] = False


def boruvka_mg(g: nx.MultiGraph) -> None:
	"""
	Finds a minimum weight spanning tree in the multigraph g using Boruvka's algorithm.
	Edges that are part of the spanning tree have a "spanning" value set to true.
	"""
	ds = DisjointSet(g.nodes)  # O(V)
	edges = list(g.edges)  # O(E)
	while edges:  # O(log(V)) iterations
		lightest_edges = dict()

		for i in reversed(range(len(edges))):  # O(E)
			u, v, m = edges[i]
			if ds.find(u) == ds.find(v):  # O(V) overall
				edges.pop(i)
				if g[u][v][m].get("spanning") is None:
					g[u][v][m]["spanning"] = False

			else:  # O(1)
				if not lightest_edges.get(ds.find(u)) or lightest_edges[ds.find(u)][3] > g[u][v][m]["weight"]:
					lightest_edges[ds.find(u)] = (u, v, m, g[u][v][m]["weight"])

				if not lightest_edges.get(ds.find(v)) or lightest_edges[ds.find(v)][3] > g[u][v][m]["weight"]:
					lightest_edges[ds.find(v)] = (u, v, m, g[u][v][m]["weight"])

		for u, v, m, w in lightest_edges.values():  # O(V)
			g[u][v][m]["spanning"] = True
			ds.union(u, v)
