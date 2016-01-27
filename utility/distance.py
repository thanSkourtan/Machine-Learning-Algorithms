'''


@author: than_skourtan
'''

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


