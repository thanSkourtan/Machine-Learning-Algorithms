"""
Contains the implementation of three different algorithms used to learn the parameters of linear discriminant functions.
Least squares, fisher's linear discriminant and the perceptron algorithm. All three approaches are described in 'Pattern
Recognition and Machine Learning By Bishop'
@author: than_skourtan
"""
import numpy as np
from random import uniform



def perceptron_training_algorithm(data_instances, step = 0.1):
    """
    Attributes:
        data_instances(list): list of objects of DataInstance type.
    """

    #take a random weight vector
    decision_boundary_dimensions = len(data_instances[0].feature_vector) - 1
    w = np.array([uniform(1,100) for i in range(decision_boundary_dimensions + 1)])
    
    while(True):
        #find the misclassified instances
        misclassified_data = []
        for data_instance in data_instances:
            if  (data_instance.output <= np.dot(data_instance.feature_vector, np.transpose(w)) and data_instance.instance_class =='A') or \
            (data_instance.output > np.dot(data_instance.feature_vector, np.transpose(w)) and data_instance.instance_class =='B') :
                misclassified_data.append(data_instance)
                
        if misclassified_data is None:
            break
        
        correction_vector = np.array([0, 0])
        
        for misclassified_feature in misclassified_data:
            correction_vector +=  (1 if misclassified_feature.instance_class == 'A' else -1) * misclassified_feature.feature_vector
            
        
        w -= - step * correction_vector





def least_squares():
    pass



def fishers_discriminant():
    pass




