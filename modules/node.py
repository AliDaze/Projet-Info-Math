import random
import sys
import os
import webbrowser

from open_diagraph_matrix import *
from open_diagraph_parralelcompose_mx import *
from open_digraph import *
class node:

    def __init__(self, identity, label, parents, children):
        '''
        identity: int; its unique id in the graph
        label: string;
        parents: int->int dict; maps a parent node's id to its multiplicity
        children: int->int dict; maps a child node's id to its multiplicity
        '''
        self.id = identity
        self.label = label
        self.parents = parents
        self.children = children

    def __str__(self):
        '''
        fonction d'affichage 
        '''
        return f'id : {self.id} , label : {self.label} , parents : {self.parents} , children : {self.children}'
    def __repr__(self):
        '''
        fonction affichage inductive
        '''
        return f'id : {self.id} , label : {self.label} , parents : {self.parents} , children : {self.children}'

    
    def copy(self) :
        '''
        return une copie du noeud
        '''
        return node(self.id, self.label, self.parents.copy(), self.children.copy())
    
    def get_id(self):

        '''
        return l'id du noeud
        '''
        return self.id
    
    def get_label(self):

        '''
        return le label du noeud
        '''
        return self.label
    
    def get_children_ids(self):
        '''
        return les clés du dictionnaire des children autrement dit les ids des children
        '''
        return list(self.children.keys())
    def get_children_ids(self):
        return self.children
    
    def get_parent_ids(self):

        '''
        return les clés du dictionnaire des parents autrements dit les ids des parents
        '''
        return list(self.parents.keys())

    def set_id(self, id):
        '''
        prend en argument un id 
        et
        set/modifie l'id du noeud
        '''
        self.id=id

    def set_label(self, label):
        '''
        prend en argument un label 
        et
        set/modifie l'id du noeuf
        '''
        self.label=label

    def set_parent_ids(self, parents):
        '''
        prend en argument des ids de parents
        et
        set/modifie les parents
        '''
        self.parents=parents

    def set_children_ids(self, children):
        '''
        prend en argument des ids de children
        et
        set/modifie les children
        '''
        self.children=children

    def remove_parent_once(self,idp):
        '''
        prend un id de noeud et retire une arrete parent/enfant avec le noeud équivalent
        '''
        if idp in self.parents:
            self.parents[idp]=self.parents[idp]-1
            if self.parents[idp] <= 0 :
                self.parents.pop(idp) 

    def remove_child_once(self,idc):
        '''
        prend un id : idc
        retire une arrete enfant/parent avec le noeud équivalent
        '''
        if idc in self.children:
            self.children[idc]=self.children[idc]-1
            if self.children[idc] <= 0 : 
                self.children.pop(idc)

    def remove_parent_id(self,idp):
        '''
        prend un id : idp
        retire toutes les arretes du parent d'id idp
        '''
        if idp in self.parents.keys():
            self.parents.pop(idp)

    def remove_child_id(self,idc):
        '''
        prend un id : idc
        retire toutes les arretes du child d'id idc
        '''
        if idc in self.children.keys():
            self.children.pop(idc)

    def indegree(self):
        return sum(self.parents.values())
    
    def outdegree(self):
        return sum(self.children.values())
    
    def degree(self):
        return self.indegree()+self.outdegree()
        