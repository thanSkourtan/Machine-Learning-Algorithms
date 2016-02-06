'''

@author: thanos
'''

from random import random, randint

def roulette_wheel_individual_selection(evaluation_list):
    """Represents a spinning wheel mechanishm for the selection of an individual out of the population."""
    population_fitness = sum(evaluation_list)
    wheel_spin = random() * population_fitness #the position in space [0,population_fitness] which represents the spinning of the wheel
    temp_fitness = 0
    for individual_position,individual_fitness in enumerate(evaluation_list): 
        temp_fitness += individual_fitness
        if temp_fitness > wheel_spin: 
            return individual_position
        
        
def tournament_selection(population, tournament_size = 15):
    
    random_individual_positions = []
    for i in range(tournament_size):
        random_number = randint(0, population.population_size - 1)
        random_individual_positions.append(random_number)
    
    max_fitness = -1
    max_position = -1
    for position in random_individual_positions:
        if max_fitness < population.population_list[position].fitness:
            max_fitness = population.population_list[position].fitness
            max_position = position
    
    return max_position



