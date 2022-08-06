# type: ignore
from math import inf
from array import array
from typing import * 
from collections.abc import Iterable # keep after typing 
from .set_util_native import intersect_sorted_cython

import numpy as np
from numpy.typing import ArrayLike

def _duck_iterable(x: Iterable):
	try:
		iterator = iter(x)
	except TypeError:
		raise ValueError("Invalid argument: must be iterable")
	else:
		return(iterator)

def _intersect_index(A, B):
	i,j,C = 0,0,[]
	while i < len(A) and j < len(B):
		if A[i] == B[j]:
			C.append(A[i])
			i += 1
			j += 1
		elif A[i] < B[j]:
			i += 1
		else:
			j += 1
	return(C)

def intersect_sorted(A: Union[Iterable, ArrayLike], B: Union[Iterable, ArrayLike]):
	assert isinstance(A, Iterable) and isinstance(B, Iterable)
	
	## Specialize for numpy arrays
	value_typecode = None
	if isinstance(A, np.ndarray) and isinstance(B, np.ndarray):
		value_typecode = np.sctype2char(np.find_common_type([A.dtype], [B.dtype])) 
		if value_typecode == 'i':
			return intersect_sorted_cython(A, B)		

	## Use typed O(1) amortized-append container, if possible 
	C = [] if value_typecode is None else array(value_typecode)

	## The O(n) intersection
	Ag, Bg = _duck_iterable(A), _duck_iterable(B)
	a, b = next(Ag, None), next(Bg, None)
	while a is not None and b is not None:
		if a == b:
			C.append(a)
			a, b = next(Ag, None), next(Bg, None) 
		elif a < b:
			a = next(Ag, None)
		elif a > b:
			b = next(Bg, None)
	return C

def list_intersect(A: Iterable, B: Iterable):
	Ag, Bg = _duck_iterable(A), _duck_iterable(B)
	C = []
	a, b = next(Ag, None), next(Bg, None)
	while a is not None and b is not None:
		if a == b:
			C.append(a)
			a, b = next(Ag, None), next(Bg, None) 
		elif a < b:
			a = next(Ag, None)
		else:
			b = next(Bg, None)
	return C

def union_sorted(A, B, duplicates: bool = False):
	A, B, C = _duck_iterable(A), _duck_iterable(B), [] 
	a, b = next(A, inf), next(B, inf)
	while a is not inf or b is not inf:
		if a == b:
			C.extend([a] if not(duplicates) else [a, a])
			a, b = next(A, inf), next(B, inf)
		else:
			if duplicates or (len(C) == 0 or min(a,b) != C[-1]):
				C.append(min(a,b))
			a, b = (next(A, inf), b) if a < b else (a, next(B, inf))
	return C

def advance_until(A: Iterator, P: Callable, default: Optional = None):
	"""
	Adavnces 'A' until 'P' holds, returning the value where P first held and the remaining iterator, if it exists
	
	Return: 
		- a := the first value where P(a) == True 
		- A := portion of A not encountered prior to P
	"""
	# A = _duck_iterable(A) if not(isinstance(A, Iterator)) else A
	assert isinstance(A, Iterator)
	# from itertools import chain
	while not P((a := next(A, default))):
		pass 
	return a, A

# set_diff
def set_diff(A: Iterable, B: Iterable):
	A, B, C = _duck_iterable(A), _duck_iterable(B), []
	b = next(B, inf)
	last_added = None
	for a in A:
		while a > b:
			b = next(B, inf)
		if a != b and a != last_added:
			C.append(a)
			last_added = a
	return C
