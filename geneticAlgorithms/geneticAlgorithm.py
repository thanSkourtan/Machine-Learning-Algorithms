""""

@author: than_skourtan

"""


from geneticAlgorithms.crossovers import uniform_crossover
from geneticAlgorithms.mutators import bit_string_mutation
from geneticAlgorithms.encodings import Binary_encoding

class Population:
    """Represents a population of individuals"""
    def __init__(self,population_size,individual_list, initialization = True):
        self.population_size = population_size
        self.population_list = [(Binary_encoding(individual_list) if initialization == True else None) for i in range(population_size)]
                

def fitness_function(individual):
    """Assigns an evaluation score to each solution"""
    return sum(individual.individual_list)/individual.individual_size



def generic_algorithm(fitness_function, fitness_threshold, population, crossover_rate,mutation_rate):
    
    # evaluate 
    evaluation_list = [fitness_function(individual) for individual in population.population_list]
    final_population = None
    
    while max(evaluation_list) < fitness_threshold: #fitness_threshold in the testing example is 1
        # crossover
        cross_over_population = Population(population.population_size,population.population_list[0].individual_size, False)
        
        uniform_crossover(crossover_rate, population, cross_over_population, evaluation_list)
               
                
        # mutation
        mutate_population = Population(cross_over_population.population_size,cross_over_population.population_list[0].individual_size, False)
        bit_string_mutation(mutation_rate, cross_over_population, mutate_population)
        
        evaluation_list = [fitness_function(individual) for individual in mutate_population.population_list]
        final_population = mutate_population
        
        for indi in final_population.population_list:
            print(indi.individual_list)
    



#===============================================================================
# TESTING
#===============================================================================

#i = Binary_array(10)

p = Population(10,15)

for i in p.population_list:
    print(i.individual_list)

generic_algorithm(fitness_function,1,p,0.95,0.2)