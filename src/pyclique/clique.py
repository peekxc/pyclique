# type: ignore
## Typing support 
from __future__ import annotations
from typing import *
from numpy.typing import ArrayLike

## Modules imports
import networkx as nx
import copy
import numpy as np 
import matplotlib.pyplot as plt
import heapq 

## Function imports
from networkx import Graph 
from collections import deque 
from array import array 
from .set_util import * 
from .meta import GraphLike, as_GraphLike

n_calls = 0

def maximal_cliques(G: Any, method: str = ["original", "pivot", "degeneracy"]):

	## Coerce G to graph-like, if not already. Acts as an assertion if otherwise. 	
	G = as_GraphLike(G) if not(isinstance(G, GraphLike)) else G

	global n_calls
	n_calls = 0
	R = array('I')
	P = array('I', range(len(G)))
	X = array('I')
	if method == "original" or method == ["original", "pivot", "degeneracy"]:
		return(list(BronKerbosch(G, R, P, X)))
	elif method == "pivot":
		get_pvt = pivot_init()
		return(list(BronKerboschPivot(G, R, P, X, get_pvt)))
	elif method == "degeneracy":
		return(list(BronKerboschDegeneracy(G, P, X)))
	else:
		raise ValueError(f"Unknown method '{method}' supplied")

def BronKerbosch(G: Graph, R: Collection, P: Collection, X: Collection): # Iterable, MutableSequence
	'''
	Basic Bron Kerbosch algorithm for enumerating maximal cliques. Used for testing purposes. 
	'''
	# assert (issorted(P) and issorted(X))
	global n_calls 
	n_calls += 1
	if len(P) == 0 and len(X) == 0:
		yield R
	for v in P:
		Nv = list(G.neighbors(v))
		R_, P_, X_ = union_sorted(R, [v]), intersect_sorted(P, Nv), intersect_sorted(X, Nv)
		yield from BronKerbosch(G, R_, P_, X_)
		P = set_diff(P, [v]) # np.setdiff1d(P, v)
		X = union_sorted(X, [v])

def pivot_random(G, P, X):
	""" choose a pivot u ∈ P ∪ X (no additional criteria) """
	return union_sorted(P, X)[0]

def pivot_min(G, P, X):
	""" choose a pivot u ∈ P ∪ X to minimize |P \ Γ(u)| """
	return min(((G.degree(v) v) for v in set_diff(P, X)), default=(0, None))[1]

def pivot_max(G, P, X):
	""" choose a pivot u ∈ P ∪ X to maximize |P ∩ Γ(u)| """
	return max(((G.degree(v), v) for v in union_sorted(P, X)), default=(0, None))[1]

def pivot_init(method=None):
	if not method:
		return pivot_random
	elif method == 'min_set_diff':
		return pivot_min
	elif method == 'max_intersect':
		return pivot_max
	else:
		raise Exception("Pivot method requested is invalid")

# https://www.ics.uci.edu/~goodrich/teach/graph/notes/Strash.pdf
def BronKerboschPivot(G: Graph, R: Collection, P: Collection, X: Collection, get_pvt=pivot_random):
	'''
	Bron Kerbosch algorithm with pivoting for enumerating maximal cliques. Used for testing purposes. 
	'''
	global n_calls 
	n_calls += 1
	if len(P) == 0 and len(X) == 0:
		yield R
	#_, u = max(((G.degree(v), v) for v in union_sorted(P, X)), default=(0, None)) 
	#Nu = G.neighbors(u) if u is not None else []
	Nu = G.neighbors(get_pvt(G, P, X)) if u is not None else []
	for v in set_diff(P, Nu):
		Nv = list(G.neighbors(v)) # neighbors of v 
		R_, P_, X_ = union_sorted(R, [v]), intersect_sorted(P, Nv), intersect_sorted(X, Nv)
		yield from BronKerboschPivot(G, R_, P_, X_)
		P = set_diff(P, [v])
		# assert not(v in X)
		X = union_sorted(X, [v])



def degeneracy(G: Graph):
	# N = G.copy()
	N = copy.deepcopy(G)
	n = len(N)
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
		W = set_diff(N.neighbors(v), L)
		W_deg = { w : N.degree(w) for w in W }
		N.remove_node(v)
		for w, w_deg in W_deg.items():
			D[w_deg].remove(w)
			heapq.heappush(D[N.degree(w)], w)
	return(dict(ordering=L, degeneracy=K))

def BronKerboschDegeneracy(G: Graph, P: Collection, X: Collection):
	global n_calls 
	n_calls += 1
	V = degeneracy(G)['ordering']
	for v in V:
		Nv = list(G.neighbors(v))
		P_, X_ = intersect_sorted(P, Nv), intersect_sorted(X, Nv)
		yield from BronKerboschPivot(G, [v], P_, X_)
		P = set_diff(P, [v])
		X = union_sorted(X, [v])
