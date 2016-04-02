"""
@author: than_skourtan
"""

import unittest
import os
from csv import reader
import numpy as np
from utility import diagrams

test_file = os.path.join(os.path.dirname(__file__), "testdata.csv")


class test_single_layer_ann(unittest.TestCase):
    
    def setUp(self):
        prices = reader(open(test_file))
        
        d = diagrams.Diagram()
        y_axis = [i for i in range(1,16356)]
        price_data = [float(line.pop()) for line in prices]
        
        d.scatter_plot(y_axis, price_data,1)
        
        
        # format to input and target
        input_data = np.array([])
        target_data = np.array([])
        
        
        
            
    
    
    def test_sample(self):
        print("A")
        

if __name__ == "__main__":
    unittest.main()