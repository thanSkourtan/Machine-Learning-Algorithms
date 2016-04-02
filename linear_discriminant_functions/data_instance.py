"""""
@author: than_skourtan
"""



class DataInstance():
    
    """A dataInstance is defined by its coordinates and the class it belongs to.
    
    Attributes: 
        feature_vector(list): the feature vector  of a data instance.
        point_class(string): the name of class the instance of the corresponding point belongs to.
         
    """
    def __init__(self, feature_vector, instance_class):
        self.feature_vector = feature_vector                   
        self.instance_class = instance_class