from pyclique import *

# def bench_intersect():
  # import pyclique
  # import timeit
  # import numpy as np
  # x = [3,4,5,6,8,9,18]
  # y = [3,5,8,13,14,32]
  # from pyclique import intersect_sorted, list_intersect
  # from pyclique import intersect_sorted_cython

  # arr_sz, alphabet_sz = 100000, 3500000
  # x = np.sort(np.random.choice(range(arr_sz), alphabet_sz)).astype(np.int32)
  # y = np.sort(np.random.choice(range(arr_sz), alphabet_sz)).astype(np.int32)

  # timeit.timeit(lambda: np.intersect1d(x, y), number=100)  
  # timeit.timeit(lambda: intersect_sorted(x, y), number=100)  
  # timeit.timeit(lambda: list_intersect(x, y), number=100)
  # timeit.timeit(lambda: intersect_sorted_cython(x,y), number=100)  
  # x_np, y_np = np.array(x), np.array(y)
  # np.asarray(intersect_sorted(x, y))

def test_list_intersect():
	assert list_intersect([1,2,3,4], [5,6,7,8]) == []
	assert list_intersect([1,2,3,4], [3,4,5,6]) == [3,4]
	assert list_intersect([1,2,3,4], [3,4]) == [3,4]
	assert list_intersect([1,5,9], [2,5,10]) == [5]
	assert list_intersect([1,2,3,4,5,6,7,8,9,10], [2,9]) == [2,9]

def test_union_unique():
	assert union_sorted([1,2,3,4], [5,6,7,8]) == [1,2,3,4,5,6,7,8]
	assert union_sorted([1,2,3,4], [3,4,5,6]) == [1,2,3,4,5,6]
	assert union_sorted([1,2,3,4], [3,4]) == [1,2,3,4]
	assert union_sorted([1,5,9], [2,5,10]) == [1,2,5,9,10]
	assert union_sorted([1,2,3,4,5,6,7,8,9,10], [2,9]) == [1,2,3,4,5,6,7,8,9,10]
	assert union_sorted([1,7,9], [2,5,6]) == [1,2,5,6,7,9]
	assert union_sorted([0,0,0,0,5,9,1037], [5,27,28,29,107]) == [0,5,9,27,28,29,107,1037]

def test_union_duplicate():
	p = dict(duplicates=True)
	assert union_sorted([1,2,3,4], [5,6,7,8], **p) == [1,2,3,4,5,6,7,8]
	assert union_sorted([1,2,3,4], [3,4,5,6], **p) == [1,2,3,3,4,4,5,6]
	assert union_sorted([1,2,3,4], [3,4], **p) == [1,2,3,3,4,4]
	assert union_sorted([1,5,9], [2,5,10], **p) == [1,2,5,5,9,10]
	assert union_sorted([1,2,3,4,5,6,7,8,9,10], [2,9], **p) == [1,2,2,3,4,5,6,7,8,9,9,10]
	assert union_sorted([1,7,9], [2,5,6], **p) == [1,2,5,6,7,9]
	assert union_sorted([0,0,0,0,5,9,1037], [5,27,28,29,107], **p) == [0,0,0,0,5,5,9,27,28,29,107,1037]


def test_set_diff():
	assert set_diff([1,2,3,4], [5,6,7,8]) == [1,2,3,4]
	assert set_diff([1,2,3,4], [3,4,5,6]) == [1,2]
	assert set_diff([1,2,3,4], [3,4]) == [1,2]
	assert set_diff([1,5,9], [2,5,10]) == [1,9]
	assert set_diff([1,2,3,4,5,6,7,8,9,10], [2,9]) == [1,3,4,5,6,7,8,10]
	assert set_diff([1,7,9], [2,5,6]) == [1,7,9]
	assert set_diff([0,0,0,0,5,9,1037], [5,27,28,29,107]) == [0,9,1037]

