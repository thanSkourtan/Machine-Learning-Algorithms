'''
Includes functions of general use.
@author: than_skourtan
'''

from math import sqrt

def mean(data_list):
    """finds the mean of a list"""
    return sum(data_list)/float(len(data_list))

def standard_deviation(data_list):
    """finds the standard deviation of a list"""
    mean_of_list = round(mean(data_list), 3)
    sum_of_squares = 0.0
    for value in data_list:
        sum_of_squares += round(pow(value - mean_of_list, 2), 3)
    return sqrt(sum_of_squares/(len(data_list)-1))

def pick_up_column(data, column_no):
    """returns an attribute(variable) list out of a two dimensional data list"""
    attribute_list = []
    for row in data:
        attribute_list.append(row[column_no])
    return attribute_list

def pick_up_all_data_columns(data):
    """Returns a list containing lists of all columns of a two dimensional data list"""
    #TODO: see whether to use numpy in order to get a column out of an two dimensional array more easily
    data_columns= [[] for i in range(0, len(data[0]))]
    for row in data: 
        for i,attribute in enumerate(row):
                data_columns[i].append(attribute)
    return data_columns
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    