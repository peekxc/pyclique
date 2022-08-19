import pyclique 
import networkx as nx 
import timeit
import matplotlib.pyplot as plt 

## We're around 24x slower than networkx so far 
G = nx.fast_gnp_random_graph(150, 0.35)
time_nx = timeit.timeit(lambda: list(nx.find_cliques(G)), number=20)
time_pc = timeit.timeit(lambda: pyclique.maximal_cliques(G), number=20)




from pyclique.set_util import _set_diff_sorted_inplace as setdiff_inplace1
from pyclique.set_util_typed import _set_diff_sorted_inplace as setdiff_inplace2


type(setdiff_inplace1)
type(setdiff_inplace2)

import numpy as np 
import copy
X1 = sorted(np.random.choice(range(30000*5), size=30000).tolist())
X2 = copy.deepcopy(X1)
X3 = copy.deepcopy(X1)

Y = sorted(np.random.choice(X1, size=10000).tolist())
assert(all([y in X1 for y in Y]))

print(timeit.timeit(lambda: pyclique.set_diff_sorted(X3, Y), number=100))
print(timeit.timeit(lambda: setdiff_inplace1(X1, iter(Y)), number=100))
print(timeit.timeit(lambda: setdiff_inplace2(X2, iter(Y)), number=100))


L = [1,2,3,4,5,6,7,9,16,18,21]
setdiff_inplace1(L, iter([1,3,5,7,9,10,11,16]))
print(L)
