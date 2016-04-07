""""
@author: than_skourtan
"""

import unittest
from random import randint
from clustering.graph_theory import *
from utility import diagrams
import numpy as np

class MST(unittest.TestCase):
    
    def setUp(self):
        self.data = [Node(np.array([randint(0,100), randint(0,100)]), i) for i in range(0,5)]   
        #d = diagrams.Diagram()
        #d.scatter_plot(self.data)
        
    
    def test_construct_complete_graph(self):
        MST.graph = construct_complete_graph(self.data)
        
    def test_prim_mst(self):
        prim_mst(self.data, MST.graph)
    
    
if __name__ == "__main__":
    unittest.main()