"""
@author: than_skourtan
"""

import numpy as np
from clustering.distance_metrics import euclidean_distance

class DataInstance:
    
    def __init__(self, feature_vector):
        self.feature_vector = feature_vector #should be numpy array
        
        
    
    
def mst(data):
    __construct_complete_graph(data)
    pass
    
    
def __construct_complete_graph(data):
    """Gets a list of data_instances and returns a graph represented by a two dimensional numpy array"""
    #data is a list of data_instances
    graph = np.zeros((len(data),len(data)))
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            graph[i][j] = graph[j][i] = euclidean_distance(data[i], data[j])
    return graph







