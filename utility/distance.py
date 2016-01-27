"""Includes distance utility functions

This module includes the following distance utility functions:

jaccard_index(cluster1,cluster2)
euclidean_distance(cluster1,cluster2)
standardised_euclidean_distance(data,cluster1,cluster2)

@author: than_skourtan
"""

"""
TODO: examine if the paremeters, which are clusters, need to be changed in order the utility distance functions to apply to more
general situations. Matlab pdist function uses the data array to return the similarity matrix
"""

from math import sqrt
from utility.general import mean,standard_deviation,pick_up_all_data_columns 


def jaccard_index(cluster1, cluster2):
    """Non-euclidean distance calculator, used for categorical data. Data concern presence - absence so their values is either 0 or 1."""
    if len(cluster1.list_of_attributes) != len(cluster2.list_of_attributes):
        print("The two points must be defined in the same dimensional space")
        return
    
    nominator = 0.0
    denominator = 0.0
    for i in range(0, len(cluster1.list_of_attributes)):
        if cluster1.list_of_attributes[i]==1 and cluster2.list_of_attributes[i]==1:
            nominator += 1
            denominator += 1
        elif cluster1.list_of_attributes[i] != cluster2.list_of_attributes[i]:
            denominator += 1
    return 1 - nominator/denominator

    
def euclidean_distance(cluster1, cluster2):
    """Calculates the euclidean distance of two clusters in the n-dimensional space, which is defined by the number of their attributes."""
    if len(cluster1.list_of_attributes) != len(cluster2.list_of_attributes):
        print("The two points must be defined in the same dimensional space.")
        return
    
    sum_of_squares = 0.0
    for i in range(0, len(cluster1.list_of_attributes)):
        sum_of_squares += pow(cluster1.list_of_attributes[i] - cluster2.list_of_attributes[i], 2)
    return sqrt(sum_of_squares)

    
def standardised_euclidean_distance(data,cluster1, cluster2):
    """Returns the euclidean distance of two clusters in the n-dimensional space, which is defined by the number of their attributes, 
       weighted by the inverse of the corresponding attribute's variance.
    """
    if len(cluster1.list_of_attributes) != len(cluster2.list_of_attributes):
        print("The two points must be defined in the same dimensional space.")
        return
    
    column_list = pick_up_all_data_columns(data)
    
    std_list = []
    for i,column in enumerate(column_list):
        if i != 0:
            std_list.append(standard_deviation(column))
    
    sum_of_squares = 0.0
    for i in range(0, len(cluster1.list_of_attributes)):
        sum_of_squares += 1/pow(std_list[i],2) * pow(cluster1.list_of_attributes[i] - cluster2.list_of_attributes[i], 2) #the weight here is the variance not the std
    return sqrt(sum_of_squares)




class Cluster:
    
    def __init__(self,my_list):
        self.list_of_attributes = my_list
        
        
cluster1 = Cluster([51,6.0,3.0])
cluster2 = Cluster([99,1.9,2.9])



'''sample data'''
data = [["S", 72, 4.8, 3.5],  
        ["C", 75, 2.8, 2.5],  
        ["C", 59, 5.4, 2.7],  
        ["S",  64, 8.2, 2.9],  
        ["C", 61, 3.9, 3.1],  
        ["G",  94, 2.6, 3.5],  
        ["S",  53, 4.6, 2.9],  
        ["C", 61, 5.1, 3.3],  
        ["C",68, 3.9, 3.4],  
        ["S",  69, 10.0, 3.0],  
        ["C", 57, 6.5, 3.3],  
        ["S",  84, 3.8, 3.1],  
        ["S",  53, 9.4, 3.0],  
        ["C", 83, 4.7, 2.5],  
        ["C",  100, 6.7, 2.8],  
        ["G",  84, 2.8, 3.0],  
        ["C", 96, 6.4, 3.1],  
        ["G",  74, 4.4, 2.8],  
        ["S",  79, 3.1, 3.6],  
        ["S",  73, 5.6, 3.0],  
        ["C",  59, 4.3, 3.4],  
        ["S",  54, 1.9, 2.8],  
        ["G", 95, 2.4, 2.9],  
        ["C",  64, 4.3, 3.0],  
        ["G", 97, 2.0, 3.0],  
        ["S", 78, 2.5, 3.4],  
        ["G", 85, 2.1, 3.0],  
        ["G",  92, 3.4, 3.3],  
        ["S",  51, 6.0, 3.0],  
        ["G",  99, 1.9, 2.9]]



oe1 = standardised_euclidean_distance(data,cluster1,cluster2)
print(oe1)










