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
        self.data = [Node(np.array([randint(0,100), randint(0,100)]), i) for i in range(0,10)]   
        #d = diagrams.Diagram()
        #d.scatter_plot(self.data)
        
    def test_construct_complete_graph(self):
        MST.graph = construct_complete_graph(self.data)
        d = diagrams.Diagram()
        #d.complete_graph_plot(graph)
        d.complete_graph_plot(self.data)
        
     
    def test_prim_mst(self):
        d = diagrams.Diagram()
        #d.complete_graph_plot(self.data)
        
        
        graph = construct_complete_graph(self.data)
        mst = prim_mst(self.data, graph)
        
        d.plot_mst_graph(mst, line_colour = "red")
        
        d.show_diagram()
        
        
        
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
        d1 = diagrams.Diagram()
        
        lala = graph_divided_in_clusters.keys()
        cluster_ids = set()
        
        for node in lala:
            cluster_ids.add(node.cluster_id)            
        cluster_data_list = [[] * len(cluster_ids)]
        '''
        for node in graph_divided_in_clusters:
            cluster_data_list[node.cluster_id].append(node)
        
        d1.scatter_plot(cluster_data_list[0], r = 3, outline_color = "red", fill_color = "red")
        d1.scatter_plot(cluster_data_list[1], r = 3, outline_color = "blue", fill_color = "blue")
        d1.show_diagram()
        '''
        
    
    
if __name__ == "__main__":
    #unittest.main()
    
    
    newSuite = unittest.TestSuite()
    newSuite.addTest(MST("test_prim_mst"))
    
    
    runner = unittest.TextTestRunner()
    runner.run(newSuite)
    
    
    