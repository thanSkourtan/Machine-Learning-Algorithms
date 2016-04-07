"""
@author: than_skourtan
"""

from heapq import heappush, heappop
import numpy as np
from distance_metrics import euclidean_distance
from sys import maxsize as max_integer
from data_instance import DataInstance

"""

References: CLRS for MST algorithm
"""
class Node(DataInstance):
    
    """DataInstance objects also work as the nodes of the graph with regards
       to the MST algorithm. 
    """
    def __init__(self, feature_vector, id):
        DataInstance.__init__(self, feature_vector)
        self.id = id
        self.min_edge_weight = max_integer
        self.parent = None
    
    def __lt__(self, other):
        return self.min_edge_weight < other.min_edge_weight
                
    
def mst(data):
    construct_complete_graph(data)
    pass
    
    
def construct_complete_graph(data):
    """Gets a list of data_instances and returns a graph represented by a two dimensional numpy array"""
    #data is a list of data_instances
    graph = np.zeros((len(data),len(data)))
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            graph[i][j] = graph[j][i] = euclidean_distance(data[i], data[j])
    return graph

def prim_mst(data, graph):
    
    data[0].min_edge_weight = 0
    
    heap = []
    for node in data:
        heappush(heap, node)
        
    while heap:        
        current_node = heappop(heap)
               
        for node in heap: #all nodes in heap are adjacent nodes, this would be wrong otherwise
            if graph[current_node.id][node.id] < node.min_edge_weight:
                    node.min_edge_weight = graph[current_node.id][node.id]
                    node.parent = current_node.id
    return data
    





