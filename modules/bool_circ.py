import random
import sys
import os
import webbrowser

from open_diagraph_matrix import *
from open_digraph import *
from node import *

class bool_circ(open_digraph):
    
    def __init__(self,g):

        self.inputs = g.inputs
        self.outputs = g.outputs
        self.nodes = g.nodes
        if not(self.is_well_formed()):
            raise Exception("n'est pas un circuit boolean")

    def is_well_formed(self):
        for node in nodes:
            if node.label=="" and not(node.indegree()==1) : 
                return False 
            if (node.label=="&" or node.label=="|" or node.label=="^") and not(node.outdegree()==1):
                return False
            if (node.label=="~") and not(node.indegree()==1) and not(node.outdegree()==1):
                return False
            return not(self.is_cyclic())