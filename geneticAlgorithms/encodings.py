"""Collection of classes used to encode chromosomes
@author: than_skourtan
"""
from random import randint

class Binary_encoding:
    """Represents a hypothesis as a binary array"""
    def __init__(self,individual_list_length):
        self.individual_size = individual_list_length
        self.individual_list = [randint(0,1) for i in range(individual_list_length)]


class Permutation_encoding:
    """Represents a hypotheses as a permutation. Used in ordering problems such as Travelling Salesman Problem."""
    def __init__(self, individual_list_length):
        self.individual_size = individual_list_length
        self.individual_list = [i for i in range(0, individual_list_length)]

