"""
Created 

@author: than_skourtan
"""
import numpy as np
from csv import reader
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
        self.layers = [Layer() if i == 0 else Layer() for i in range(len(number_of_units_in_layer))] #the layers
        self.output_array = output_array
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
                        
        print("initialization done")  
        
    
    
    
    def _forward_propagation(self, data_instance):
        #clear all the layers output arrays
        for layer in self.layers:
            layer.output_array = []
        
        #load the first instance to the first layer
        self.layers[0].output_array = data_instance
        
        
        for unit in self.units:
            if unit.layer != 1:
                previous_layer = self.layers[unit.layer - 2] #for each layer we need the previous one
                current_layer = self.layers[unit.layer - 1]
                result = np.around(np.dot(previous_layer.output_array, unit.incoming_weight_array), decimals = 8) 
                output = unit.activate_function(result)
                current_layer.output_array = np.append(current_layer.output_array, output) # append in np is static. it returns a new array
                
                unit.output = output #save it also at the unit
                
        print("the network's output is ", self.units[-1].output)
        for i, unit in enumerate(self.units):
            if i == 13:
                print(i, "'s forw incoming: ", unit.incoming_weight_array)
                print(i, "'s forw outgoing: ", unit.outgoing_weight_array)
            
    
    
    def _backpropagation(self, target_instance):
        #clear all the layers error arrays
        for layer in self.layers:
            layer.error_array = []
            
        #calculate errors
        for unit in reversed(self.units):
            current_layer = self.layers[unit.layer - 1]
            if unit.layer == 1: #if we reach the first layer stop
                break;
            elif unit.layer == len(self.layers): #if we are at the last layer
                unit.error = np.around(unit.output * (1.0 - unit.output) * (target_instance - unit.output), decimals = 8)    
                current_layer.error_array = np.insert(current_layer.error_array, 0, unit.error)
            else: #if we are at a hidden layer
                unit.error = np.around(unit.output * (1.0 - unit.output) * np.dot(self.layers[unit.layer].error_array, unit.outgoing_weight_array), decimals = 10) # error array of next layer and weight of current unit
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
        
        for i, unit in enumerate(self.units):
            if i == 13:
                print(i, "'s back incoming: ", unit.incoming_weight_array)
                print(i, "'s back outgoing: ", unit.outgoing_weight_array)
        
        
        
        
    def train(self):
        lalo = 1
        for data_instance, target_instance in zip(self.output_array, self.target_array):
            print("instance ", lalo, " --------------------------------------------------------------------")
            self._forward_propagation(data_instance)
            self._backpropagation(target_instance)
            lalo += 1
            if lalo == 8: break
        





#===============================================================================
# TESTING
#===============================================================================


housing = reader(open("..\\housing.csv"),delimiter=' ')
targets = reader(open("..\\target.csv"),delimiter=' ')


housing_data = [line for line in housing]
housing_temp = []

for i in range(len(housing_data)):
    housing_temp += [row.split(";") for row in housing_data[i]]
    
for i in range(len(housing_temp)):
    housing_temp[i] = [float(element) for element in housing_temp[i]]
    
final_housing_data = np.array(np.around(housing_temp,5))

################
target_data = [line for line in targets]

for i in range(len(target_data)):
    target_data[i] = [round(float(element),5) for element in target_data[i]]
    
    
final_target_data = np.array(target_data)




#represents the structure of the neural network
number_of_units_in_layer = OrderedDict({1 : (13, linear) , 2: (10, sigmoid), 3 : (1, linear)})

network = Network(0.1, final_housing_data, final_target_data, number_of_units_in_layer)

network.train()


print("oe")

"""
#represents the inputs
input_array = np.array([(10), (30), (20)])
target_array = [0,1]

#represents the structure of the neural network
number_of_units_in_layer = OrderedDict({1 : (3, linear) , 2: (2, sigmoid), 3 : (2, sigmoid)})

network = Network(0.1, input_array, target_array, number_of_units_in_layer)

network._forward_propagation()

network._backpropagation()

print("lala")
"""



