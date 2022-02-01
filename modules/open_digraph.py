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
        return node(self.id, self.label, self.parents, self.children)
    
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

        
    



class open_digraph: # for open directed graph
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
        return node(self.inputs, self.outputs, self.nodes)

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
        l=self.get_node_ids()+ self.get_input_ids() +self.get_output_ids()
        m=l[0]
        while (m in l):
            m=m+1
        return m
    def clean(self):
        for node in self.get_nodes():
            if(node.get_children_ids()==[] and node.get_parent_ids()==[] and ((node.get_id() in self.get_input_ids()) or (node.get_id() in self.get_output_ids()) )):
                self.nodes.pop(node.get_id())
                if node.get_id() in self.get_input_ids():
                    self.inputs.remove(node.get_id())
                if node.get_id() in self.get_output_ids():
                    self.outputs.remove(node.get_id())
    def add_edge(self, src, tgt):
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
        new_node=node(self.new_id(), label, {}, {})
        self.nodes[new_node.get_id()]=new_node
        for i in parents.keys() :
            for j in range(parents[i]):
                self.add_edge(new_node.get_id(), i)
            
        for i in children.keys() :
            for j in range(children[i]):
                self.add_edge(i, new_node.get_id())

    def remove_edge(self,src,tgt):
        tgt_node = self.get_node_by_id(tgt)
        src_node = self.get_node_by_id(src)
        tgt_node.remove_parent_once(src)
        src_node.remove_child_once(tgt)
        if tgt in self.get_input_ids():
            self.inputs.remove(tgt)
        if src in self.output_ids():
            self.outputs.remove(src)

    def remove_parallel_edges(self,src,tgt):
        tgt_node = self.get_node_by_id(tgt)
        src_node = self.get_node_by_id(src)
        tgt_node.remove_parent_id(src)
        src_node.remove_child_id(tgt)
        if tgt in self.get_input_ids():
            self.inputs.remove(tgt)
        if src in self.get_output_ids():
            self.outputs.remove(src)
    def remove_node_by_id(self,*args):
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
        ids_node=self.get_node_ids()

        for i in self.inputs:
            if not(i in ids_node) :
                return False
        for j in self.outputs:
            if not(j in ids_node):
                return False
        return True

    def inputs_child_one(self):
        ids=self.get_input_ids()
        nodes = self.get_nodes_by_ids(ids)
        for node in nodes : 
            if not(len(node.get_children_ids())==1) or not(len(node.get_parent_ids())==0):
                return False
            if not(node.children[node.get_children_ids()[0]]==1):
                return False
        return True

    def outputs_parent_one(self):
        ids=self.get_output_ids()
        nodes = self.get_nodes_by_ids(ids)
        for node in nodes :
            if not(len(node.get_parent_ids())==1) or not(len(node.get_children_ids())==0):
                return False
            if not(node.parents[node.get_parent_ids()[0]]==1):
                return False
        return True

    def cle_nodes_exist(self):
        for i in self.get_node_ids():
            if self.nodes[i].get_id()!=i :
                return False
        return True

    def same_multiple_nodes(self):
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
        return self.input_output_in_graph() and self.inputs_child_one() and self.outputs_parent_one() and self.cle_nodes_exist() and self.same_multiple_nodes()

    def add_node_input(self,idc):
        if idc in self.get_input_ids():
            self.inputs.remove(idc)
        if not(idc in self.get_node_ids()):
            raise Exception("Sorry, no id in the graph")
        children_node={idc:1}
        id_node=self.new_id()
        self.add_node("",{},children_node)
        self.set_input_ids(self.get_input_ids()+[id_node])

    def add_node_output(self,idp):
        if idp in self.get_output_ids():
            self.outputs.remove(idp)
        if not(idp in self.get_node_ids()):
            raise Exception("Sorry , no id in the graph")
        parents_node={idp:1}
        id_node=self.new_id()
        self.add_node("",parents_node,{})
        self.set_output_ids(self.get_output_ids()+[id_node])
    
    


