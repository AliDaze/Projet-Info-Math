import random
import sys
import os
import webbrowser

from open_diagraph_matrix import *
from open_digraph import *
from node import *

class open_diagraph_parralelcompose_mx:
	
    def iparralel(self,g):
        max_id_g=g.max_id()
        min_id_g=g.max_id()
        min_id_self=self.min_id()
        max_id_self=self.max_id()
        self.shift_indices(max(max_id_g,max_id_self)-min(min_id_g,min_id_self)+1)
        self.set_output_ids(self.get_output_ids()+g.get_output_ids())
        self.set_input_ids(self.get_input_ids()+g.get_input_ids())
        self.nodes.update(g.nodes)
    
    def parralel(self,g):
        new=open_digraph.origin()
        new.iparralel(self)
        new.iparralel(g)
        return new

    def icompose(self,g):
        if(len(self.get_input_ids()) != len(g.get_output_ids())):
            raise Exception("nombre d'entrées différent")
        max_id_g=g.max_id()
        min_id_g=g.min_id()
        min_id_self=self.min_id()
        max_id_self=self.max_id()
        self.shift_indices(max(max_id_g,max_id_self)-min(min_id_g,min_id_self)+1)
        list_self_inputs=self.get_input_ids()
        list_g_outputs=g.get_output_ids()
        self.nodes.update(g.nodes)
        
        for i in range(len(list_self_inputs)):
            self.add_edge(list_self_inputs[i],list_g_outputs[i])
        self.set_input_ids(g.get_input_ids())


    def compose(self,g):
        new=self.copy()
        newg=g.copy()
        new.icompose(newg)

        return new
    def parcours_dict(self,dict,node,k,nodes_notseen):
        if node in nodes_notseen: 
            dict[node.get_id()]=k
            nodes_notseen.difference([node])
            children_ids=node.get_children_ids()
            parents_ids=node.get_parent_ids()
            for i in range(len(children_ids)):
                self.parcours_dict(dict,self.get_node_by_id(i),k,nodes_notseen)
            for j in range(len(parents_ids)):
                self.parcours_dict(dict,self.get_node_by_id(j),k,nodes_notseen)

    def connected_components(self):
        dict={}
        nodes_notseen=self.get_nodes()
        k=0
        while(nodes_notseen!=[]):
            current_node=nodes_notseen[0]
            self.parcours_dict(dict,current_node,k,nodes_notseen)
            seen=[self.get_node_by_id(key) for key,v in dict.items() if v==k]
            k=k+1
            
        return (k,dict)

    def connnexe_compose(self):
        k,v=self.connected_components()
        list_g=[]
        for i in range(k):
            newg=open_digraph.origin()
            seen={key:self.get_node_by_id(key) for key,value in v.items() if value==i}
            newg.nodes.update(seen)
            inputs_g=[value.id for key,value in seen.items() if  (((len(value.get_children_ids())==1) and (len(value.get_parent_ids())==0)) and (value.children[value.get_children_ids()[0]]==1))]
            ouputs_g=[value.id for key,value in seen.items() if  (((len(value.get_parent_ids())==1) and (len(value.get_children_ids())==0)) and ((node.parents[node.get_parent_ids()[0]]==1)))]
            newg.set_output_ids(outputs_g)
            newg.set_input_ids(inputs_g)
            list_g.append(newg)
        return list_g

    def iparralel_list(self,*args):
        for i in args:
            self.iparralel(i)

    def parralel_list(self,*args):
        new=open_digraph.origin()
        new.iparralel(self)
        for argk in args:
            new.iparralel(argk)
        return new