# cython: language_level=3, boundscheck=False, wraparound=False, initializedcheck=False, cdivision=True
# distutils: language=c++
# from typing import List
from libcpp.vector cimport vector
from cpython cimport array

from cpython cimport array
import array


cdef _intersect_sorted_cython(int[:] A, int[:] B, vector[int]& C):
	cdef int i = 0 
	cdef int j = 0 
	while i < A.shape[0] and j < B.shape[0]:
		if A[i] == B[j]:
			C.push_back(A[i])
			i += 1
			j += 1
		elif A[i] < B[j]:
			i += 1
		else:
			j += 1

cpdef intersect_sorted_cython(int[:] A, int[:] B):
	cdef vector[int] C
	C.reserve(min(A.shape[0], B.shape[0]))
	_intersect_sorted_cython(A, B, C)
	return(C)