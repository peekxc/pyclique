from typing import List

def _intersect_sorted(A: List[int], B: List[int]) -> List[int]:
	i: int = 0
	j: int = 0
	C: List[int] = []
	while i < len(A) and j < len(B):
		if A[i] == B[j]:
			C.append(A[i])
		elif A[i] < B[j]:
			i += 1
		else:
			j += 1
	return(C)