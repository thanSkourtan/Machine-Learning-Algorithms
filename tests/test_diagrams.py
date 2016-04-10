"""
@author: thanos
"""

import unittest
from random import randint
from utility import diagrams
import linear_discriminant_functions.data_instance as dscrnt
import numpy as np
from clustering.graph_theory import *

class DiagramsTest(unittest.TestCase):
    
    def setUp(self):
        #builds the axes
        self.x_axis = [randint(0,100) for i in range(100)]
        self.y_axis = [(2*x+35) for x in self.x_axis]
        
        #builds the data_instances
        self.data_instances = [dscrnt.DataInstance(np.array([randint(0,100),randint(0,100)]), "", randint(0, 100)) for i in range(0,15)]
        #sets up the classes based on the linear function y = 2x + 35
        for data_instance in self.data_instances:
            if data_instance.feature_vector[-1] > (2*data_instance.feature_vector[0] + 35):
                data_instance.instance_class = "A"
            else:
                data_instance.instance_class = "B"
        self.data_instances = self.data_instances
        
        self.data = [Node(np.array([randint(0,100), randint(0,100)]), i) for i in range(0,7)]  
    
    
    def test_scatter_plotA(self):
        d = diagrams.Diagram()
        d.scatter_plot(self.x_axis, self.y_axis)
        
    
    def test_scatter_plotB(self):    
        d = diagrams.Diagram()
        d.scatter_plot(self.data_instances)
        
    def test_complete_graph_plot(self):
        d = diagrams.Diagram()
        d.complete_graph_plot(self.data_instances)
        
        
    def test_line_graph(self):
        pass
        #d = diagrams.Diagram()
        #d.line_graph(self.x_axis, self.y_axis)
        
    def test_plot_mst_graph(self):
        complete_graph = construct_complete_graph(self.data)
        mst = prim_mst(self.data, complete_graph)
        
        d = diagrams.Diagram()
        d.plot_mst_graph(mst)
        
        
    def test_double_data_instance_addition_in_scatterplot(self):
        d = diagrams.Diagram()
        data_instance1 = [dscrnt.DataInstance(np.array([100,150]), "", randint(1,10))]
        d.scatter_plot(data_instance1, outline_color = "red", fill_color = "red")
        data_instance2 = [dscrnt.DataInstance(np.array([100,100]), "", randint(1,10))]
        d.scatter_plot(data_instance2, outline_color ="blue", fill_color = "blue")
        d.show_diagram()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    
    
    suite = unittest.TestSuite()
    suite.addTest(DiagramsTest("test_double_data_instance_addition_in_scatterplot"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
