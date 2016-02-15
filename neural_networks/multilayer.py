"""
Created 

@author: than_skourtan
"""
import numpy as np
import matplotlib
from math import e
from collections import OrderedDict
from neural_networks.activation_functions import sigmoid, linear




class Unit:
    def __init__(self, incoming_weight_array = [], input_value = None):
        self.incoming_weight_array = incoming_weight_array
        self.input_value = input_value
        
        

class Network:
    
    incoming_weight_array1 = np.array([[0.2], [-0.1], [0.4]])
    incoming_weight_array2 = np.array([[0.7], [-1.2], [1.2]])
    
    incoming_weight_array3 = np.array([[1.1],[0.1]])
    incoming_weight_array4 = np.array([[3.1],[1.17]])
    
    def __init__(self, input_units, number_of_units_in_layer):
        self.input_units = input_units
        self.number_of_units_in_layer = number_of_units_in_layer
        self.list_of_units = []
        
        
        for layer in number_of_units_in_layer.items():
            if layer[0] == 1:
                for unit in range(layer[1][0]):
                    self.list_of_units.append(Unit(input_value = input_units))
            elif layer[0] == 2:
                counter1 = 0
                for unit in range(layer[1][0]):
                    if counter1 == 0:
                        self.list_of_units.append(Unit(incoming_weight_array = self.incoming_weight_array1))
                        counter1 += 1
                    else: 
                        self.list_of_units.append(Unit(incoming_weight_array = self.incoming_weight_array2))
            elif layer[0] == 3:
                counter1 = 0
                for unit in range(layer[1][0]):
                    if counter1 == 0:
                        self.list_of_units.append(Unit(incoming_weight_array = self.incoming_weight_array3))
                        counter1 += 1
                    else: 
                        self.list_of_units.append(Unit(incoming_weight_array = self.incoming_weight_array4))
                        
                        
                        
        print("oe")  
    
    
    
    def forward_propagation(self):
        pass


#represents the inputs
input_array = np.array([10, 20, 30])

#represents the structure of the neural network
number_of_units_in_layer = OrderedDict({1 : (3, linear) , 2: (2, sigmoid), 3 : (2, sigmoid)})

print(input_array)
network = Network(input_array, number_of_units_in_layer)







