"""Collection of crossover methods. 
@author: than_skourtan

"""

from random import random, randint
from geneticAlgorithms.selectors import roulette_wheel_individual_selection, tournament_selection
from geneticAlgorithms.encodings import Binary_encoding, Permutation_encoding


def uniform_crossover(crossover_rate, population, cross_over_population, evaluation_list):
    """Each gene of descendant is chosen from each of the two parents with a fixed 50% probability"""
    for i, individual in enumerate(population.population_list):
        if crossover_rate > random(): # this happens at 95% of times
            parent1 = individual
            parent2 = population.population_list[roulette_wheel_individual_selection(evaluation_list)]
            descendant = Binary_encoding(parent1.individual_size)
            for j,gene in enumerate(descendant.individual_list):
                if 0.5 > random():
                    descendant.individual_list[j] = parent1.individual_list[j]
                else:
                    descendant.individual_list[j] = parent2.individual_list[j]            
                
                
            cross_over_population.population_list[i] = descendant
        else: #this happens at 5% of times
            cross_over_population.population_list[i] = individual

    return cross_over_population


def ordered_crossover(crossover_rate, population, cross_over_population, evaluation_list, elitism):
    
    for i in range(elitism):
        cross_over_population.population_list[i] = population.population_list[i] 
    
    
    """Applies to cases such as the Travelling Salesman Problem, where the chromosome is an ordered list"""
    for i, individual in enumerate(population.population_list[elitism:],elitism):
        if crossover_rate > random() : # this happens at 95% of times
            parent1 = individual
            
            #parent2 = population.population_list[roulette_wheel_individual_selection(evaluation_list)] 1st problem
            parent2 = population.population_list[tournament_selection(population)]
            descendant = Permutation_encoding(parent1.individual_size)
            descendant.individual_list = [-1 for k in range(0, len(descendant.individual_list))]        
            
            
            offset1 = int(random() * parent1.individual_size)
            offset2 = int(random() * parent2.individual_size) # TODO: see if it has to be changed so that offsets do not get 0 or the highest values
            while offset2 == offset1: # offset1 and offest2 should be different numbers
                offset2 = int(random() * parent2.individual_size)
            min_boundary = min(offset1, offset2)
            max_boundary = max(offset1, offset2)
            
            
            
            #fill parent1 values
            for z in range(min_boundary,max_boundary):
                descendant.individual_list[z] = parent1.individual_list[z]
            
            
            #fill parent2 values    
            for j in range(descendant.individual_size):
                
                if j in range(min_boundary, max_boundary):
                    continue
                else:
                    position = (max_boundary + j) % parent2.individual_size # this is totally correct!!! do not change
                    value = parent2.individual_list[position]
                    while value in descendant.individual_list: 
                        position = (position + 1) % parent2.individual_size
                        value = parent2.individual_list[position]
                    
                    descendant.individual_list[j] = value
                     
                    
            cross_over_population.population_list[i] = descendant
        else: #this happens at 5% of times
            cross_over_population.population_list[i] = individual

    return cross_over_population
    
    

        
        
        
        
        
        
        
        
        
        
        