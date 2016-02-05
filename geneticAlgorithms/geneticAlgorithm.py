""""

@author: than_skourtan

"""

from random import random
from geneticAlgorithms.crossovers import uniform_crossover, ordered_crossover
from geneticAlgorithms.mutators import bit_string_mutation, swap_mutation
from geneticAlgorithms.encodings import Binary_encoding, Permutation_encoding
from geneticAlgorithms.fitnessFunctions import fitness_function, City, fitness_TSP

class Population:
    """Represents a population of individuals"""
    def __init__(self,population_size,individual_list, initialization = True):
        self.population_size = population_size
        #self.population_list = [(Binary_encoding(individual_list) if initialization == True else None) for i in range(population_size)] first problem
        self.population_list = [(Permutation_encoding(individual_list) if initialization == True else None) for i in range(population_size)]


def evaluation(population, cities):
    evaluation_list = []
    for individual in population.population_list:
        individual.fitness = fitness_TSP(individual, cities)
        evaluation_list.append(individual.fitness)
    
    evaluation_list = sorted(evaluation_list, reverse = True)
    population.population_list = sorted(population.population_list, key = lambda x:x.fitness, reverse = True)
    return evaluation_list



def generic_algorithm(fitness_function, fitness_threshold, population, crossover_rate,mutation_rate, cities, elitism):
    
    # evaluate 
    # evaluation_list = [fitness_function(individual) for individual in population.population_list] first problem
    
    evaluation_list = evaluation(population, cities)
    
    
    current_population = population
    generations = 0
    #while max(evaluation_list) < fitness_threshold: #fitness_threshold in the testing example is 1
    while generations < 10000:
        # crossover
        cross_over_population = Population(population.population_size,population.population_list[0].individual_size, False)
        
        #uniform_crossover(crossover_rate, population, cross_over_population, evaluation_list, elitism) 1o provlima
        ordered_crossover(crossover_rate, current_population, cross_over_population, evaluation_list, elitism) 
              
        # evaluation_list = evaluation(cross_over_population, cities)        
        # mutation
        mutate_population = Population(cross_over_population.population_size,cross_over_population.population_list[0].individual_size, False)
        #bit_string_mutation(mutation_rate, cross_over_population, mutate_population, elitism) 1o problima
        swap_mutation(mutation_rate, cross_over_population, mutate_population, elitism)
        
        #evaluation_list = [fitness_function(individual) for individual in mutate_population.population_list] 1o provlima
        current_population = mutate_population
        
        evaluation_list = evaluation(current_population, cities)
        
        print("The shortest distance is " , 1/max(evaluation_list), "and the route is ", current_population.population_list[0].individual_list)
        
        generations += 1
    

#===============================================================================
# TESTING
#===============================================================================

#i = Binary_array(10)

p = Population(10,100)

for i in p.population_list:
    print(i.individual_list)


cities = [City(random() * 100, random() * 100, i) for i in range(100)]
generic_algorithm(fitness_function,1,p,0.95,0.6,cities,1)













