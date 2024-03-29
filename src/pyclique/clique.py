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

from pyclique.utility import counted 
from .set_util import * 
from .meta import GraphLike, as_GraphLike

n_calls = 0

## TODO: determine if G is read-only, a stream, modifiable, etc...
def maximal_cliques(G: Any, method: str = ["original", "pivot", "degeneracy"], **kwargs):

	## Coerce G to graph-like, if not already. Acts as an assertion if otherwise. 	
	G = as_GraphLike(G) if not(isinstance(G, GraphLike)) else G

	global n_calls
	n_calls = 0
	R = array('I')
	P = array('I', range(len(G)))
	X = array('I')
	if method == "original" or method == ["original", "pivot", "degeneracy"]:
		yield from BronKerbosch(G, R, P, X)
	elif method == "pivot":
		get_pvt = pivot_init(**kwargs)
		yield from BronKerboschPivot(G, R, P, X, get_pvt)
	elif method == "degeneracy":
		yield from BronKerboschDegeneracy(G, P, X)
	else:
		raise ValueError(f"Unknown method '{method}' supplied")

# @counted(True)
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
		Nv = list(G.neighbors(v)) # neighbors of v 
		R_, P_, X_ = union_sorted(R, [v]), intersect_sorted(P, Nv), intersect_sorted(X, Nv)
		yield from BronKerbosch(G, R_, P_, X_)
		P = set_diff_sorted(P, [v]) # np.setdiff1d(P, v)
		X = union_sorted(X, [v])

def pivot_random(G, P, X) -> Optional[int]:
	""" 
	Choose a pivot u ∈ P ∪ X (no additional criteria) 
	If no such pivot exists (e.g. P and X are empty), returns None. 
	"""
	px = union_sorted(P, X)
	return px[0] if len(px) > 0 else None

def pivot_min(G, P, X) -> Optional[int]:
	""" 
	Choose a pivot u ∈ P ∪ X to minimize |P \\ Γ(u)| 
	If no such pivot exists (e.g. P and X are empty), returns None. 
	"""
	return min(((G.degree(v), v) for v in set_diff_sorted(P, X)), default=(0, None))[1]

def pivot_max(G, P, X) -> Optional[int]:
	""" 
	Choose a pivot u ∈ P ∪ X to maximize |P ∩ Γ(u)| 
	If no such pivot exists (e.g. P and X are empty), returns None. 
	"""
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
	u = get_pvt(G, P, X)
	Nu = G.neighbors(u) if u is not None else []
	for v in set_diff_sorted(P, Nu):
		Nv = list(G.neighbors(v)) # neighbors of v 
		R_, P_, X_ = union_sorted(R, [v]), intersect_sorted(P, Nv), intersect_sorted(X, Nv)
		yield from BronKerboschPivot(G, R_, P_, X_)
		P = set_diff_sorted(P, [v])
		# assert not(v in X)
		X = union_sorted(X, [v])

def degeneracy(G: Graph):
	### G must have .degree, .remove_node, neighbors
	# N = G.copy()
	N = copy.deepcopy(G)
	n = len(N)
	L = array('I')
	D = [[] for i in range(n)]
	for i, (nid, deg) in enumerate(N.degree()):
		D[deg].append(nid)
	K = array('I')
	k = 0 
	for d in D:
		i = min(range(n), key=lambda i: i if len(d) > 0 else n+1)
		assert len(d) > 0
		k = max(k, i)
		K.append(k)
		v = heapq.heappop(d)
		L.append(v)
		W = set_diff_sorted(N.neighbors(v), L)
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
		P = set_diff_sorted(P, [v])
		X = union_sorted(X, [v])
