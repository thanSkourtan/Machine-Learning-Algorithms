"""
Created on 24 Nov 2015

Implements the ID3 algorithm as described in "Machine Learning", Tom Mitchell, Chapter 3

@author: thanSkourtan
"""

import itertools 
from math import log

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
    
    def __init__(self,label,attribute=None,value=None,left_child=None,right_sibling=None,parent=None):
        self.label = label
        self.attribute = attribute
        self.value = value
        self.left_child = left_child
        self.right_sibling = right_sibling
        self.parent = parent
        
        

def id3(data,target_attribute,attributes):
    
    values_distribution = values_per_column(data,len(data[0])-1)
    keys = list(values_distribution.keys())
    
    
    if len(keys) == 1 and keys[0] == "positive\\n":
        return Node("positive")
    elif len(keys) == 1 and keys[0] == "negative\\n":
        return Node("negative")
    elif len(keys) == 0:
        return Node()
    
    
    
#    for attribute in attributes:
        
    
    
    #Node()
    
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
          

def calculate_entropy(data,column):
    entropy = 0.0
    values_distribution = values_per_column(data,column)
    for separate_value in values_distribution.values():
        entropy -= separate_value/len(data)* log(separate_value/len(data),2)
    return entropy






file = [line.split(",") for line in itertools.islice(open("..//Python//heart_train.arff.txt"),16,None)]

#lala = values_per_column(file,13)

#lala = calculate_entropy(my_data,4)


#print(lala)

