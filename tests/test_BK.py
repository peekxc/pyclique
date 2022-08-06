import pyclique
import networkx as nx
import numpy as np

def test_BK_basic():
  G = nx.Graph()
  G.add_nodes_from(range(4))
  G.add_edges_from([[0,1], [1,2], [0,2], [1,3], [2,3]])
  assert pyclique.maximal_cliques(G) == [[0,1,2], [1,2,3]]