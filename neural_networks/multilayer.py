"""
Created 

@author: than_skourtan
"""
import numpy as np
import matplotlib

from collections import OrderedDict
from neural_networks.activation_functions import sigmoid, linear




class Unit:
    def __init__(self, layer, activate_function, weight_array = [], input_value = None):
        self.weight_array = weight_array
        self.input_value = input_value
        self.layer = layer #layer that belongs to
        self.activate_function = activate_function
        

class Layer:
    """we define the Layer class as a way to manage input arrays, becauese input arrays belong to the layer, not to the inputs."""
    def __init__(self, input_array = []):
        self.input_array = input_array
        
        

class Network:
    
    incoming_weight_array1 = np.array([[0.2], [-0.1], [0.4]])
    incoming_weight_array2 = np.array([[0.7], [-1.2], [1.2]])
    
    incoming_weight_array3 = np.array([[1.1],[0.1]])
    incoming_weight_array4 = np.array([[3.1],[1.17]])
    
    def __init__(self, input_array, number_of_units_in_layer):
        self.number_of_units_in_layer = number_of_units_in_layer
        self.units = [] #the units
        self.layers = []  #the layers
        
        #build the layers
        for layer in range(len(number_of_units_in_layer)):
            if layer == 0:
                self.layers.append(Layer(input_array))
            else:
                self.layers.append(Layer())
        
        #build the units
        for layer in number_of_units_in_layer.items():
            if layer[0] == 1:
                for unit in range(layer[1][0]):
                    self.units.append(Unit(layer[0], layer[1][1]))
            elif layer[0] == 2:
                counter1 = 0
                for unit in range(layer[1][0]):
                    if counter1 == 0:
                        self.units.append(Unit(layer[0], layer[1][1], weight_array = self.incoming_weight_array1))
                        counter1 += 1
                    else: 
                        self.units.append(Unit(layer[0], layer[1][1], weight_array = self.incoming_weight_array2))
            elif layer[0] == 3:
                counter1 = 0
                for unit in range(layer[1][0]):
                    if counter1 == 0:
                        self.units.append(Unit(layer[0], layer[1][1], weight_array = self.incoming_weight_array3))
                        counter1 += 1
                    else: 
                        self.units.append(Unit(layer[0], layer[1][1], weight_array = self.incoming_weight_array4))
                        
                        
                        
        print("oe")  
        
    
    
    
    def forward_propagation(self):
        for unit in self.units:
            if unit.layer != 1:
                previous_layer = self.layers[unit.layer - 2] #for each layer we need the previous one
                current_layer = self.layers[unit.layer - 1]
                result = np.dot(previous_layer.input_array, unit.weight_array) 
                output = unit.activate_function(result)
                current_layer.input_array = np.append(current_layer.input_array, output) # append in np is static. it returns a new array


#represents the inputs
input_array = np.array([(10), (30), (20)])

#represents the structure of the neural network
number_of_units_in_layer = OrderedDict({1 : (3, linear) , 2: (2, sigmoid), 3 : (2, sigmoid)})

network = Network(input_array, number_of_units_in_layer)

network.forward_propagation()






