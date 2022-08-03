# type: ignore
import numpy as np 
import networkx as nx

from typing import * 
from numpy.typing import ArrayLike
from networkx import Graph
from .clique import BronKerbosch, BronKerboschPivot, BronKerboschDegeneracy
from .set_util import intersect_sorted, list_intersect
#from .set_util_fast import _intersect_sorted
from .set_util_native import intersect_sorted_cython

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
