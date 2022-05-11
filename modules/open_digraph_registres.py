import random
import sys
import os

import copy
import time
from math import *
import numpy as np

class open_digraph_registres:

    @classmethod
    def adder(cls,registre1,registre2,c="0"):
        registre1=registre1[::-1]
        registre2=registre2[::-1]
        G=cls.origin()
        node_c=G.add_node(c)
        for i in range(len(registre1)):
            node_c=G.adder_bis(registre1[i],registre2[i],node_c,i)
        G.add_node("c'",{node_c:1},{})
        return G

    def adder_bis(self,a,b,c,i):
        node_copie_c=self.add_node("",{c:1},{})
        node_a=self.add_node(a)
        copie_a=self.add_node("",{node_a:1},{})
        node_b=self.add_node(b)
        copie_b=self.add_node("",{node_b:1},{})
        node_and=self.add_node("&",{copie_b:1,copie_a:1},{})
        node_xor1=self.add_node("^",{copie_b:1,copie_a:1},{})
        node_copie_xor1=self.add_node("",{node_xor1:1},{})
        node_and2=self.add_node("&",{node_copie_xor1:1,node_copie_c:1},{})
        node_or=self.add_node("|",{node_and:1,node_and2:1},{})
        node_xor2=self.add_node("^",{node_copie_xor1:1,node_copie_c:1})
        node_r=self.add_node(f"r{i}",{node_xor2:1},{})

        return node_or
    

            
    @classmethod
    def half_adder(cls,registre1,registre2):
        G = cls.adder(registre1,registre2,"0")
        #G.get_node_by_id(G.get_input_ids()[-1]).set_label("0")
        return G
    @classmethod
    def entier_adder(cls,n,taille=8):
        graph=cls.origin()
        bin_n=bin(n)[2:]
        if(taille<(len(bin_n))):
            raise Exception("mauvaise taille de registre")
        bin_n=((taille-len(bin_n))*"0")+bin_n
        for i in range(len(bin_n)):
            id=graph.new_id()
            graph.add_node(bin_n[i])
            graph.add_input_id(id)
            id2=graph.new_id()
            graph.add_node(f"output{i}",{id:1},{})
            graph.add_output_id(id2)

        print(graph.is_well_formed_circ())
        return graph

    def table1_copies(self,node):
        if(node.get_label() == "0" or node.get_label() == "1"):

                if(self.get_node_by_id(node.get_children_ids()[0]).get_label() == ""):

                    nodes_copies = self.get_node_by_id(node.get_children_ids()[0]).get_children_ids()
                    for node_copie in nodes_copies:

                        id_node=self.new_id()
                        self.add_node(node.get_label(),{},{node_copie:1})
                        self.add_input_id(id_node)

                    self.remove_node_by_id(node.get_children_ids()[0])
                    self.remove_node_by_id(node.get_id())

    def table1_non(self,node):
        if(node.get_label() == "0" or node.get_label() == "1"):
            if(self.get_node_by_id(node.get_children_ids()[0]).get_label() == "~"):
                        if(node.get_label() == "0"):
                            self.add_node("1",{},{self.get_node_by_id(node.get_children_ids()[0]).get_children_ids()[0]:1})
                            self.remove_node_by_id(node.get_children_ids()[0])
                            self.remove_node_by_id(node.get_id())
                        else:
                            self.add_node("0",{},{self.get_node_by_id(node.get_children_ids()[0]).get_children_ids()[0]:1})
                            self.remove_node_by_id(node.get_children_ids()[0])
                            self.remove_node_by_id(node.get_id())

    def table1_et(self,node):
        if(node.get_label() == "0" or node.get_label() == "1"):
            if(self.get_node_by_id(node.get_children_ids()[0]).get_label() == "&"):
                        if(node.get_label() == "0"):
                            nodes_copies= self.get_node_by_id(node.get_children_ids()[0]).get_parent_ids()
                            for node_copie in nodes_copies:
                                if node_copie!=node.get_id():
                                    self.add_node("",{node_copie:1},{})
                            self.add_node("0",{},{self.get_node_by_id(node.get_children_ids()[0]).get_children_ids()[0]:1})
                                
                            self.remove_node_by_id(node.get_children_ids()[0])
                            self.remove_node_by_id(node.get_id())
                        else:
                            self.remove_node_by_id(node.get_id())
    def table1_ou(self,node):
        if(node.get_label() == "0" or node.get_label() == "1"):
            if(self.get_node_by_id(node.get_children_ids()[0]).get_label() == "|"):
                        if(node.get_label() == "1"):
                            nodes_copies= self.get_node_by_id(node.get_children_ids()[0]).get_parent_ids()
                            for node_copie in nodes_copies:
                                if node_copie!=node.get_id():
                                    self.add_node("",{node_copie:1},{})
                            self.add_node("1",{},{self.get_node_by_id(node.get_children_ids()[0]).get_children_ids()[0]:1})
                                
                            self.remove_node_by_id(node.get_children_ids()[0])
                            self.remove_node_by_id(node.get_id())
                        else:
                            self.remove_node_by_id(node.get_id())

    def table1_xor(self,node):
        if(node.get_label() == "0" or node.get_label() == "1"):
            if(self.get_node_by_id(node.get_children_ids()[0]).get_label() == "^"):
                        if(node.get_label() == "0"):
                            self.remove_node_by_id(node.get_id())
                        else:
                            id_node=self.new_id()
                            self.add_node("~",{},{self.get_node_by_id(node.get_children_ids()[0]).get_children_ids()[0]:1})
                            self.add_node("^",self.get_node_by_id(node.get_children_ids()[0]).parents,{id_node:1})
                            self.remove_node_by_id(node.get_children_ids()[0])
                            self.remove_node_by_id(node.get_id())

    def table1_et_to_1(self,node):
        if(node.get_label() == "&" and (node.indegree()== 0)):
            self.add_node("1",{},node.children)
            self.remove_node_by_id(node.get_id())

    def table1_ou_xor_to_0(self,node):
        if ((node.get_label() == "^" or node.get_label() == "|") and (len(node.get_parent_ids()) == 0)):
                self.add_node("0",{},node.children)
                self.remove_node_by_id(node.get_id())
    def table1_regles(self):
        '''
        retire les copies et les remplace par des repetitions de la primitive
        '''
        nodes=self.get_nodes()
        for node in nodes:
            print(node.get_children_ids())
            if(node.get_children_ids()!=[]):
                if(node.get_label() == "0" or node.get_label() == "1"):

                    if(self.get_node_by_id(node.get_children_ids()[0]).get_label() == ""):

                        self.table1_copies(node)
                        return True
                    
                    if(self.get_node_by_id(node.get_children_ids()[0]).get_label() == "~"):

                        self.table1_non(node)
                        return True
                    
                    if(self.get_node_by_id(node.get_children_ids()[0]).get_label() == "&"):
                        
                        self.table1_et(node)
                        return True
                    
                    if(self.get_node_by_id(node.get_children_ids()[0]).get_label() == "|"):
                        
                        self.table1_ou(node)
                        return True
                    
                    if(self.get_node_by_id(node.get_children_ids()[0]).get_label() == "^"):
                        
                        self.table1_xor(node)
                        return True
            
            if ((node.get_label() == "^" or node.get_label() == "|") and (len(node.get_parent_ids()) == 0)):
                self.table1_ou_xor_to_0(node)
                return True

            if(node.get_label() == "&" and (len(node.get_parent_ids()) == 0)):
                self.table1_et_to_1(node)
                return True

        return False

            

    def evaluate(self):
        changement=True
        while(changement):
            changement=self.table1_regles()
           