import pyclique 
import networkx as nx 
import timeit
import matplotlib.pyplot as plt 

## We're around 24x slower than networkx so far 
G = nx.fast_gnp_random_graph(150, 0.35)
time_nx = timeit.timeit(lambda: list(nx.find_cliques(G)), number=20)
time_pc = timeit.timeit(lambda: pyclique.maximal_cliques(G), number=20)



