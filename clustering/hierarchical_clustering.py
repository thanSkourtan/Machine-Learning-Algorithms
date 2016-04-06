""" Contains the declaration of the cluster class and the implementation of the agglomerative clustering algorithm.
@author: than_skourtank
"""

from sys import float_info
from copy import copy
from distance_metrics import euclidean_distance
from utility.general import standard_deviation, mean, pick_up_column
from clustering.data_instance import DataInstance

class Cluster(DataInstance):
    """Class(Structure) that represents a cluster.
    
    Attributes:
        feature_vector(list): a list of cluster's feature data.
        left(Cluster): a pointer to the left child cluster.
        right(Cluster): a pointer to the right child cluster.
        distance(double): if the cluster has children, the distance is the distance of its children. Otherwise it is 0. Graphically, it is the
            height of each cluster.
        idn(int): the id number of the cluster
        label(string or int): the label of the data. It is obligatory.
        left_top_corner_x_coordinate(double): the x(horizontal) coordinate of the left top corner of the cluster shape (see print_cluster). It
            is used only when building the dendrogram.
    
    """
    def __init__(self, feature_vector = None, left=None, right=None, distance=0.0, idn=None, label=None, left_top_corner_x_coordinate=None): 
        DataInstance.__init__(self, feature_vector)
        self.left = left
        self.right = right
        self.distance = distance
        self.idn = idn
        self.label = label
        self.left_top_corner_x_coordinate = left_top_corner_x_coordinate

def agglomerative_clustering(data, distance = euclidean_distance,linkage=max):
    """Constructs a binary tree of clusters.
    The function contains the implementation of the agglomerative_clustering algorithm. 
    
    Parameters:
        data(list): a two dimensional list representing the data. The first column must be the labels of the data. The other columns must be attributes.
        distance (function object): a distance metric from the distanceMetrics module. Euclidean distance is the default value.
        linkage(function object): 
        
    Returns: 
        cluster_list(list): A binary tree represented by a list, containing all the clusters, starting from the lowest and ending at the top one.
        instances_num(int): the size of the data (TODO: although it saves time getting it here, see if is better to take it at the print_dendrogram function)
    
    """
    distances = {} #the dissimilarity matrix
    cluster_list = [] #the binary tree of clusters
    
    for i,row in enumerate(data):
        cluster_list.append(Cluster([feature_value for j, feature_value in enumerate(row) if j != 0],idn = i, label = row[0]))
    
    instances_num = len(cluster_list)
    last_idn = cluster_list[-1].idn  #gets the last id number
    
    #build the distances array
    for i in range(0, len(cluster_list)-1):
            for j in range(i+1,len(cluster_list)):
                distances[cluster_list[i].idn, cluster_list[j].idn]=distance(cluster_list[i], cluster_list[j])
    
    while(True):
        shortest = float_info.max
        shortest_cluster = ()
        changed = False
        #find the shortest distance
        for i in range(0,len(cluster_list)-1):
            if cluster_list[i].idn!=-1:
                for j in range(i+1,len(cluster_list)):
                    if cluster_list[j].idn!=-1:
                        if distances[cluster_list[i].idn, cluster_list[j].idn] < shortest:
                            shortest = distances[cluster_list[i].idn, cluster_list[j].idn] 
                            shortest_cluster = (copy(cluster_list[i]), copy(cluster_list[j]))
                            shortest_cluster_temp = cluster_list[i], cluster_list[j]
                            position_in_cluster_list = (i, j)
                            changed = True
        if not changed: 
            break
        
        #create a new cluster
        temporary_cluster = Cluster(left = shortest_cluster_temp[0], right = shortest_cluster_temp[1], distance = shortest, idn= last_idn+1)            
        last_idn +=1
        
        cluster_list[position_in_cluster_list[0]].idn=-1
        cluster_list[position_in_cluster_list[1]].idn=-1
        
        #restructure the distances dictionary
        temp_dictionary = {}
        for cluster in cluster_list:
            if cluster.idn!=-1:
                low_first = min(cluster.idn, shortest_cluster[0].idn)
                high_first = max(cluster.idn, shortest_cluster[0].idn)
                low_second  = min(cluster.idn, shortest_cluster[1].idn)
                high_second = max(cluster.idn, shortest_cluster[1].idn)
                
                temp_dictionary[cluster.idn, temporary_cluster.idn]=max(distances[low_first, high_first], distances[low_second, high_second])
                del distances[low_first, high_first]
                del distances[low_second, high_second]
        
        del distances[shortest_cluster[0].idn, shortest_cluster[1].idn] #TODO: see whether there is a less expensive way to do this, rather than deletion
        
        cluster_list.append(temporary_cluster)
        distances.update(temp_dictionary)
        
    return cluster_list, instances_num



##############################################################################################################################
#ON GOING DEVELOPMENT


def create_sets(N, total_sets,binary_array, i=0):
    """Finds the subsets of a givet set.
       
       The number of a set's subsets is 2 ^ n, where n = amount of elements belong to the set. The function uses a divide and conquer algorithm
       in order to represent the subsets to a binary array.
    """
    if(sum(binary_array) == N-1 or i==N): return
    binary_array[i]=1
    total_sets.append(copy(binary_array))
    #print(binary_array)
    create_sets(N, total_sets,binary_array, i+1)
    if(i!=0): 
        binary_array[i]=0
    else:
        return
    create_sets(N, total_sets, binary_array, i+1)
    

def divisive_clustering(data2, cluster_list = []):
    
    total_sets = []
    create_sets(len(data2), total_sets, binary_array =  [0] * len(data2))
    for a_set in total_sets:
        #break the set
        set0 = [i for i, element in enumerate(a_set) if element ==0]
        set1 = [i for i, element in enumerate(a_set) if element ==1]
        cluster_one = None
        cluster_two = None
        
        #base case
        if(len(set0)==1):
            #find the correct row, the correct instance
            position = a_set.index(1)
            base_cluster = Cluster(data2[position][0], data2[position][1], data2[position][2], data2[position][3], data2[position][4],
                                   data2[position][5], data2[position][6], data2[position][7], data2[position][8], data2[position][9], 
                                   idn = position, label = data2[position][10])
            cluster_list.append(base_cluster)
            return base_cluster
        #recursion
        else: #we pass only the data of the corresponding set
            partial_data = [row for i, row in enumerate(data2) if i in set0]
            cluster_one = divisive_clustering(partial_data)
            
            #Cluster(left = shortest_cluster_temp[0], right = shortest_cluster_temp[1], distance = shortest,idn= last_idn+1)   
        ########################################################################
        #same goes for sum1 ...
        #base case
        if(len(set1)==1):
            #find the correct row, the correct instance
            position = a_set.index(1)
            base_cluster = Cluster(data2[position][0], data2[position][1], data2[position][2], data2[position][3], data2[position][4],
                                   data2[position][5], data2[position][6], data2[position][7], data2[position][8], data2[position][9], 
                                   idn = position, label = data2[position][10])
            cluster_list.append(base_cluster)
            return base_cluster
        #recursion
        else: #we pass only the data of the corresponding set
            partial_data = [row for i, row in enumerate(data2) if i in set1]
            cluster_two = divisive_clustering(partial_data)
            cluster_list.append(Cluster(left = cluster_one, right = cluster_two))
        
        
            
    #new_cluster = Cluster()
    
    
    #def __init__(self, *features,left=None,right=None, distance=0.0, idn=None,label=None, left_top_corner_x_coordinate=None):


'''
standardizes the values of the list passed as argument
'''

def standardisation(data_list):
    m = mean(data_list)
    sd = standard_deviation(data_list)
    return [((row-m)/sd) for row in data_list]

    

