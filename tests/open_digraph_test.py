import sys
import os
root = os.path.normpath(os.path.join(__file__, './../..'))
sys.path.append(root)# allows us to fetch files from the project root
import unittest
from modules.open_digraph import *


class InitTest(unittest.TestCase):
    def test_init_node(self):
        n0 = node(0, 'i', {}, {1:1})
        self.assertEqual(n0.id, 0)
        self.assertEqual(n0.label, 'i')
        self.assertEqual(n0.parents, {})
        self.assertEqual(n0.children, {1:1})
        self.assertIsInstance(n0, node)

class NodeTest(unittest.TestCase):
    def setUp(self):
        self.n0 = node(0, 'a', [], [1])
    def test_get_id(self):
        self.assertEqual(self.n0.get_id(), 0)
    def test_get_label(self):
        self.assertEqual(self.n0.get_label(), 'a')
    def testcopy(self):
        self.assertIsNot(self.n0, self.n0.copy())

class GraphTest(unittest.TestCase):
    def setUp(self):
        self.ad_node_2 = node(3,"hamid_1",{},{2:1})
        self.ad_node = node(2,"hamid_2",{3:1, 16:2},{16:1})
        self.ad_node_3 = node(16,"hamid_3",{2:1},{2:2, 19:1})
        self.ad_node_4 = node(19,"hamid_4",{16:1},{})
        self.ad_node_5=node(4, "hamid_5", {2:1},{3:2})
        self.ad_node_6=node(3,"hamid_1",{},{2:4})
        self.ad_node_7=node(4, "hamid_5", {2:1},{3:2})
        self.ad_node_8=node(4, "hamid_5", {2:1},{3:2})
        self.graph_1 = open_digraph([3],[19],[self.ad_node,self.ad_node_2, self.ad_node_3, self.ad_node_4])
        self.graph_2 = open_digraph([3],[19],[self.ad_node, self.ad_node_2, self.ad_node_3, self.ad_node_4, self.ad_node_5])
        self.graph_3 = open_digraph([23],[19],[self.ad_node,self.ad_node_2, self.ad_node_3, self.ad_node_4])
        self.graph_4 = open_digraph([3],[19, 190],[self.ad_node,self.ad_node_2, self.ad_node_3, self.ad_node_4])
        self.graph_5 = open_digraph([3],[19],[self.ad_node,self.ad_node_6, self.ad_node_3, self.ad_node_4])
    def test_well_formed (self):
        '''graph respectant toutes les conditions'''
        self.assertTrue(self.graph_1.is_well_formed())
        '''graph dont l'input a un parent'''
        self.assertFalse(self.graph_2.is_well_formed())
        '''graph dont lequel un des inputs n'existe pas dans le graph '''
        self.assertFalse(self.graph_3.is_well_formed())
        '''graph dont lequel un des inputs a un enfante dont sa multiplicité > 1 '''
        self.assertFalse(self.graph_5.is_well_formed())
        '''graph dont lequel un des outputs n'existepas dans le graph '''
        self.assertFalse(self.graph_4.is_well_formed())
        

    def test_ajooute_retire_noeud(self):
        self.graph_1.add_node("hamid_ajoute",{19:3}, {3:1})
        self.assertTrue(self.graph_1.is_well_formed())
        self.graph_1.remove_node_by_id(2)
        self.assertTrue(self.graph_1.is_well_formed())
        
    def test_ajoute_entree_sortie(self):
        

if __name__ == '__main__': # the following code is called only when
    unittest.main() # precisely this file is run
