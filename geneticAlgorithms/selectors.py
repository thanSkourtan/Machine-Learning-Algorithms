'''

@author: thanos
'''

from random import random


def roulette_wheel_individual_selection(evaluation_list):
    """Represents a spinning wheel mechanishm for the selection of an individual out of the population."""
    population_fitness = sum(evaluation_list)
    wheel_spin = random() * population_fitness #the position in space [0,population_fitness] which represents the spinning of the wheel
    temp_fitness = 0
    for individual_position,individual_fitness in enumerate(evaluation_list): 
        temp_fitness += individual_fitness
        if temp_fitness > wheel_spin: 
            return individual_position