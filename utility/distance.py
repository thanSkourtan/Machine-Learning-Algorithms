"""Includes distance utility functions

This module includes the following distance utility functions:

jaccard_index(cluster1,cluster2)
euclidean_distance(cluster1,cluster2)

Each functions takes two cluster objects as parameters and returns a double value.

@author: than_skourtan
"""

"""
TODO: examine if the paremeters, which are clusters, need to be changed in order the utility distance functions to apply to more
general situations.
"""

from math import sqrt

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
    """Calculates the euclidean distance of two clusters in the n-dimensional space, defined by the number of their attributes."""
    if len(cluster1.list_of_attributes) != len(cluster2.list_of_attributes):
        print("The two points must be defined in the same dimensional space.")
        return
    
    sum_of_squares = 0.0
    for i in range(0, len(cluster1.list_of_attributes)):
        sum_of_squares += pow(cluster1.list_of_attributes[i] - cluster2.list_of_attributes[i], 2)
    return sqrt(sum_of_squares)

    
def standardised_euclidean_distance(cluster1, cluster2):
    """Calculates the euclidean distance of two clusters in the n-dimensional space, defined by the number of their attributes."""
    if len(cluster1.list_of_attributes) != len(cluster2.list_of_attributes):
        print("The two points must be defined in the same dimensional space.")
        return
    
    weight = 15.615
    sum_of_squares = 0.0
    for i in range(0, len(cluster1.list_of_attributes)):
        sum_of_squares += 1/weight * pow(cluster1.list_of_attributes[i] - cluster2.list_of_attributes[i], 2)
    return sqrt(sum_of_squares)




def mean(data_list):
    '''
    finds the mean of a list 
    '''
    return sum(data_list)/float(len(data_list))

def standard_deviation(data_list):
    '''
    finds the standard deviation of a list
    '''
    mean_of_list = round(mean(data_list), 3)
    sum_of_squares = 0.0
    for value in data_list:
        sum_of_squares += round(pow(value - mean_of_list, 2), 3)
    #return sqrt(sum_of_squares/(len(data_list)-1))
    return (sum_of_squares/(len(data_list)-1))


lala = [-0.156,0.036,-0.998,-0.668,-0.860,1.253,-1.373,-0.860,-0.412,-0.348,-1.116,0.613,-1.373,0.549,1.637,0.613,1.381,-0.028,0.292,-0.092,-0.988,-1.309,1.317,-0.668,1.445,0.228,0.677,1.125,-1.501,1.573]

print(standard_deviation(lala))

class Cluster:
    
    def __init__(self,my_list):
        self.list_of_attributes = my_list
        
        
cluster1 = Cluster([51,6.0,3.0])
cluster2 = Cluster([99,1.9,2.9])

oe1 = standardised_euclidean_distance(cluster1,cluster2)
oe2 = euclidean_distance(cluster1,cluster2)
print(oe1)
print(oe2)









