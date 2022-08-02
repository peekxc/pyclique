# type: ignore
import numpy as np 
import networkx as nx

from typing import * 
from numpy.typing import ArrayLike
from networkx import Graph
from .clique import BronKerbosch, BronKerboschPivot, BronKerboschDegeneracy
from .set_util import intersect_sorted, list_intersect
#from .set_util_fast import _intersect_sorted
from .set_util_native import _intersect_sorted_cython

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


def test_set_diff_add():
		assert set_diff_add([1,2,3,4], [5,6,7,8]) == [1,2,3,4]
		assert set_diff_add([1,2,3,4], [3,4,5,6]) == [1,2]
		assert set_diff_add([1,2,3,4], [3,4]) == [1,2]
		assert set_diff_add([1,5,9], [2,5,10]) == [1,9]
		assert set_diff_add([1,2,3,4,5,6,7,8,9,10], [2,9]) == [1,3,4,5,6,7,8,10]
		assert set_diff_add([1,7,9], [2,5,6]) == [1,7,9]
		assert set_diff_add([0,0,0,0,5,9,1037], [5,27,28,29,107]) == [0,9,1037]
