# cython: language_level=3, boundscheck=False, wraparound=False, initializedcheck=False, cdivision=True
# distutils: language=c++
# from typing import List
from libcpp.vector cimport vector
from cpython cimport array


cpdef _intersect_sorted_cython(int[:] A, int[:] B):
	cdef int i = 0 
	cdef int j = 0 
	cdef vector[int] C
	while i < A.shape[0] and j < B.shape[0]:
		if A[i] == B[j]:
			C.push_back(A[i])
			i += 1
			j += 1
		elif A[i] < B[j]:
			i += 1
		else:
			j += 1
	return(C)