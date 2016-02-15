'''


@author: thanos
'''

from math import exp



def sigmoid(number):
    """can take a number or a list of numbers"""
    return 1 / 1 + exp(-number) #TODO: to change it


def binary_step(number):
    return 0 if number < 0 else 1



def linear():
    pass