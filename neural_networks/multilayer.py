"""
Created 

@author: than_skourtan
"""
import numpy as np
import matplotlib

from collections import OrderedDict
from neural_networks.activation_functions import sigmoid, linear




class Unit:
    def __init__(self, layer, activate_function, incoming_weight_array = np.array([]), outgoing_weight_array = np.array([]), input_value = None): #TODO: delete the input value
        self.incoming_weight_array = incoming_weight_array
        self.outgoing_weight_array = outgoing_weight_array
        self.input_value = input_value
        self.layer = layer #layer that belongs to
        self.activate_function = activate_function
        self.output = 0
        self.error = 0
        

class Layer:
    """we define the Layer class as a way to manage input arrays, becauese input arrays belong to the layer, not to the inputs."""
    def __init__(self, output_array = []):
        self.output_array = output_array
        self.error_array = np.array([])
        
        
        
        

class Network:
    
    def __init__(self, learning_rate, output_array, target_array, number_of_units_in_layer):
        self.learning_rate = learning_rate
        self.number_of_units_in_layer = number_of_units_in_layer
        self.units = [] #the units
        
        #build the layers, assigning the input values only to the first
        self.layers = [Layer(output_array) if i == 0 else Layer() for i in range(len(number_of_units_in_layer))] #the layers
        
        self.target_array = target_array
        
        #produces a uniformly distributed number between [0,1)
        random_weight_values = lambda number_of_rows : 2 * np.random.random_sample((number_of_rows, 1)) - 1
        
        #finds number of units in previous layers
        previous_layers_units = lambda current_layer : number_of_units_in_layer[current_layer - 1][0]
        
        #build the units
        for current_layer, current_layer_data in number_of_units_in_layer.items():    
            if current_layer == 1:               #the first layer                                    
                for j in range(current_layer_data[0]):
                    self.units.append(Unit(current_layer, current_layer_data[1])) 
            elif current_layer != len(self.layers): #any layer but the last
                for i in range(current_layer_data[0]):
                    self.units.append(Unit(current_layer,current_layer_data[1],incoming_weight_array = random_weight_values(previous_layers_units(current_layer))))
                    
                    current_unit = self.units[-1]
                    counter = 0
                    for j, corresponding_unit in enumerate(self.units): #add weight in previous, corresponding unit
                        if corresponding_unit.layer == current_unit.layer - 1: #if we are at the previous layer
                            corresponding_unit.outgoing_weight_array = np.append(corresponding_unit.outgoing_weight_array, current_unit.incoming_weight_array[counter])
                            counter += 1
                            continue
                    
            else:         #last layer
                for i in range(current_layer_data[0]):
                    self.units.append(Unit(current_layer, current_layer_data[1], incoming_weight_array = random_weight_values(previous_layers_units(current_layer))))
                    current_unit = self.units[-1]
                    counter = 0
                    for j, corresponding_unit in enumerate(self.units): #add weight in previous, corresponding unit
                        if corresponding_unit.layer == current_unit.layer - 1: #if we are at the previous layer
                            corresponding_unit.outgoing_weight_array = np.append(corresponding_unit.outgoing_weight_array, current_unit.incoming_weight_array[counter])
                            counter += 1
                            continue
                        
        print("oe")  
        
    
    
    
    def forward_propagation(self):
        for unit in self.units:
            if unit.layer != 1:
                previous_layer = self.layers[unit.layer - 2] #for each layer we need the previous one
                current_layer = self.layers[unit.layer - 1]
                result = np.dot(previous_layer.output_array, unit.incoming_weight_array) 
                output = unit.activate_function(result)
                current_layer.output_array = np.append(current_layer.output_array, output) # append in np is static. it returns a new array
                unit.output = output #save it also at the unit
    
    
    def backpropagation(self):
        
        #calculate errors
        counter = 0
        for unit in reversed(self.units):
            current_layer = self.layers[unit.layer - 1]
            if unit.layer == 1: #if we reach the first layer stop
                break;
            elif unit.layer == len(self.layers): #if we are at the last layer
                unit.error = unit.output * (1.0 - unit.output) * (self.target_array[counter] - unit.output)    
                current_layer.error_array = np.insert(current_layer.error_array, 0, unit.error)
                counter = 1
            else: #if we are at a hidden layer
                unit.error = unit.output * (1.0 - unit.output) * np.dot(self.layers[unit.layer].error_array, unit.outgoing_weight_array) # error array of next layer and weight of current unit
                current_layer.error_array = np.insert(current_layer.error_array, 0,unit.error)
        
        
        change_layer = lambda layer1, layer2 : False if layer1 == layer2 else True 
        
        counter = -1
        previous_layer = -1
        #update weights 
        for unit in self.units:
            if change_layer(unit.layer, previous_layer):
                counter = 0
            else:
                counter += 1
            if unit.layer == 1: #if we are the first layer skip
                continue
            for i, (weight, input_value) in enumerate(zip(unit.incoming_weight_array, self.layers[unit.layer -2].output_array)): #i is the position of the unit at the layer
                
                new_weight = weight + self.learning_rate * unit.error * input_value 
                unit.incoming_weight_array[i] = new_weight #change the weight in current unit
                for j, corresponding_unit in enumerate(self.units): #change weight in corresponding unit
                    if corresponding_unit.layer == unit.layer - 1: #if we are at the previous layer
                        self.units[j + i].outgoing_weight_array[counter] = new_weight  #when we find the layer the unit is then i positions from it
                        break
            previous_layer = unit.layer 
        
        
        





#===============================================================================
# TESTING
#===============================================================================


#represents the inputs
input_array = np.array([(10), (30), (20)])
target_array = [0,1]

#represents the structure of the neural network
number_of_units_in_layer = OrderedDict({1 : (3, linear) , 2: (2, sigmoid), 3 : (2, sigmoid)})

network = Network(0.1, input_array, target_array, number_of_units_in_layer)

network.forward_propagation()

network.backpropagation()

print("lala")




