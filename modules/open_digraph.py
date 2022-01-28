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
        return f'id : {self.id} , label : {self.label} , parents : {self.parents} , children : {self.children}'
    def __repr__(self):
        return f'id : {self.id} , label : {self.label} , parents : {self.parents} , children : {self.children}'

    
    def copy(self) :
        return node(self.id, self.label, self.parents, self.children)
    
    def get_id(self):
        return self.id
    
    def get_label(self):
        return self.label
    
    def get_children_ids(self):
        return self.children.keys()
    
    def get_parent_ids(self):
        return self.parents.keys()

    def set_id(self, id):
        self.id=id

    def set_label(self, label):
        self.label=label

    def set_parent_ids(self, parents):
        self.parents=parents

    def set_children_ids(self, children):
        self.children=children
        
    



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
        return f'id : {self.inputs} ,outputs : {self.outputs} nodes : {self.nodes}'

    def __repr__(self):
        return f'id : {self.inputs} ,outputs : {self.outputs} nodes : {self.nodes}'



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
        return f'cet id n existe pas '
    
    def get_nodes_by_ids(self, ids):
        return[self.get_node_by_id(id) for id in ids]
    
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
        
    def add_node(self, label="", parents={},children={}):
        new_node=node(self.new_id(), label, {}, {})
        self.nodes[new_node.get_id()]=new_node
        for i in parents.keys() :
            for j in range(parents[i]):
                self.add_edge(new_node.get_id(), i)
            
        for i in children.keys() :
            for j in range(children[i]):
                self.add_edge(i, new_node.get_id())

    


