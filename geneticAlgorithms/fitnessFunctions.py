'''


@author: thanos
'''

from math import sqrt
from random import random
from geneticAlgorithms.encodings import Permutation_encoding

def fitness_function(individual):
    """Assigns an evaluation score to each solution"""
    return sum(individual.individual_list)/individual.individual_size


def fitness_TSP(individual, cities):
    
    euclidean_distance = lambda previous_city, current_city : sqrt(pow((previous_city.x - current_city.x), 2) + pow((previous_city.y - current_city.y), 2)) 

    total_distance = 0
    previous_city = None
    current_city = None
    for i, city_id in enumerate(individual.individual_list):
        if i == 0:
            previous_city = cities[city_id] # first city in individual 
        elif i == (individual.individual_size-1): # last city in individual
            current_city = cities[city_id]
            total_distance += euclidean_distance(previous_city, current_city)
            total_distance += euclidean_distance(current_city, cities[0]) #distance from last to first
        else:
            current_city = cities[city_id]
            total_distance += euclidean_distance(previous_city, current_city)
            previous_city = current_city
            
    return 1/total_distance

    
    
class City:
    
    def __init__(self, x, y, idn):
        self.idn = idn
        self.x = x
        self.y = y
        
        
        
##########
#TESTING

class Population:
    """Represents a population of individuals"""
    def __init__(self,population_size,individual_list, initialization = True):
        self.population_size = population_size
        self.population_list = [(Permutation_encoding(individual_list) if initialization == True else None) for i in range(population_size)]



population = Population(10,15)
cities = [City(int(random() * 10), int(random() * 10), i) for i in range(population.population_list[0].individual_size)]
lala = [fitness_TSP(individual, cities) for individual in population.population_list]

print(lala)






















