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
general situations. Matlab pdist function gets passed the data array to return the similarity matrix.
"""

from math import sqrt
from utility.general import standard_deviation,pick_up_all_data_columns 


def jaccard_index(cluster1, cluster2):
    """Non-euclidean distance calculator, used for categorical data. Data concern presence - absence so their values are either 0 or 1."""
    if len(cluster1.feature_vector) != len(cluster2.feature_vector):
        print("The two points must be defined in the same dimensional space")
        return
    
    nominator = 0.0
    denominator = 0.0
    for i in range(0, len(cluster1.feature_vector)):
        if cluster1.feature_vector[i]==1 and cluster2.feature_vector[i]==1:
            nominator += 1
            denominator += 1
        elif cluster1.feature_vector[i] != cluster2.feature_vector[i]:
            denominator += 1
    return 1 - nominator/denominator


def euclidean_distance(cluster1, cluster2):
    """Calculates the euclidean distance of two clusters in the n-dimensional space, which is defined by the number of their attributes."""
    if len(cluster1.feature_vector) != len(cluster2.feature_vector):
        print("The two points must be defined in the same dimensional space.")
        return
    
    sum_of_squares = 0.0
    for i in range(0, len(cluster1.feature_vector)):
        sum_of_squares += pow(cluster1.feature_vector[i] - cluster2.feature_vector[i], 2)
    return sqrt(sum_of_squares)


def standardised_euclidean_distance(data,cluster1, cluster2):
    """Returns the euclidean distance of two clusters in the n-dimensional space, which is defined by the number of their attributes, 
       weighted by the inverse of the corresponding attribute's variance.
    """
    if len(cluster1.feature_vector) != len(cluster2.feature_vector):
        print("The two points must be defined in the same dimensional space.")
        return
    
    column_list = pick_up_all_data_columns(data)
    
    std_list = []
    for i,column in enumerate(column_list):
        if i != 0:         #because the first column is always the data labels
            std_list.append(standard_deviation(column))
    
    sum_of_squares = 0.0
    for i in range(0, len(cluster1.feature_vector)):
        sum_of_squares += 1/pow(std_list[i],2) * pow(cluster1.feature_vector[i] - cluster2.feature_vector[i], 2) #the weight here is the variance not the std
    return sqrt(sum_of_squares)


def chi_square_distance(data, cluster1, cluster2):
    """This distance metric is used only for categorical data."""
    
    if len(cluster1.feature_vector) != len(cluster2.feature_vector):
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
        relative_data.append([feature/temp_sum for i,feature in enumerate(row) if i !=0])
    
    column_list = pick_up_all_data_columns(relative_data)
    
    cluster1_list = []
    cluster2_list = []
    for feature in cluster1.feature_vector:
        cluster1_list.append(feature/sum(cluster1.feature_vector))
        
    for feature in cluster2.feature_vector:
        cluster2_list.append(feature/sum(cluster2.feature_vector))
    
    sum_of_squares = 0.0
    for i in range(0, len(cluster1_list)):
        sum_of_squares += (1/average_profiles[i]) * pow(cluster1_list[i] - cluster2_list[i], 2)
    return sqrt(sum_of_squares)










