# type: ignore
from math import inf
from array import array
from typing import * 
#from typing import List,
from collections.abc import Iterable # keep after typing 

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

def intersect_sorted(A: Union[Iterable, ArrayLike], B: [Iterable, ArrayLike]):
	assert isinstance(A, Iterable) and isinstance(B, Iterable)
	
	## Specialize for numpy arrays
	value_typecode = None
	if isinstance(A, np.ndarray) and isinstance(B, np.ndarray):
		value_typecode = np.sctype2char(np.find_common_type([A.dtype], [B.dtype])) 
	
	## Use typed O(1) amortized-append container, if possible 
	C = [] if value_typecode is None else array(value_typecode)

	## The O(n) intersection
	Ag, Bg = _duck_iterable(A), _duck_iterable(B)
	a = next(Ag, None)
	b = next(Bg, None)
	while a is not None and b is not None:
		if a == b:
			C.append(a)
			a = next(Ag, None)
			b = next(Bg, None)
		elif a < b:
			a = next(Ag, None)
		elif a > b:
			b = next(Bg, None)
	return C

def list_intersect(A: Iterable, B: Iterable):
	Ag = (i for i in B)
	Bg = (i for i in B)
	C = []

	a = next(Ag, None)
	b = next(Bg, None)
	while a is not None and b is not None:
		if a == b:
			C.append(a)
			a = next(Ag, None)
			b = next(Bg, None)
		elif a < b:
			a = next(Ag, None)
		elif a > b:
			b = next(Bg, None)

	return C


def list_intersect2(A, B):
		Ag = (a for a in A)
		Bg = (b for b in B)
		C = []

		b = next(Bg)
		for a in Ag:
				if not b:
						break

				while a > b:
						print(f'> a:{a},b:{b}')
						b = next(Bg, None)
				if a == b:
						print(f'== a:{a},b:{b}')
						C.append(a)
						b = next(Bg, None)
						continue
				# consider removing elif
				#elif a < b:
				#    print(f'< a:{a},b:{b}')
				#    continue

		return C




# union
def list_union_unique(A, B):
		Ag = (a for a in A)
		Bg = (b for b in B)
		C = []

		a = next(Ag, inf)
		b = next(Bg, inf)
		c = -inf
		while a is not inf or b is not inf:
				if a == b:
						print(f'= a: {a}, b: {b}, c: {c}')
						if a > c:
								c = a
								C.append(c)
						a = next(Ag, inf)
						b = next(Bg, inf)
				elif a < b:
						print(f'< a: {a}, b: {b}, c: {c}')
						if a > c:
								c = a
								C.append(c)
						a = next(Ag, inf)
				elif a > b:
						print(f'> a: {a}, b: {b}, c: {c}')
						if b > c:
								c = b
								C.append(c)
						b = next(Bg, inf)

		return C
		



def list_union_duplicate(A, B):
		Ag = (a for a in A)
		Bg = (b for b in B)
		C = []

		a = next(Ag, inf)
		b = next(Bg, inf)
		c = -inf
		while a is not inf or b is not inf:
				if a <= b:
						print(f'= a: {a}, b: {b}, c: {c}')
						if a >= c:
								c = a
								C.append(c)
						a = next(Ag, inf)
				elif a > b:
						print(f'> a: {a}, b: {b}, c: {c}')
						if b >= c:
								c = b
								C.append(c)
						b = next(Bg, inf)

		return C


# set_diff
def set_diff_add(A, B):
	Bg = (b for b in B)
	C = []

	b = next(Bg, inf)
	last_added = None
	for a in A:
		while a > b:
			b = next(Bg, inf)

		if a == b:
			continue
		elif a < b and a != last_added:
			C.append(a)
			last_added = a

	return C
