import numpy as np 

from typing import * 
from numpy.typing import ArrayLike

import networkx as nx
G = nx.Graph()
G.add_nodes_from(range(4))
G.add_edges_from([[0,1], [1,2], [0,2], [1,3], [2,3]])

nx.draw(G, node_size=12)

R = np.array([], dtype=int)
P = np.fromiter(range(4), dtype=int)
X = np.array([], dtype=int)
#BronKerbosch(G, R = R, P = P, X = X)

def BronKerbosch(G, R: ArrayLike, P: ArrayLike, X: ArrayLike):
  print('here1')
  if P.size == 0 and X.size == 0:
    print(f"clique: {R}")
    yield R
  print('here2')
  for v in P:
    Nv = list(G.neighbors(v))
    # R, P, X = np.append(R, v), np.intersect1d(P, Nv), np.intersect1d(X, Nv)
    print(f"Before: R = {R}, P={P}, X={X}")
    R_, P_, X_ = np.append(R, v), np.intersect1d(P, Nv), np.intersect1d(X, Nv)
    print(f"Before2: R = {R_}, P={P_}, X={X_}")
    
    BronKerbosch(G, R_, P_, X_)
  
    P = np.setdiff1d(P, v)
    X = np.append(X, v)
    print(f"After: R = {R}, P={P}, X={X}")

list(BronKerbosch(G, R = R, P = P, X = X))