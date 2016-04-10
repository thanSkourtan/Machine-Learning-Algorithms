""""
@author: than_skourtan
"""

import unittest
from random import randint
from clustering.graph_theory import *
from utility import diagrams
import numpy as np
from clustering.tests.data_producer import *


color_list = ["red", "green", "orange", "blue4", "cyan2", "SeaGreen1", "green4", "khaki2",
              "yellow2", "DarkGoldenrod4", "pink4", "brown4", "maroon4", "gray4", "magenta4"]



class MST(unittest.TestCase):
    
    def setUp(self):
        self.data = [Node(np.array([randint(0,100), randint(0,100)]), i) for i in range(0,10)]   
        self.data =[Node(np.array([randint(0,100), randint(0,100)]), i) for i in range(0,10)] 
        #d = diagrams.Diagram()
        #d.scatter_plot(self.data)
        
    def test_construct_complete_graph(self):
        MST.graph = construct_complete_graph(self.data)
        d = diagrams.Diagram()
        #d.complete_graph_plot(graph)
        d.complete_graph_plot(self.data)
        
     
    def test_prim_mst(self):
        d = diagrams.Diagram()
        d.complete_graph_plot(self.data)
        
        
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
        data = four_corners_data(100)
        complete_graph = construct_complete_graph(data)
        mst = prim_mst(data, complete_graph)
        #d = diagrams.Diagram()
        #d.plot_mst_graph(mst)
        
        #na dw mipws apo dw kai katw epireazontai oi times twn diagrammatwn
        mst_with_inconsistency = inconsistent_edges(mst, 3, 2)
        
        ##############debug code#############
        l = diagrams.Diagram()
        l.plot_mst_graph(mst)
        
        graph_divided_in_clusters, no_of_clusters = cluster_divisioning(mst_with_inconsistency)
        d1 = diagrams.Diagram()
        
                 
        cluster_data_list = [[] for i in range(0,no_of_clusters)]
        
        for node in graph_divided_in_clusters:
            cluster_data_list[node.cluster_id].append(node)
        
        for i, cluster_list in enumerate(cluster_data_list):
            d1.scatter_plot(cluster_list, r = 2, outline_color = color_list[i % 15], fill_color = color_list[i % 15])
        
        d1.show_diagram()
        

        
        
    
    
if __name__ == "__main__":
    #unittest.main()
    
    
    newSuite = unittest.TestSuite()
    newSuite.addTest(MST("test_cluster_divisioning"))
    
    
    runner = unittest.TextTestRunner()
    runner.run(newSuite)
    
    
    