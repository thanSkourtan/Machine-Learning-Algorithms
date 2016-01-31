""""

@author: thanos

"""


from random import randint


class Population:
    
    def __init__(self,population_size,binary_array_length):
        self.population_list = [self.Individual(binary_array_length) for i in range(population_size)]
    
    
    
    
    class Individual:
        def __init__(self,binary_array_length):
            self.binary_array = [randint(0,1) for i in range(binary_array_length)]
    
    
    
    
    
        

def fitness_function(individual):
    """Assigns an evaluation score to each solution"""
    return sum(individual.binary_array)/len(individual.binary_array)

def generic_algorithm(fitness_function, fitness_threshold, population, crossover_rate,mutation_rate):
    
    evaluation_list = [fitness_function(individual) for individual in population]
    
    while max(evaluation_list)<fitness_threshold: #fitness_threshold in the testing example is 1
        #create a new population, a new generation
        pass



#===============================================================================
# TESTING
#===============================================================================

p = Population(10,15)

for i in p.population_list:
    print(i.binary_array)

generic_algorithm(fitness_function,1,p.population_list,0.1,0.2)