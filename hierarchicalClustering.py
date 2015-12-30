'''

@author: than_skourtan
'''

import math

class Point:
    '''
    The x-axis is indicated by the suffix 1, the y-axis is indicated by the suffix 2 etc.
    The coordinates are stored as instance variables and are also stored in a list in order
    to be better manipulated.
    '''
    def __init__(self,x1,x2,*args):
        self.x1 = x1
        self.x2 = x2
        self.list_of_coordinates= [self.x1,self.x2]
        for dimension in args:
            self.dimension = dimension
            self.list_of_coordinates.append(self.dimension)
        

'''
counts the euclidean distance of two points in the n-dimensional space in which they are definedxs
'''
    
def euclidean_distance(point1, point2):
    if len(point1.list_of_coordinates) != len(point2.list_of_coordinates):
        print("The two points must be defined in the same dimensional space")
        return
    sum_of_squares = 0.0
    for i in range(0,len(point1.list_of_coordinates)):
        sum_of_squares += pow(point1.list_of_coordinates[i]-point2.list_of_coordinates[i],2)
    return math.sqrt(sum_of_squares)


'''
finds the mean of a list 
'''

def mean(data_list):
    return sum(data_list)/float(len(data_list))

'''
finds the standard deviation of a list
'''

def standard_deviation(data_list):
    mean_of_list = round(mean(data_list),3)
    sum_of_squares = 0.0
    for value in data_list:
        sum_of_squares += round(pow(value - mean_of_list,2),3)
    return math.sqrt(sum_of_squares/(len(data_list)-1))


'''
standardizes the values of the list passed as argument
'''

def standardisation(data_list):
    m = mean(data_list)
    sd = standard_deviation(data_list)
    return [((row-m)/sd) for row in data_list]

    
'''
returns an attribute(variable) list out of a two dimensional data list
'''

def pick_up_column(data,column_no):
    attribute_list = []
    for row in data:
        attribute_list.append(row[column_no])
    return attribute_list

'''sample data'''


data = [[0,2,9,14,2,72,4.8,3.5,"S"],
        [26,4,13,11,0,75,2.8,2.5,"C"],
        [0,10,9,8,0,59,5.4,2.7,"C"],
        [0,0,15,3,0,64,8.2,2.9,"S"],
        [13,5,3,10,7,61,3.9,3.1,"C"],
        [31,21,13,16,5,94,2.6,3.5,"G"],
        [9,6,0,11,2,53,4.6,2.9,"S"],
        [2,0,0,0,1,61,5.1,3.3,"C"],
        [17,7,10,14,6,68,3.9,3.4,"C"],
        [0,5,26,9,0,69,10.0,3.0,"S"],
        [0,8,8,6,7,57,6.5,3.3,"C"],
        [14,11,13,15,0,84,3.8,3.1,"S"],
        [0,0,19,0,6,53,9.4,3.0,"S"],
        [13,0,0,9,0,83,4.7,2.5,"C"],
        [4,0,10,12,0,100,6.7,2.8,"C"],
        [42,20,0,3,6,84,2.8,3.0,"G"],
        [4,0,0,0,0,96,6.4,3.1,"C"],
        [21,15,33,20,0,74,4.4,2.8,"G"],
        [2,5,12,16,3,79,3.1,3.6,"S"],
        [0,10,14,9,0,73,5.6,3.0,"S"],
        [8,0,0,4,6,59,4.3,3.4,"C"],
        [35,10,0,9,17,54,1.9,2.8,"S"],
        [6,7,1,17,10,95,2.4,2.9,"G"],
        [18,12,20,7,0,64,4.3,3.0,"C"],
        [32,26,0,23,0,97,2.0,3.0,"G"],
        [32,21,0,10,2,78,2.5,3.4,"S"],
        [24,17,0,25,6,85,2.1,3.0,"G"],
        [16,3,12,20,2,92,3.4,3.3,"G"],
        [11,0,7,8,0,51,6.0,3.0,"S"],
        [24,37,5,18,1,99,1.9,2.9,"G"]]



'''
point1 = Point(51,6.0,3.0)
point2 = Point(99,1.9,2.9)

print(euclidean_distance(point1,point2))

'''
myList = pick_up_column(data,5)
lalala = standardisation(myList)

print("oe")









