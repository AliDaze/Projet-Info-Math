from modules.open_digraph import *
ad_node_2 = node(3,"hamid_1",{},{2:1})
ad_node = node(2,"hamid_2",{3:1, 16:2},{16:1})
ad_node_3 = node(16,"hamid_3",{2:1},{2:2, 19:1})
ad_node_4 = node(19,"hamid_4",{16:1},{})
ad_node_5 = node(21,"hamid_33",{16:1},{2:1})
ad_node_2_2 = node(3,"hamid_1",{},{2:1})
ad_node_2_1 = node(2,"hamid_2",{3:1, 16:2},{16:1})
ad_node_2_3 = node(16,"hamid_3",{2:1},{2:2, 19:1})
ad_node_2_4 = node(19,"hamid_4",{16:1},{})
ad_node_2_5 = node(21,"hamid_33",{16:1},{2:1})
graph = open_digraph([3],[19],[ad_node,ad_node_2, ad_node_3, ad_node_4])

graph_2 = open_digraph([3],[19],[ad_node_2_1,ad_node_2_2, ad_node_2_3, ad_node_2_4, ad_node_2_5])

print(graph_2.well_formed())
print(graph.inputs)
print(graph.well_formed())
graph.add_node(" ",{2:3},{16:2})
print(graph.well_formed())
graph_2.add_node(" ",{2:3},{16:2})
print(graph_2.well_formed())
print(graph)
graph.remove_parallel_edges(16,2)
print(graph)
print(graph.well_formed())
print(graph.inputs)
graph.add_node_input(2)
print(graph.inputs)
print(graph.well_formed())
print("achou")
graph.add_node_output(2)
print(graph.well_formed())
graph.add_edge(16,2)
print(graph.well_formed())
'''
print([ad_node,ad_node_2, ad_node_3, ad_node_4])
print(ad_node)
print(graph)
print(node(3,"hamid",[3],[3]).copy())
print("hello world")
print(graph.get_id_node_map())
print(graph.get_nodes())
print(len(graph.get_nodes()))
print(graph.get_node_ids())
d={'a':1,'b':2, 'c':3}
print(d.keys())
print(d.values())
print(d['b'])
print(graph.get_nodes_by_ids([3]))
print(graph)
k=graph.new_id()
print(graph.new_id())
graph.add_node("hamid_5",{19:3}, {3:1})
print(graph)
k=graph.new_id()
print(graph.new_id())'''





	
