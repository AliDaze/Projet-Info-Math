import random
import sys
import os
import webbrowser

from open_digraph import *
from open_diagraph_parralelcompose_mx import *
from node import *
    
def random_rand_list(n,bound):
    return [int(random.randrange(0,bound)) for i in range(n)]

def random_int_matrix(n,bound,null_diag=True):
    M=[random_rand_list(n,bound) for i in range(n)]
    if null_diag:
        for i in range(n):
            M[i][i]=0
    return M


def random_symetric_int_matrix(n,bound,null_diag=True):
    
    if null_diag :
        M=random_int_matrix(n,bound)
    else:
        M=M=random_int_matrix(n,bound, false)
    for i in range(n-1):
        for j in range(i+1,n):
            M[i][j]=M[j][i]
    return M
        
            
def random_oriented_int_matrix(n, bound,null_diag=True):
    
    M=random_int_matrix(n,bound, null_diag)
    for i in range(n-1):
        for j in range(i+1,n):
            if (int(random.randrange(0,bound)) %2==0):
                M[i][j]=0
            else :
                M[j][i]=0
    return M

def random_triangular_int_matrix(n, bound, null_diag=True) :
    M=[]
    for i in range(n):
        M.append([])
        for j in range(n) :
            if (i>j) or (i==j and null_diag) :
                M[i].append(0)
            else :
                M[i].append(int(random.randrange(0,bound)))
    return M

def graph_from_adjacency_matrix(M,n):
    graph=open_digraph([],[],[node(i,"v"+str(i),{},{}) for i in range(n)])
    l=graph.get_node_ids()
    for i in range(n):
        for j in range(n):
            for k in range(M[i][j]):
                graph.add_edge(l[j], l[i])
    return graph 

'''
@classmethod
    def random(n, bound, inputs=0, outputs=0, form="free"):
    
    if form=="free":
        return graph_from_adjacency_matrix(n)
    elif form=="DAG":
    ...
    elif form=="oriented":
    ...
    elif form=="loop-free":
    ...
    elif form=="undirected":
    ...
    elif form=="loop-free undirected":
'''