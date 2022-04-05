from modules.open_digraph import *




M=(random_triangular_int_matrix(7,3))
'''for i in range(4):
print(M[i])
print("\n")'''

'''(M=[ [0, 1, 1, 0, 0],
[0, 0, 0, 1, 2],
[0, 0, 0, 2, 0],
[1, 0, 0, 0, 1],
[0, 0, 0, 0, 0] ]'''
M2=(random_triangular_int_matrix(4,2)) 
M3=(random_triangular_int_matrix(7,4)) 
G=graph_from_adjacency_matrix(M,7)
G3=graph_from_adjacency_matrix(M3,7)
G2=graph_from_adjacency_matrix(M2,4)
#print(G)
#G.shift_indices(10)
#print("\n \n")
#print(G)
#print(G.djikstra(10))
#node4=G.get_node_by_id(10)
#print(G.distance_ancetres(15,14))
#print(G.trie_topologique())
#print(f"profondeur noeud = {(G.profondeur_noeud(G.get_node_by_id(11)))}" )
#print("profondeur g = ",(G.profondeur_graph()))
#path,dist=G.longest_path(10,15)
#print(path)
#print(dist)
k=bool_circ.origin()


g=k.parse_parentheses("((x0)&((x1)&(x2)))|((x1)&(~(x2)))", "((x0)&(~(x1)))|(x2)")

g.display(True)




#print(G.is_well_formed())
#G.display(True)
#G2.display(True)

#G.iparralel_list(G2,G3)
#k,g_dict=G.connected_components()
#print(k)
#print(g_dict)
#list_g=G.connnexe_compose()
#G.display(True)
#for i in g_list:
#	i.display()
#G0=random_graph(7,2,form="DAG")
#for k in list_g:
#	k.display(True)

#G.remove_node_by_id(10)
#G.display(True)
#G.save_as_dot_file("/home/tp-home002/gkemich/Documents/Projet-Info-Math/mm.dot",verbose=False)
#G2=open_digraph.from_dot_file("/home/tp-home002/gkemich/Documents/Projet-Info-Math/mm.dot")
#G2.display(True)
#print(g_new.is_well_formed())
#print(g_new)
