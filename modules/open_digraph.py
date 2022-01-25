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
        return self.children
    
    def get_parent_ids(self):
        return self.parents

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
        return [node for node in nodes]





