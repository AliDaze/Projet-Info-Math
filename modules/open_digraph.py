import random
import sys
import os
import webbrowser

from modules.open_diagraph_matrix import *
from modules.open_diagraph_parralelcompose_mx import *
from modules.node import *


class open_digraph(open_diagraph_parralelcompose_mx): # for open directed graph
    def __init__(self, inputs, outputs, nodes):
        '''
        inputs: int list; the ids of the input nodes
        outputs: int list; the ids of the output nodes
        nodes: node iter;
        '''
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict

    def __str__(self):
        '''
        fonction d'affichage 
        '''
        return f'id : {self.inputs} ,outputs : {self.outputs} nodes : {self.nodes}'

    def __repr__(self):
        '''
        fonction d'affichage inductif
        '''
        if isinstance(self, list):
            for i in self:
                __repr__(i)
        else:
            __str__(self)



    @classmethod
    def origin(cls): 
        return cls([],[],{})

    
    def copy(self) :
        nodez=map(lambda x : x.copy() ,self.nodes.values())

        return open_digraph(self.inputs.copy(), self.outputs.copy(), nodez)

    def get_input_ids(self):
        return self.inputs

    def get_output_ids(self):
        return self.outputs

    def get_id_node_map(self):
        return self.nodes

    def get_nodes(self):
        return list(self.nodes.values())
    
    def get_node_ids(self):
        return list(self.nodes.keys())
    
    def get_node_by_id(self, id):
        if id in self.get_node_ids() :
            return self.nodes[id]
        raise Exception("Sorry, no id in the graph")
    
    def get_nodes_by_ids(self, ids):
        return [self.get_node_by_id(id) for id in ids]
    
    def set_input_ids(self, inputs):
        self.inputs=inputs
        
    def set_output_ids(self, outputs):
        self.outputs=outputs
        
    def add_input_id(self, id):
        self.inputs.append(id)
        
    def add_output_id(self, id):
        self.outputs.append(id)
        
    def new_id (self):
        '''
        crée un nouvel id
        '''
        l=self.get_node_ids()+ self.get_input_ids() +self.get_output_ids()
        m=l[0]
        while (m in l):
            m=m+1
        return m
    def clean(self):
        '''
        fonction qui supprime les inputs et outputs sans enfant/parent
        '''
        for node in self.get_nodes():
            if(node.get_children_ids()==[] and node.get_parent_ids()==[] and ((node.get_id() in self.get_input_ids()) or (node.get_id() in self.get_output_ids()) )):
                self.nodes.pop(node.get_id())
                if node.get_id() in self.get_input_ids():
                    self.inputs.remove(node.get_id())
                if node.get_id() in self.get_output_ids():
                    self.outputs.remove(node.get_id())
    def add_edge(self, src, tgt):
        '''
        ajoute une arrete qui va de tgt a src
        '''
        src_node=self.get_node_by_id(src)
        tgt_node=self.get_node_by_id(tgt)
        if tgt in src_node.parents.keys():
            src_node.parents[tgt]=src_node.parents[tgt]+1
        else :
            src_node.parents[tgt]=1
            
        if src in tgt_node.children.keys():
            tgt_node.children[src]=tgt_node.children[src]+1
        else :
            tgt_node.children[src]=1
        
    def add_node(self, label=" ", parents={},children={}):
        '''
        crée un node avec label et parents/enfants données
        '''
        new_node=node(self.new_id(), label, {}, {})
        self.nodes[new_node.get_id()]=new_node
        for i in parents.keys() :
            for j in range(parents[i]):
                self.add_edge(new_node.get_id(), i)
            
        for i in children.keys() :
            for j in range(children[i]):
                self.add_edge(i, new_node.get_id())

    def remove_edge(self,src,tgt):
        '''
        enleve une arrete qui part de src a tgt
        '''
        tgt_node = self.get_node_by_id(tgt)
        src_node = self.get_node_by_id(src)
        tgt_node.remove_parent_once(src)
        src_node.remove_child_once(tgt)
        if tgt in self.get_input_ids():
            self.inputs.remove(tgt)
        if src in self.output_ids():
            self.outputs.remove(src)

    def remove_parallel_edges(self,src,tgt):
        '''
        retire toutes les arretes de src a tgt
        '''
        tgt_node = self.get_node_by_id(tgt)
        src_node = self.get_node_by_id(src)
        tgt_node.remove_parent_id(src)
        src_node.remove_child_id(tgt)
        if tgt in self.get_input_ids():
            self.inputs.remove(tgt)
        if src in self.get_output_ids():
            self.outputs.remove(src)
    def remove_node_by_id(self,*args):
        '''
        remove des nodes du graph
        '''
        for arg in args:
            if arg in self.get_input_ids():
                self.inputs.remove(arg)
            if arg in self.get_output_ids():
                self.outputs.remove(arg)
            if arg in self.nodes.keys():
                nodearg=self.get_node_by_id(arg)
                for k in nodearg.get_parent_ids():
                    self.remove_parallel_edges(k,arg)
                for j in nodearg.get_children_ids():
                    self.remove_parallel_edges(arg,j)
                self.nodes.pop(arg)
        self.clean()


    def input_output_in_graph(self):
        '''
        verifie que les inputs et les outputs sont dans le graph
        '''
        ids_node=self.get_node_ids()

        for i in self.inputs:
            if not(i in ids_node) :
                return False
        for j in self.outputs:
            if not(j in ids_node):
                return False
        return True

    def inputs_child_one(self):
        '''
        verifie qu'il a un enfant a une multipilicité
        '''
        ids=self.get_input_ids()
        nodes = self.get_nodes_by_ids(ids)
        for node in nodes : 
            if not(len(node.get_children_ids())==1) or not(len(node.get_parent_ids())==0):
                return False
            if not(node.children[node.get_children_ids()[0]]==1):
                return False
        return True

    def outputs_parent_one(self):
        '''
        verifie qu'il a un parent a une multipilicité
        '''
        ids=self.get_output_ids()
        nodes = self.get_nodes_by_ids(ids)
        for node in nodes :
            if not(len(node.get_parent_ids())==1) or not(len(node.get_children_ids())==0):
                return False
            if not(node.parents[node.get_parent_ids()[0]]==1):
                return False
        return True

    def cle_nodes_exist(self):
        '''
        chaque node a son id comme clé dans nodes
        '''
        for i in self.get_node_ids():
            if self.nodes[i].get_id()!=i :
                return False
        return True

    def same_multiple_nodes(self):
        '''
        verifie que les multiplicités des arretes sont respectés d'un noeud a l'autre 
        '''
        nodes=self.get_nodes()
        for node in nodes :
            node_id= node.get_id()
            ids_parents_node = node.get_parent_ids()
            ids_children_node = node.get_children_ids()
            for i in ids_parents_node : 
                if not((i in self.nodes)): 
                    return False
                if not((node_id in self.get_node_by_id(i).get_children_ids())) :
                    return False
                if  not(node.parents[i]==self.get_node_by_id(i).children[node_id]):
                    return False
            for j in ids_children_node : 
                if not((j in self.nodes)):
                    return False
                
                if not((node_id in self.get_node_by_id(j).get_parent_ids())) :
                    return False
                if not(node.children[j]==self.get_node_by_id(j).parents[node_id]):
                    return False

        return True


    def is_well_formed(self):
        '''
        verifie que le graph est bien formé
        '''
        return self.input_output_in_graph() and self.inputs_child_one() and self.outputs_parent_one() and self.cle_nodes_exist() and self.same_multiple_nodes()

    def add_node_input(self,idc):
        '''
        ajoute un input avec une arrete vers le noeud d'id idc
        '''
        if idc in self.get_input_ids():
            self.inputs.remove(idc)
        if not(idc in self.get_node_ids()):
            raise Exception("Sorry, no id in the graph")
        children_node={idc:1}
        id_node=self.new_id()
        self.add_node("",{},children_node)
        self.set_input_ids(self.get_input_ids()+[id_node])

    def add_node_output(self,idp):
        '''
        ajoute un output avec une arrete vers le noeud d'id idp
        '''
        if idp in self.get_output_ids():
            self.outputs.remove(idp)
        if not(idp in self.get_node_ids()):
            raise Exception("Sorry , no id in the graph")
        parents_node={idp:1}
        id_node=self.new_id()
        self.add_node("",parents_node,{})
        self.set_output_ids(self.get_output_ids()+[id_node])

    def save_as_dot_file(self, path, verbose=False):
        exit_basename=path.__contains__(".dot")
        #print(exit_basename)
        if(exit_basename):
            #isExist = os.path.exists(path)
            name = os.path.basename(path)
            path=path.replace(name,"")
        else:
            name = "graph.dot"

        #print(path)
        isExist = os.path.exists(path)
        #print(isExist)
        if(isExist):
            pathf=path+"/"+name
            if(os.path.exists(pathf)):
                os.remove(pathf)
            fichier = open(pathf, "a")


        else:
            if(os.path.exists(name)):
                os.remove(name)
            fichier = open(name, "a")
        graph_name="graph_"+str(random.randint(0,10000))
        fichier.write("digraph "+graph_name+" {\n")
        if verbose:
            for node in self.nodes:
                fichier.write(str(node)+" [label=\" label: "+self.nodes[node].get_label()+ " \\nid: " + str(node)+ "\"];\n")
        for node in self.get_nodes():
            children=node.children
            for child in children:
                for multiplicite in range(children[child]):
                    fichier.write(str(node.get_id()) + " -> " + str(child) + ";\n")


        fichier.write("}\n")


        fichier.close()

    @classmethod
    def from_dot_file(self, path) :
        fichier = open(path, "r+") 
        list_ids=[]
        for ligne in fichier :
            ligne.strip()
            
            if((ligne=="") or ("{" in ligne) or ("}" in ligne) or ("digraph" in ligne) or ("[label=" in ligne ) or not("->" in ligne)):
                continue
            
            ligne=ligne.replace("\n","")
            ligne=ligne.replace(" ","")
            ligne=ligne.replace(";","")
            ligne=ligne.replace("->"," ")
            ligne_list=ligne.split()
            for i in ligne_list:
                list_ids.append(int(i))
            
            #print(ligne)
        list_ids_remove_duplicates=list(set(list_ids))
        G_new=open_digraph([],[],[node(id, "v"+str(id),{},{}) for id in list_ids_remove_duplicates])
        for i in range(0,len(list_ids)-1,2):
            G_new.add_edge(list_ids[i+1], list_ids[i])
        
     
        fichier.close()
        
        return G_new
            
    def display (self, verbose=False):
        num=str(random.randint(0,10000))
        nom=os.getcwd()+"/graph"+num
        self.save_as_dot_file( nom+".dot", verbose)
        os.system('dot -Tpdf graph'+num+'.dot -o graph'+num+'.pdf')
        webbrowser.open_new(nom+".pdf")

    def is_cyclic(self):
        gcopy = self.copy()
        cyclic= True
        while(cyclic):
            retire=False
            if gcopy.nodes == {} : 
                cyclic=False
                break
            for i in gcopy.nodes.values():
                if i.children=={}:
                    gcopy.remove_node_by_id(i.get_id())
                    retire=True
            if not(retire) : 
                break
        return cyclic 

    def min_id(self):
        return min(self.get_node_ids())

    def max_id(self):
        return max(self.get_node_ids())

    def shift_indices(self,n):
        for node in self.get_nodes():
            old_id=node.get_id()
            child={idc+n:node.children[idc] for idc in node.get_children_ids()}
            parent={idc+n:node.parents[idc] for idc in node.get_parent_ids()}
            node.set_parent_ids(parent)
            node.set_children_ids(child)
            node.set_id(node.get_id()+n)
            self.nodes[node.get_id()]=node
            del self.nodes[old_id]
        inputs=[i+n for i in self.get_input_ids()]
        output=[i+n for i in self.get_output_ids()]
        self.set_output_ids(output)
        self.set_input_ids(inputs)
    
    @classmethod
    def id_dict(self):
        dict_id={}
        nodes_ids=self.get_node_ids()
        for i in range(len(nodes_ids)):
            dict_id[node_id[i]]=i
        return dict_id
    @classmethod
    def adjacency_matrix(self):
        dict_id=self.id_dict()
        l=len(dict_id.keys())
        M=np.zeros((l,l))
        for i in self.get_nodes():
            id_i=i.get_id()
            for j in i.get_children_ids():
                M[i][j]=i.children[j]
            for k in i.get_parent_ids():
                M[i][k]=i.children[k]
        return M

    def djikstra(src,direction=None):
        q=[src]
        dist = {src : 0}
        prev = {}
        while (q!=[]):
            u=(min(q,key=lambda x : dist[x])).get_id()
            q.pop(u)
            if direction == None : 
                neighbors = [self.get_node_by_id(i) for i in u.get_children_ids()]+ [self.get_node_by_id(i) for i in u.get_parent_ids()]
            if direction == 1:
                neneighbors = [self.get_node_by_id(i) for i in u.get_children_ids()]
            if direction ==-1 : 
                neighbors = neighbors = [self.get_node_by_id(i) for i in u.get_parent_ids()]
            for v in neighbors:
                if not(v in dist.keys()):
                    q.append(v)
                if not(v in q) or (dist[v]> dist[u]+1):
                    dist[v]=dist[u]+1
                    prev[v]=u

        return dist, prev

 


def graph_from_adjacency_matrix(M,n):
    graph=open_digraph([],[],[node(i,"v"+str(i),{},{}) for i in range(n)])
    l=graph.get_node_ids()
    for i in range(n):
        for j in range(n):
            for k in range(M[i][j]):
                graph.add_edge(l[j], l[i])
    return graph  

    

