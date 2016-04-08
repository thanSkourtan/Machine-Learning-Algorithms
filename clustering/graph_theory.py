"""
@author: than_skourtan
"""

from heapq import heappush, heappop
import numpy as np
from distance_metrics import euclidean_distance
from sys import maxsize as max_integer
from clustering.data_instance import DataInstance
from utility.general import mean, standard_deviation

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
        self.inconsistence = False
        self.mean = 0.0
        self.standard_deviation = 0.0 
        self.cluster = None
    
    
    def __lt__(self, other):
        return self.min_edge_weight < other.min_edge_weight
                
    
def mst(data):
    construct_complete_graph(data)
    pass
    
    
def construct_complete_graph(data):
    """Gets a list of data_instances and returns a graph represented by a two dimensional numpy array"""
    #data is a list of data_instances
    complete_graph = np.zeros((len(data),len(data)))
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            complete_graph[i][j] = complete_graph[j][i] = euclidean_distance(data[i], data[j])
    return complete_graph

def prim_mst(data, complete_graph):
    """We only need to initialize the min_edge_weight and the parent attribute in data list and there's our MST!"""
    data[0].min_edge_weight = 0
    
    heap = []
    for node in data:
        heappush(heap, node)
        
    while heap:        
        current_node = heappop(heap)
               
        for node in heap: #all nodes in heap are adjacent nodes, this would be wrong otherwise
            if complete_graph[current_node.id][node.id] < node.min_edge_weight:
                    node.min_edge_weight = complete_graph[current_node.id][node.id]
                    node.parent = current_node
    
        
    return data #undercover MST
    

def inconsistent_edges(mst, k, q):    
    
    """We are  building the mst in the form of an adjacency list, which will provide a better way to find the adjacent edges in the 
       inconsistent_edges algorithm
    """
    adjacency_list = {node : [] for node in mst} # adjacent nodes for every node
    for node in mst: #keep only the parent
        if node.parent is not None:
            adjacency_list[node].append(node.parent) #fill in the parent
            adjacency_list[node.parent].append(node) #one's parent is another man's child!
    
    """Nodes can also represent edges(except for the initial node), as they include all relative info: the 
       distance, the current node and the parent node
    """
    for edge in adjacency_list:
        used = set()
        counter = k-1
        all_neighbour_nodes = set(adjacency_list.get(edge))
        used = all_neighbour_nodes
        current_frontier = all_neighbour_nodes
        while counter > 0 and current_frontier:
            temp = set()
            for adj_edge in current_frontier:
                temp = temp | set([item for item in adjacency_list.get(adj_edge) if item is not edge])
                
            
            current_frontier = temp - used
            used = used | temp
            all_neighbour_nodes = all_neighbour_nodes | temp
            counter -= 1
            
        print("the neighbours for ", edge.id, " are", end =" ")
        
        '''debug code'''
        for lala in all_neighbour_nodes:
            print(lala.id, end = ",")
        print()
        
        weights_list = [node.min_edge_weight for node in all_neighbour_nodes]
        edge.mean = mean(weights_list)
        edge.standard_deviation = standard_deviation(weights_list)
        if (edge.min_edge_weight > (q * edge.standard_deviation + edge.mean)):
            edge.inconsistence = True
            
    
       
"""
    for second_edge in other_edges:
        if second_edge is the most k steps from edge:
            list _of_edge. append(second_edge)
    
    mean(twn weigths tis parapanw listas)
    std(twn weigths tis parapanw listas )
    
    if (edge.min_edge_weight > q * std)
    
"""



