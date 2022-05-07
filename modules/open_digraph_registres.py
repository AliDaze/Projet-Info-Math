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


