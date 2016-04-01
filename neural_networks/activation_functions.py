"""


@author: than_skourtan
"""

from math import exp



def sigmoid(number):
    """can take a number or a list of numbers"""
    oe = round(1 / (1 + exp(-number)), 5)
    return  oe


def binary_step(number):
    return 0 if number < 0 else 1

def linear(result):
    return result



