""""
@author: than_skourtan
"""

import unittest
from random import randint
from graph_theory import DataInstance, _construct_complete_graph
from utility import diagrams
import numpy as np

class MST(unittest.TestCase):
    
    
    
    def setUp(self):
        self.data = [DataInstance(np.array([randint(0,100), randint(0,100)])) for i in range(0,10)]   
        d = diagrams.Diagram()
        d.scatter_plot(self.data)
    
    def test_MST(self):
        _construct_complete_graph(self.data)
    
    
    
    
if __name__ == "__main__":
    unittest.main()