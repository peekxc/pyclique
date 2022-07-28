G = nx.Graph()
G.add_nodes_from(range(4))
G.add_edges_from([[0,1], [1,2], [0,2], [1,3], [2,3]])

nx.draw(G, node_size=120)

issorted = lambda l: all(l[i] <= l[i+1] for i in range(len(l) - 1))

G = nx.fast_gnp_random_graph(25, 0.5)
nx.draw(G, node_size=120)

max(nx.core_number(G).values())

## TODO: solve the degeneracy ordering problem 
min_degree_id = min(nx.degree(G), key=lambda d: d[1])[0]


sorted(maximal_cliques(G, 'original'), key=lambda L: (len(L), *L))

sorted(maximal_cliques(G, 'pivot'), key=lambda L: (len(L), *L))

sorted(maximal_cliques(G, 'degeneracy'), key=lambda L: (len(L), *L))



# degeneracy(G)['ordering']
# degeneracy(G)['degeneracy']
# K_core = np.fromiter(dict(sorted(zip(L,K))).values(), dtype=int)
# nx.draw(Gc, with_labels=True, pos=pos,node_color=K_core)




# L1 = [1,2,3,4]
# L2 = [3,4,5,6]

# head_l1 = 0
# head_l2 = 0
# for i in max(len(L1), len(L2)):
# 	L1[head_l1] < L2[head_l2]
# 	# pop L1[head_l1] to output list 
# 	# head_l1 ++ 


# nx.draw(G, with_labels=True)

# G = nx.fast_gnp_random_graph(10, 0.32)
# pos =  nx.spring_layout(G) #nx.kamada_kawai_layout(G) #nx.planar_layout(G)