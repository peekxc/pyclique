import numpy as np 

from typing import * 
from numpy.typing import ArrayLike

import networkx as nx
from networkx import Graph 
import matplotlib.pyplot as plt
from collections import deque 

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

def maximal_cliques(G: Graph, method: str = ["original", "pivot", "degeneracy"]):
	R = np.array([], dtype=int)
	P = np.fromiter(range(len(G.nodes)), dtype=int)
	X = np.array([], dtype=int)
	if method == "original" or method == ["original", "pivot", "degeneracy"]:
		return(list(BronKerbosch(G, R, P, X)))
	elif method == "pivot":
		return(list(BronKerboschPivot(G, R, P, X)))
	elif method == "degeneracy":
		return(list(BronKerboschDegeneracy(G, P, X)))
	else:
		raise ValueError(f"Unknown method '{method}' supplied")