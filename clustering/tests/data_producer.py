""""
@author: thanos
"""

from random import randint
from clustering.graph_theory import *
import numpy as np
from math import sqrt, pow


    
def four_corners_data(number_of_data_instances, data_range = (0, 100), rightX = 0.3, leftX = 0.3, upperY = 0.2, lowerY = 0.2):
    
    """      |      |
             |      |
    1(leftX)_|      |__2_(rightX)__
       
      ________       _____________
      3(leftX)|     |  4(rightX)
              |     |
    """

        
    x = lambda window : randint(data_range[0] if window == 1 or window == 3 else data_range[1] - rightX * data_range[1], 
                                data_range[1] if window == 2 or window == 4 else data_range[0] + leftX * data_range[1])
        
    y = lambda window : randint(data_range[0] if window == 3 or window == 4 else data_range[1] - upperY * data_range[1],
                               data_range[1] if window == 1 or window == 2 else data_range[0] + lowerY * data_range[1])
     
    
    data_instances = []         
    for i in range(number_of_data_instances):
        #window = randint(1,4)
        data_instances.append(Node(np.array([x(randint(1,4)),y(randint(1,4))]), i))
    
    return data_instances


def circle_in_circle(number_of_data_instances, data_range = (0, 100), center = (50, 50), r = 1):
    
    """             __
                  /   \ 
                 \____/                        
    """
    
    x = lambda : randint(int(center[0] - r if center[0] - r >=0 else data_range[0]),int( center[1] + r if center[1] + 4 <= data_range[1] else data_range[1]))
    #(x-j)**2 + (y -h)**2 = r**2
    y = lambda x : randint(int( -(sqrt(pow(r,2) + pow((x - center[0]),2)) + center[1])), int( sqrt(pow(r, 2) + pow((x - center[0]), 2)) + center[1])) 
    
    
    
    
    data_instances = []         
    for i in range(number_of_data_instances):
        #window = randint(1,4)
        l = x()
        data_instances.append(Node(np.array([l,y(l)]), i))
    
    return data_instances 
    















