## Typing support 
from typing import * 
from numpy.typing import ArrayLike

## Modules imports
import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt
import heapq 

## Function imports
from networkx import Graph 
from collections import deque 
from array import array 

def BronKerbosch(G: Graph, R: ArrayLike, P: ArrayLike, X: ArrayLike):
	'''
	Basic Bron Kerbosch algorithm for enumerating maximal cliques. Used for testing purposes. 
	'''
	# assert (issorted(P) and issorted(X))
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
		# assert not(v in X)
		X = np.append(X, v)

def degeneracy(G: Graph):
	N = G.copy()
	n = len(N.nodes)
	L = array('I')
	D = [[] for i in range(n)]
	for i, (nid, deg) in enumerate(N.degree()):
		D[deg].append(nid)
	K = array('I')
	k = 0 
	for j in range(n):
		i = min(range(n), key=lambda i: i if len(D[i]) > 0 else n+1)
		assert len(D[i]) > 0
		k = max(k, i)
		K.append(k)
		v = heapq.heappop(D[i])
		L.append(v)
		W = np.setdiff1d(np.fromiter(N.neighbors(v), dtype=int), L)
		W_deg = dict(N.degree(W))
		N.remove_node(v)
		for w, w_deg in W_deg.items():
			D[w_deg].remove(w)
			heapq.heappush(D[N.degree(w)], w)

	L = np.array(L) # degeneracy order 
	K = np.array(K) # degeneracies
	return(dict(ordering=L, degeneracy=K))

def BronKerboschDegeneracy(G: Graph, P: ArrayLike, X: ArrayLike):
	V = degeneracy(G)['ordering']
	for v in V:
		Nv = list(G.neighbors(v))
		P_, X_ =  np.intersect1d(P, Nv), np.intersect1d(X, Nv)
		yield from BronKerboschPivot(G, np.array([v]), P_, X_)
		P = np.setdiff1d(P, v)
		X = np.append(X, v)
