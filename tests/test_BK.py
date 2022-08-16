import pyclique
import networkx as nx
import numpy as np
from typing import * 

def test_empty():
	try:
		pyclique.maximal_cliques(nx.Graph())
	except Exception as e:
		assert False 

def test_BK_basic():
	G = nx.Graph()
	G.add_nodes_from(range(4))
	G.add_edges_from([[0,1], [1,2], [0,2], [1,3], [2,3]])
	assert pyclique.maximal_cliques(G) == [[0,1,2], [1,2,3]]

def test_BK_medium():
	G = nx.fast_gnp_random_graph(25, 0.5)
	max_cliques_truth = list(nx.find_cliques(G))
	max_cliques_truth = sorted([sorted(clique) for clique in max_cliques_truth])
	assert isinstance(max_cliques_truth, List)

	max_cliques_test = pyclique.maximal_cliques(G)
	max_cliques_test = sorted([sorted(clique) for clique in max_cliques_test])
	assert max_cliques_test == max_cliques_truth

def test_BK_methods():
	G = nx.fast_gnp_random_graph(25, 0.5)
	max_cliques_truth = list(nx.find_cliques(G))
	max_cliques_truth = sorted([sorted(clique) for clique in max_cliques_truth])
	assert isinstance(max_cliques_truth, List)

	max_cliques_test = pyclique.maximal_cliques(G, "original")
	max_cliques_test = sorted([sorted(clique) for clique in max_cliques_test])
	assert max_cliques_test == max_cliques_truth

	max_cliques_test = pyclique.maximal_cliques(G, "pivot")
	max_cliques_test = sorted([sorted(clique) for clique in max_cliques_test])
	assert max_cliques_test == max_cliques_truth

	max_cliques_test = pyclique.maximal_cliques(G, "degeneracy")
	max_cliques_test = sorted([sorted(clique) for clique in max_cliques_test])
	assert max_cliques_test == max_cliques_truth

# [ ] test different pivot algorithms (should be in tests/ folder)
# [ ] time it with timeit.timeit and a lambda (zero-arity) run between 100 and 1000

def test_BK_calls():
	G = nx.fast_gnp_random_graph(25, 0.5)
	C = pyclique.maximal_cliques(G, "original")
	print(pyclique.clique.n_calls)
	C = pyclique.maximal_cliques(G, "pivot")
	print(pyclique.clique.n_calls)
	C = pyclique.maximal_cliques(G, "degeneracy")
	print(pyclique.clique.n_calls)
	print(f"# of cliques: {len(C)}")


def test_BK_adj_matrix():
	G = nx.fast_gnp_random_graph(25, 0.5)
	D = nx.to_scipy_sparse_array(G).todense()
	max_cliques_truth = list(nx.find_cliques(G))
	max_cliques_truth = sorted([sorted(clique) for clique in max_cliques_truth])
	assert isinstance(max_cliques_truth, List)

	max_cliques_test = pyclique.maximal_cliques(D)
	max_cliques_test = sorted([sorted(clique) for clique in max_cliques_test])
	assert max_cliques_test == max_cliques_truth
