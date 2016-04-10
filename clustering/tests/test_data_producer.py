"""
@author: thanos
"""

import unittest
from utility.diagrams import *
from clustering.tests.data_producer import *

class TestDataProducer(unittest.TestCase):
    
    
    def test_four_corners_data(self):
        d = DataProducer()
        data_instances = d.four_corners_data(100)
        d = Diagram()
        d.scatter_plot(data_instances)
        d.show_diagram()
        
        
    def test_circle_in_circle(self):
        d = DataProducer()
        data_instances = d.circle_in_circle(1)
        d = Diagram()
        d.scatter_plot(data_instances)
        d.show_diagram()




if __name__ == "__main__":
    
    suite = unittest.TestSuite()
    suite.addTest(TestDataProducer("test_circle_in_circle"))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)
