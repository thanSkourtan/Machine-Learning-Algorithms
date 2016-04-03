"""
@author: than_skourtan
"""

import unittest
import numpy as np
from utility import diagrams
from random import randint
import data_instance as dscrnt
import discriminant_functions_algorithms as dfa

class test_discriminant_functions(unittest.TestCase):
    
    
    def _init__(self, data_instances):
        self.data_instances = data_instances

    def setUp(self):
        
        
        
        #builds the dataset
        data_instances = [dscrnt.DataInstance(np.array([randint(0,100),1]), "", randint(0,100)) for i in range(0,100)]
                
        #sets up the classes based on the linear function y = 2x + 35
        for data_instance in data_instances:
            if data_instance.output > (2*data_instance.feature_vector[0] + 35):
                data_instance.instance_class = "A"
            else:
                data_instance.instance_class = "B"
        self.data_instances = data_instances
        
        #d = diagrams.Diagram()
        #d.scatter_plot(data_instances)
        
        '''
        x_axis = [randint(0,100) for i in range(100)]
        y_axis = [(2*x+35) for x in x_axis]
        d = diagrams.Diagram()
        d.scatter_plot(x_axis,y_axis);
        
        
        x_axis = [randint(0,100) for i in range(100)]
        y_axis = [(1*x+15) for x in x_axis]
        d = diagrams.Diagram()
        d.scatter_plot(x_axis,y_axis);
        '''

    def tearDown(self):
        pass


    def test_perceptron_training_algorithm(self):
        dfa.perceptron_training_algorithm(self.data_instances, True)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()