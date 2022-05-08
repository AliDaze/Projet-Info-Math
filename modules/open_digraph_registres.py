import random
import sys
import os

import copy
import time
from math import *
import numpy as np

class open_digraph_registres:

    @classmethod
    def adder(cls,n):
        '''
        rend le graph de l additionneur de deux registre de taille n bits  avec les label "a"+i et "b"+i avec i le poid du bit
        pour evaluer le graph il suffit de renommer par les valeur qu'on veut evaluer
        '''

        #creer le graph du cas de base (n==0)
        G = cls.origin()
        node1 = G.add_node("")
        node2 = G.add_node("")
        node3 = G.add_node("")
        G.add_node_input(node1, label="a0")
        G.add_node_input(node2, label="b0")
        G.add_node_input(node3, label="c")
        xor1 = G.add_node("^")
        xor2 = G.add_node("^")
        divise = G.add_node("")
        and1 = G.add_node("&")
        and2 = G.add_node("&")
        or1 = G.add_node("|")
        G.add_node_output(xor2, label="r0")
        G.add_node_output(or1, label="c'")

        G.add_edge(xor1,node1 )
        G.add_edge(and1,node1)
        G.add_edge(xor1,node2)
        G.add_edge(and1,node2)
        G.add_edge(xor2,node3)
        G.add_edge(and2,node3)
        G.add_edge(divise,xor1)
        G.add_edge(and2,divise)
        G.add_edge(xor2,divise)
        G.add_edge(or1,and1)
        G.add_edge(or1,and2)

        for i in range(0, n):
            #relier et assembler les grapgs
            add = G.copy()
            indice_bit_a = len(add.get_input_ids()) // 2
            indice_bit_b = indice_bit_a
            for node in add.get_input_ids():
                n = G.get_node_by_id(node)
                if n.get_label()[0] == "a":
                    n.set_label(f"a{indice_bit_a}")
                    indice_bit_a += 1
                if n.get_label()[0] == "b":
                    n.set_label(f"b{indice_bit_b}")
                    indice_bit_b += 1
            retenue_sortant = G.get_output_ids()[-1]
            retenue_entrant = add.get_input_ids()[-1]
            retenue_entrant += G.max_id() + 1
            G.iparralel(add)
            node_retenue_entrant=G.get_node_by_id(retenue_entrant)
            node_retenue_sortant=G.get_node_by_id(retenue_sortant)
            G.add_edge(node_retenue_entrant.get_children_ids()[0], node_retenue_sortant.get_parent_ids()[0])
            G.remove_node_by_id(retenue_entrant)
            G.remove_node_by_id(retenue_sortant)
        inputs = G.get_input_ids()[:-1]
        new_inputs=inputs[0::2] + inputs[1::2] + [G.get_input_ids()[-1]]
        G.set_input_ids(new_inputs)
        for i, o in enumerate(G.get_output_ids()[0:-1]):
            #renommer les output avec "r"+i avec i le poid du bit
            n = G.get_node_by_id(o)
            n.set_label(f"r{i+1}")
        return G

            
    @classmethod
    def half_adder(cls,n):
        G = cls.adder(n)
        G.get_node_by_id(G.get_input_ids()[-1]).set_label("0")
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

    def table1_regles(self):
        '''
        retire les copies et les remplace par des repetitions de la primitive
        '''
        nodes=self.get_nodes()
        for node in nodes:
            if(node.get_label() == "0" or node.get_label() == "1"):

                if(node.get_children_ids()[0].get_label() == ""):

                    nodes_copies = node.get_children_ids()[0].get_children_ids()
                    for node_copie in nodes_copies:

                        id_node=self.new_id()
                        self.add_node(node.get_label(),{},{node_copie:1})
                        self.add_input_id(id_node)

                    self.remove_node_by_id(node.get_children_ids()[0])
                    self.remove_node_by_id(node.get_id())

                if(node.get_children_ids()[0].get_label() == "~"):
                    if(node.get_label() == "0"):
                        self.add_node("1",{},{node.get_children_ids()[0].get_children_ids()[0]:1})
                        self.remove_node_by_id(node.get_children_ids()[0])
                        self.remove_node_by_id(node.get_id())
                    else:
                        self.add_node("0",{},{node.get_children_ids()[0].get_children_ids()[0]:1})
                        self.remove_node_by_id(node.get_children_ids()[0])
                        self.remove_node_by_id(node.get_id())

                if(node.get_children_ids()[0].get_label() == "&"):
                    if(node.get_label() == "0"):
                        nodes_copies= node.get_children_ids()[0].get_parent_ids()
                        for node_copie in nodes_copies:
                            self.add_node("",{node_copie:1},{})
                        self.add_node("0",{},{node.get_children_ids()[0].get_children()[0]})
                            
                        self.remove_node_by_id(node.get_children_ids()[0])
                        self.remove_node_by_id(node.get_id())
                    else:
                        self.remove_node_by_id(node.get_id())
                
                if(node.get_children_ids()[0].get_label() == "|"):
                    if(node.get_label() == "1"):
                        nodes_copies= node.get_children_ids()[0].get_parent_ids()
                        for node_copie in nodes_copies:
                            self.add_node("",{node_copie:1},{})
                        self.add_node("1",{},{node.get_children_ids()[0].get_children()[0]})
                            
                        self.remove_node_by_id(node.get_children_ids()[0])
                        self.remove_node_by_id(node.get_id())
                    else:
                        self.remove_node_by_id(node.get_id())
                
                if(node.get_children_ids()[0].get_label() == "^"):
                    if(node.get_label() == "0"):
                        self.remove_node_by_id(node.get_id())
                    else:
                        id_node=self.new_id()
                        self.add_node("~",{},{node.get_children()[0].get_children()[0]:1})
                        self.add_node("^",node.get_children()[0].parents,{id_node:1})
                        self.remove_node_by_id(node.get_children_ids()[0])
                        self.remove_node_by_id(node.get_id())
            
            if ((node.get_label() == "^" or node.get_label() == "|") and (len(node.get_parent_ids()) == 0)):
                self.add_node("0",{},node.children)
                self.remove_node_by_id(node.get_id())

            if(node.get_label() == "&" and (len(node.get_parent_ids()) == 0)):
                self.add_node("1",{},node.children)
                self.remove_node_by_id(node.get_id())

            

