from typing import *
# from math import inf
import sys 

INT_INF: Final[int] = sys.maxsize


def _set_diff_sorted_inplace(A: MutableSequence[int], B: Iterable[int]) -> None: # Iterable[int]
  B_iter: Iterator[int] = iter(B)
  b: int = next(B_iter, INT_INF)
  i: int = 0
  while(b != INT_INF):
    a: int = A[i]
    while b < a: b = next(B_iter, INT_INF) # advance b while b not in A 
    if a == b:
      del A[i]
      b = next(B_iter, INT_INF)
    else:
      i += 1
