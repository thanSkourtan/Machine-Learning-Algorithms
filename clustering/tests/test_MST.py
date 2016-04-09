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
        self.data = [Node(np.array([randint(0,100), randint(0,100)]), i) for i in range(0,20)]   
        #d = diagrams.Diagram()
        #d.scatter_plot(self.data)
        
    def test_construct_complete_graph(self):
        MST.graph = construct_complete_graph(self.data)
        d = diagrams.Diagram()
        #d.complete_graph_plot(graph)
        d.complete_graph_plot(self.data)
        
     
    def test_prim_mst(self):
        d1 = diagrams.Diagram()
        d1.complete_graph_plot(self.data)
        MST.mst = prim_mst(self.data, MST.graph)
        d2 = diagrams.Diagram()
        d2.plot_mst_graph(mst)
        
        
        
        
    def test_inconsistent_edges(self):
        complete_graph = construct_complete_graph(self.data)
        mst = prim_mst(self.data, complete_graph)
        d = diagrams.Diagram()
        d.plot_mst_graph(mst)
        inconsistent_edges(mst, 3, 2)
    
    
    def test_cluster_divisioning(self):
        complete_graph = construct_complete_graph(self.data)
        mst = prim_mst(self.data, complete_graph)
        d = diagrams.Diagram()
        d.plot_mst_graph(mst)
        mst_with_inconsistency = inconsistent_edges(mst, 3, 2)
        graph_divided_in_clusters = cluster_divisioning(mst_with_inconsistency)
    
    
if __name__ == "__main__":
    #unittest.main()
    
    
    newSuite = unittest.TestSuite()
    newSuite.addTest(MST("test_cluster_divisioning"))
    
    
    runner = unittest.TextTestRunner()
    runner.run(newSuite)
    
    
    