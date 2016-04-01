"""
Contains the implementation of three different algorithms used to learn the parameters of linear discriminant functions.
Least squares, fisher's linear discriminant and the perceptron algorithm. All three approaches are described in 'Pattern
Recognition and Machine Learning By Bishop'
@author: than_skourtan
"""

from random import uniform

class DataInstance():
    
    """A dataInstance is defined by its coordinates and the class it belongs to.
    
    Attributes: 
        feature_vector(list): the feature vector  of a data instance.
        point_class(string): the name of class the instance of the corresponding point belongs to.
         
    """
    def __init__(self, feature_vector, instance_class):
        self.feature_vector = feature_vector                   
        self.instance_class = instance_class



def perceptron_training_algorithm(data_instances, step = 0.1):
    """
    Attributes:
        data_instances(list): list of objects of DataInstance type.
    """
    decision_boundary_dimensions = len(data_instances.feature_vector) - 1
    w = [uniform(1,100) for i in range(decision_boundary_dimensions + 1)]
    print("debug")





def least_squares():
    pass



def fishers_discriminant():
    pass




