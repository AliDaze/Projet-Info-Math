from modules.open_digraph import *




M=(random_triangular_int_matrix(4,10))
'''for i in range(4):
print(M[i])
print("\n")'''

'''(M=[ [0, 1, 1, 0, 0],
[0, 0, 0, 1, 2],
[0, 0, 0, 2, 0],
[1, 0, 0, 0, 1],
[0, 0, 0, 0, 0] ]'''
G=graph_from_adjacency_matrix(M,4)
print(G)
#print(G.is_well_formed())
G.display(True)
G.save_as_dot_file("/home/tp-home002/gkemich/Documents/Projet-Info-Math/mm.dot",verbose=False)
G2=open_digraph.from_dot_file("/home/tp-home002/gkemich/Documents/Projet-Info-Math/mm.dot")
G2.display(True)
#print(g_new.is_well_formed())
#print(g_new)
