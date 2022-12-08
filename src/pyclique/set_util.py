# type: ignore
import copy
import enum
from array import array
from collections.abc import Iterable  # keep after typing
from math import inf
from typing import *

import numpy as np
from numpy.typing import ArrayLike

# from .set_util_native import intersect_sorted_cython


def _duck_iterable(x: Iterable):
	try:
		iterator = iter(x)
	except TypeError:
		raise ValueError("Invalid argument: must be iterable")
	else:
		return(iterator)

def advance_until(A: Iterator, P: Callable, default: Optional = None):
	"""
	Adavnces 'A' until 'P' holds, returning the value where P first held and the remaining iterator, if it exists
	
	Returns a tuple (a, A), where: 
		a := the first value where P(a) == True 
		A := A-iterator pointing to the next value after a
	"""
	# A = _duck_iterable(A) if not(isinstance(A, Iterator)) else A
	assert isinstance(A, Iterator)
	# from itertools import chain
	while not P((a := next(A, default))):
		pass 
	return a, A
	
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

## -- Intersection algorithms --

def _intersect_sorted(A: Iterable, B: Iterable, C: MutableSequence):
	""" 	
	Given two Iterables 'A' and 'B', writes the elements that lie in both to the output 'C'
	"""
	assert isinstance(A, Iterable) and isinstance(B, Iterable)
	A, B = _duck_iterable(A), _duck_iterable(B)
	a, b = next(A, None), next(B, None)
	while a is not None and b is not None:
		if a == b:
			C.append(a)
			a, b = next(A, None), next(B, None) 
		elif a < b:
			a = next(A, None)
		else:
			b = next(B, None)

def _intersect_sorted_inplace(A: MutableSequence, B: Iterable):
	""" 	
	Linear-time sorted intersection
	"""
	_set_diff_sorted_inplace(A, B)

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

	## The O(n) intersection algorithm
	_intersect_sorted(A, B, C)
	return(C)

## -- Union algorithms --

def _union_sorted_inplace(A: MutableSequence, B: Iterable):
	""" 	
	Linear-time sorted intersection
	"""
	Ac = copy.deepcopy(A)
	_intersect_sorted_inplace(Ac, B)
	A.extend(Ac)

def _union_sorted(A: Iterable, B: Iterable, C: MutableSequence, duplicates: bool = False):
	a, b = next(A, inf), next(B, inf)
	while a is not inf or b is not inf:
		if a == b:
			C.extend([a] if not(duplicates) else [a, a])
			a, b = next(A, inf), next(B, inf)
		else:
			if duplicates or (len(C) == 0 or min(a,b) != C[-1]):
				C.append(min(a,b))
			a, b = (next(A, inf), b) if a < b else (a, next(B, inf))

def union_sorted(A: Union[Iterable, MutableSequence], B: Iterable, duplicates: bool = False, inplace: bool = False):
	assert isinstance(A, Iterable) and isinstance(A, Iterable), "A,B must at least be Iterables"
	
	## If inplace=True, A must be Mutable
	if inplace:
		assert isinstance(A, MutableSequence), "A must be mutable if inplace=True"
		_union_sorted_inplace(A, B, duplicates)
		C = A
	else: 
		A, B, C = _duck_iterable(A), _duck_iterable(B), []
		_union_sorted(A, B, C, duplicates)
	return(C)

## -- Set difference algorithms --
def _set_diff_sorted(A: Iterable, B: Iterable, C: MutableSequence):
	b = next(B, inf)
	last_added = None
	for a in A:
		while a > b:
			b = next(B, inf)
		if a != b and a != last_added:
			C.append(a)
			last_added = a

def _set_diff_sorted_inplace(A: MutableSequence, B: Iterable):
	b = next(B, inf)
	i = 0
	while(b != inf):
		a = A[i]
		while b < a: b = next(B, inf) # advance b while b not in A 
		if a == b:
			del A[i]
			b = next(B, inf)
		else:
			i += 1

def set_diff_sorted(A: Iterable, B: Iterable):
	A, B, C = _duck_iterable(A), _duck_iterable(B), []
	_set_diff_sorted(A, B, C)
	return(C)

def set_diff(A: Iterable, B: Iterable):
	A, B = list(A), list(B)
	return [A.remove(b) for b in B if b in A]

# def argmax(A: Iterable, key: Callable):
# 	A = _duck_iterable(A)
