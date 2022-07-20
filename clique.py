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

max(nx.core_number(G).values())

## TODO: solve the degeneracy ordering problem 
min_degree_id = min(nx.degree(G), key=lambda d: d[1])[0]
G.nodes



def maximal_cliques(G: Graph):
	R = np.array([], dtype=int)
	P = np.fromiter(range(len(G.nodes)), dtype=int)
	X = np.array([], dtype=int)
	return(deque(BronKerbosch(G, R, P, X)))

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
		for clique in BronKerbosch(G, R_, P_, X_):
			yield clique
		P = np.setdiff1d(P, v)
		# assert not(v in X)
		X = np.append(X, v)

d = max(nx.core_number(G).values())



maximal_cliques(G)

len(list(nx.find_cliques(G)))

import timeit 
# timeit.timeit(lambda x: )
x = list(BronKerbosch(G, R = R, P = P, X = X))

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




# def degeneracy():

from array import array 
import heapq 
G = nx.fast_gnp_random_graph(10, 0.32)
pos =  nx.spring_layout(G) #nx.kamada_kawai_layout(G) #nx.planar_layout(G)
Gc = G.copy()

def degeneracy(G: Graph):
	n = len(G.nodes)
	L = array('I')
	D = [[] for i in range(n)]
	for i, (nid, deg) in enumerate(G.degree()):
		D[deg].append(nid)
	K = array('I')
	k = 0 
	for j in range(n):
		i = min(range(n), key=lambda i: i if len(D[i]) > 0 else n+1)
		assert len(D[i]) > 0
		k = max(k, i)
		#assert G.degree(v) == k
		K.append(k)
		v = heapq.heappop(D[i])
		L.append(v)
		W = np.setdiff1d(np.fromiter(G.neighbors(v), dtype=int), L)
		W_deg = dict(G.degree(W))
		G.remove_node(v)
		for w, w_deg in W_deg.items():
			D[w_deg].remove(w)
			heapq.heappush(D[G.degree(w)], w)

	L = np.array(L) # degeneracy order 
	K = np.array(K) # degeneracies
	return(dict(ordering=L, degeneracy=K))

K_core = np.fromiter(dict(sorted(zip(L,K))).values(), dtype=int)
nx.draw(Gc, with_labels=True, pos=pos,node_color=K_core)



def BronKerbosch3(G: Graph):
	P = 
	V = degeneracy(G)['ordering']
	R, X = [], []
	for each vertex v in a degeneracy ordering of G do
			BronKerbosch2({v}, P ⋂ N(v), X ⋂ N(v))
			P := P \ {v}
			X := X ⋃ {v}



L1 = [1,2,3,4]
L2 = [3,4,5,6]

head_l1 = 0
head_l2 = 0
for i in max(len(L1), len(L2)):
	L1[head_l1] < L2[head_l2]
	# pop L1[head_l1] to output list 
	# head_l1 ++ 


nx.draw(G, with_labels=True)