"""
Created on 24 Nov 2015

Implements the ID3 algorithm as described here https://en.wikipedia.org/wiki/ID3_algorithm

@author: thanSkourtan
"""

import itertools 

class Node:
    
    """Represents the node of the decision tree.
    
    Each node corresponds to an attribute of the training set, a value of this attribute,
    and pointers to three nodes that define its position in the tree. The tree 
    representation was adopted by CLRS, Chapter 10, "Represented rooted trees" for the 
    case of arbitrary number of children.
    
    Parameters
    ----------
    attribute:
    value:
    left_child:
    right_child:
    parent:
    
    """
    
    def __init__(self,attribute=None,value=None,left_child=None,right_sibling=None,parent=None):
        self.attribute = attribute
        self.value = value
        self.left_child = left_child
        self.right_sibling = right_sibling
        self.parent = parent
        

#def id3(data):
 #   if()
  #  Node()
    
def values_per_column(data,column):
    """
    
    """
    
    values_distribution={}
    column_values=[line[column] for line in data]
    
    for value in column_values:
        if value not in values_distribution.keys():
            values_distribution[value]=1
        else:
            values_distribution[value] += 1
    return values_distribution
          


file = [line.split(",") for line in itertools.islice(open("..//Python//heart_train.arff.txt"),16,None)]

lala = values_per_column(file,13)

print(file)

