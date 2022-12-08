import numpy as np
from typing import * 
from .utility import inverse_choose
from numpy.typing import ArrayLike


## Implementation details 
## Can distinguish if G is simple, i.e. no self loops?
# Adjacency matrix | ArrayLike  (n x n), symmetric 
# Adjacency list   | Sequence[Collection[int]]
# Edge list        | ArrayLike (m x 2) -- unique? pairs? List[Tuple(int, int)]?
# Incidence matrix | ArrayLike (n x m), non-symmetric
# Sparse Matrix 	 | Scipy issparse 	
# Pairwise dist.   | ArrayLike (n choose 2, 1)
# Iterable[Tuple[int, int]]
# Generator[Tuple[int, int]]

def is_adj_matrix(A: Any) -> bool:
	return(isinstance(A, np.ndarray) and len(A.shape) == 2 and np.prod(A.shape) == A.shape[0]**len(A.shape) and all(np.diag(A) == 0) and all(np.ravel(A == A.T)))

def is_adj_list(A: Any) -> bool:
	return(isinstance(A, Sequence[Collection[int]]))

def is_edge_list(A: Any) -> bool:
	return(isinstance(A, Sequence[Tuple[int, int]]))

def is_inc_matrix(A: Any) -> bool:
	return(isinstance(A, np.ndarray) and len(A.shape) == 2 and any(np.ravel(A != A.T)))

def is_pairwise_distances(x: ArrayLike) -> bool:
	''' Checks whether 'x' is a 1-d array of pairwise distances '''
	x = np.array(x, copy=False) # don't use asanyarray here
	if x.ndim > 1: return(False)
	n = inverse_choose(len(x), 2)
	return(x.ndim == 1 and n == int(n))

from typing import Protocol
@runtime_checkable
class GraphLike(Protocol):
	def __init__(self, **kwargs) -> None: pass
	def __len__() -> int: pass
	def neighbors(self, v: int) -> Iterable: pass
	def degree(v: int) -> int: 
		raise NotImplementedError

@runtime_checkable
class EditableGraphLike(GraphLike, Protocol):
	def remove_node(v: int) -> None: 
		raise NotImplementedError

## Fun exercise: how to bootstrap these wrapper classes ?
# For assigning __len__, see: https://stackoverflow.com/questions/13012159/how-create-a-len-function-on-init
from functools import partial
class GraphFactory():
	def __init__(self, G: Any, Len: Callable, Neighbors: Callable, Degree: Callable, Remove: Callable = None) -> None:
		self.G = G
		self.L = Len
		self.neighbors = partial(Neighbors, G)
		self.degree = partial(Degree, G)
		if Remove is not None: 
			self.remove_node = partial(Remove, G)

	def __len__(self): return(self.L(self.G))

def as_GraphLike(G: Any) -> GraphLike:
	if is_adj_matrix(G):
		am_len = lambda D: D.shape[0]
		am_neighbors = lambda D, v: np.flatnonzero(D[v,:]) if (v >= 0 and v < D.shape[0]) else np.array([])
		am_degree = lambda D, v: len(np.flatnonzero(D[v,:])) if (v >= 0 and v < D.shape[0]) else 0
		# def am_remove(D, v):
		# 	D[:,v] = D[v,:] = 0
		# 	return(None)

		GF = GraphFactory(G=G, Len=am_len, Neighbors=am_neighbors, Degree=am_degree)
		return(GF)
	else:
		raise NotImplementedError
	
