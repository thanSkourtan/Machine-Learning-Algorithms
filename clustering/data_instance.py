"""
@author: than_skourtan
"""



class DataInstance():
    def __init__(self, feature_vector):
        self.feature_vector = feature_vector
        
        



def data_instances_to_lists(data_instances):
    """Converts the feature vectors of a list of data_instances to two lists of data applying
       to the x, y axis. Applies to cases where the graphical representation of data in the 
       two dimensional space is needed.
       """ 
    for data_instance in data_instances:
        if data_instance.feature_vector.size != 2:
            print("The data should have only 2 features.")
            return
        
    x_axis = [data_instance.feature_vector[0] for data_instance in data_instances]
    y_axis = [data_instance.feature_vector[1] for data_instance in data_instances]
    return x_axis, y_axis