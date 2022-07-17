import numpy as np 

from typing import * 
from numpy.typing import ArrayLike

import networkx as nx
from networkx import Graph 
import matplotlib.pyplot as plt
from collections import deque 

G = nx.Graph()
G.add_nodes_from(range(4))
G.add_edges_from([[0,1], [1,2], [0,2], [1,3], [2,3]])

nx.draw(G, node_size=120)

issorted = lambda l: all(l[i] <= l[i+1] for i in range(len(l) - 1))

G = nx.fast_gnp_random_graph(25, 0.5)
nx.draw(G, node_size=120)

def maximal_cliques(G: Graph):
	R = np.array([], dtype=int)
	P = np.fromiter(range(len(G.nodes)), dtype=int)
	X = np.array([], dtype=int)
	return(deque(BronKerbosch(G, R, P, X)))
#return(deque(BronKerboschPivot(G, R, P, X)))

def BronKerbosch(G: Graph, R: ArrayLike, P: ArrayLike, X: ArrayLike):
	'''
	Basic Bron Kerbosch algorithm for enumerating maximal cliques. Used for testing purposes. 
	'''
	assert (issorted(P) and issorted(X))
	if P.size == 0 and X.size == 0:
		yield R
	for v in P:
		Nv = list(G.neighbors(v))
		R_, P_, X_ = np.append(R, v), np.intersect1d(P, Nv), np.intersect1d(X, Nv)
		yield from BronKerbosch(G, R_, P_, X_)
		P = np.setdiff1d(P, v)
		X = np.append(X, v)

def BronKerboschPivot(G: Graph, R: ArrayLike, P: ArrayLike, X: ArrayLike):
	'''
	Bron Kerbosch algorithm with pivoting for enumerating maximal cliques. Used for testing purposes. 
	'''
	if P.size == 0 and X.size == 0:
		yield R
	Nu = max((list(G.neighbors(v)) for v in np.union1d(P, X)), default=0)
	for v in np.setdiff1d(P, Nu):
		Nv = list(G.neighbors(v))
		R_, P_, X_ = np.append(R, v), np.intersect1d(P, Nv), np.intersect1d(X, Nv)
		yield from BronKerboschPivot(G, R_, P_, X_)
		P = np.setdiff1d(P, v)
		X = np.append(X, v)


d = max(nx.core_number(G).values())

maximal_cliques(G)


len(list(nx.find_cliques(G)))

import timeit 
# timeit.timeit(lambda x: )
#x = list(BronKerbosch(G, R = R, P = P, X = X))

# TODO:
# - benchmarks w/ timeit ; comparison with networkx find_cliques 
# - Make BK faster (how to do this)
# - Make variants of BK 
# - Make nice interface / package for it 
# - Supports multiple graph inputs / Protocol class for neighbors functionality? 
# - Really think about C++ variant / fast implementation 
# - Compare with other python clique implementations
# - Implements other maximal clique extensions if they are simple enough 
# - k clique problems




