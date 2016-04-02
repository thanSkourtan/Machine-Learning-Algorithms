"""
@author: thanos
"""

import unittest
from random import randint
from utility import diagrams
import linear_discriminant_functions.discriminant_functions_algorithms as dscrnt
import numpy as np

class DiagramsTest(unittest.TestCase):
    
    def setUp(self):
        #builds the axes
        self.x_axis = [randint(0,100) for i in range(100)]
        self.y_axis = [(2*x+35) for x in self.x_axis]
        
        #builds the data_instances
        self.data_instances = [dscrnt.DataInstance(np.array([randint(0,100),randint(0,100)]), "") for i in range(0,100)]
        #sets up the classes based on the linear function y = 2x + 35
        for data_instance in self.data_instances:
            if data_instance.feature_vector[-1] > (2*data_instance.feature_vector[0] + 35):
                data_instance.instance_class = "A"
            else:
                data_instance.instance_class = "B"
        self.data_instances = self.data_instances
    
    
    
    def test_scatter_plotA(self):
        d = diagrams.Diagram()
        d.scatter_plot(self.x_axis, self.y_axis)
        
    
    def test_scatter_plotB(self):    
        d = diagrams.Diagram()
        d.scatter_plot(self.data_instances)
        
        
        
        
    def test_line_graph(self):
        pass
        #d = diagrams.Diagram()
        #d.line_graph(self.x_axis, self.y_axis)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
