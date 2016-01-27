"""Includes distance utility functions

This module includes the following distance utility functions:

jaccard_index(cluster1,cluster2)
euclidean_distance(cluster1,cluster2)
standardised_euclidean_distance(data,cluster1,cluster2)
chi_square_distance(data,cluster1,cluster2)

Each function takes two different clusters as parameters and calculates the distance between them, based on 
their attributes.

@author: than_skourtan
"""

"""
TODO: examine if the paremeters, which are clusters, need to change in order the utility distance functions to apply to more
general situations. Matlab pdist function uses the data array to return the similarity matrix.
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
        if i != 0:         #because the first column is always the data labels
            std_list.append(standard_deviation(column))
    
    sum_of_squares = 0.0
    for i in range(0, len(cluster1.list_of_attributes)):
        sum_of_squares += 1/pow(std_list[i],2) * pow(cluster1.list_of_attributes[i] - cluster2.list_of_attributes[i], 2) #the weight here is the variance not the std
    return sqrt(sum_of_squares)


def chi_square_distance(data, cluster1, cluster2):
    """This distance metric is used for categorical data."""
    
    if len(cluster1.list_of_attributes) != len(cluster2.list_of_attributes):
        print("The two points must be defined in the same dimensional space.")
        return
    
    column_list = pick_up_all_data_columns(data)
    total_attrs = []
    for i, data_list in enumerate(column_list):
        if i != 0:
            total_attrs.append(sum(data_list))
    average_profiles = [value/sum(total_attrs) for value in total_attrs]
    
    relative_data = []
    for row in data:
        temp_sum = sum(row[1:]) #skips the label column
        relative_data.append([attribute/temp_sum for i,attribute in enumerate(row) if i !=0])
    
    column_list = pick_up_all_data_columns(relative_data)
    
    cluster1_list = []
    cluster2_list = []
    for attribute in cluster1.list_of_attributes:
        cluster1_list.append(attribute/sum(cluster1.list_of_attributes))
        
    for attribute in cluster2.list_of_attributes:
        cluster2_list.append(attribute/sum(cluster2.list_of_attributes))
    
    sum_of_squares = 0.0
    for i in range(0, len(cluster1_list)):
        sum_of_squares += (1/average_profiles[i]) * pow(cluster1_list[i] - cluster2_list[i], 2)
    return sqrt(sum_of_squares)
    

class Cluster:
    
    def __init__(self,my_list):
        self.list_of_attributes = my_list
        
        
cluster1 = Cluster([0, 10, 9, 8, 0])
cluster2 = Cluster([32, 26, 0, 23, 0])




'''sample data'''
data = [["S", 0, 2, 9, 14, 2],  
        ["C", 26, 4, 13, 11, 0],  
        ["C", 0, 10, 9, 8, 0],  
        ["S", 0, 0, 15, 3, 0],  
        ["C", 13, 5, 3, 10, 7],  
        ["G", 31, 21, 13, 16, 5],  
        ["S", 9, 6, 0, 11, 2],  
        ["C", 2, 0, 0, 0, 1],  
        ["C", 17, 7, 10, 14, 6],  
        ["S", 0, 5, 26, 9, 0],  
        ["C", 0, 8, 8, 6, 7],  
        ["S", 14, 11, 13, 15, 0],  
        ["S", 0, 0, 19, 0, 6],  
        ["C", 13, 0, 0, 9, 0],  
        ["C", 4, 0, 10, 12, 0],  
        ["G", 42, 20, 0, 3, 6],  
        ["C", 4, 0, 0, 0, 0],  
        ["G", 21, 15, 33, 20, 0],  
        ["S", 2, 5, 12, 16, 3],  
        ["S", 0, 10, 14, 9, 0],  
        ["C", 8, 0, 0, 4, 6],  
        ["S", 35, 10, 0, 9, 17],  
        ["G", 6, 7, 1, 17, 10],  
        ["C", 18, 12, 20, 7, 0],  
        ["G", 32, 26, 0, 23, 0],  
        ["S", 32, 21, 0, 10, 2],  
        ["G", 24, 17, 0, 25, 6],  
        ["G", 16, 3, 12, 20, 2],  
        ["S", 11, 0, 7, 8, 0],  
        ["G", 24, 37, 5, 18, 1]]



oe1 = chi_square_distance(data,cluster1,cluster2)
print(oe1)










