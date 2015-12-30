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




point1 = Point(51,6.0,3.0)
point2 = Point(99,1.9,2.9)

print(euclidean_distance(point1,point2))