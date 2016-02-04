'''


@author: thanos
'''

from random import randint, random



def bit_string_mutation(mutation_rate, cross_over_population, mutate_population):
    
    for i, individual in enumerate(cross_over_population.population_list):
        for j, gene in enumerate(individual.individual_list):
            if mutation_rate > random(): # this happens at 20% of times      
                if gene == 0:
                    individual.individual_list[j] = 1    
                else:
                    individual.individual_list[j] = 0
        mutate_population.population_list[i] = individual
    return mutate_population
        

def swap_mutation(mutation_rate, cross_over_population, mutate_population):
    
    for i, individual in enumerate(cross_over_population.population_list):
        for j, gene in enumerate(individual.individual_list):
            if mutation_rate > random(): # this happens at 20% of times      
                swap_position = randint(0,individual.individual_size - 1)
                individual.individual_list[j] = individual.individual_list[swap_position]
                individual.individual_list[swap_position] = gene    
        mutate_population.population_list[i] = individual
    return mutate_population



