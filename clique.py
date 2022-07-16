import numpy as np 

from typing import * 
from numpy.typing import ArrayLike

import networkx as nx
from networkx import Graph 
from collections import deque 

G = nx.Graph()
G.add_nodes_from(range(4))
G.add_edges_from([[0,1], [1,2], [0,2], [1,3], [2,3]])

nx.draw(G, node_size=12)

R = np.array([], dtype=int)
P = np.fromiter(range(4), dtype=int)
X = np.array([], dtype=int)

issorted = lambda l: all(l[i] <= l[i+1] for i in range(len(l) - 1))

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
    for clique in BronKerbosch(G, R_, P_, X_):
      yield clique
    P = np.setdiff1d(P, v)
    X = np.append(X, v)

G = nx.fast_gnp_random_graph(50, 0.5)
len(list(nx.find_cliques(G)))

def maximal_cliques(G: Graph):
  R = np.array([], dtype=int)
  P = np.fromiter(range(len(G.nodes)), dtype=int)
  X = np.array([], dtype=int)
  return(deque(BronKerbosch(G, R, P, X)))

import timeit 
timeit.timeit(lambda x: )
x = list(BronKerbosch(G, R = R, P = P, X = X))

