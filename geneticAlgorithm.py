""""

@author: than_skourtan

"""


from random import randint,random


class Population:
    
    def __init__(self,population_size,binary_array_length, initialization = True):
        self.population_size = population_size
        self.population_list = [(Individual(binary_array_length) if initialization == True else None) for i in range(population_size)]
    
    
    
    
class Individual:
    """Represents the hypothesis instance. A hypothesis is represented as a binary array"""
    def __init__(self,binary_array_length):
        self.individual_size = binary_array_length
        self.binary_array = [randint(0,1) for i in range(binary_array_length)]    
    
    
    
    
def roulette_wheel_individual_selection(evaluation_list):
    """Represents a spinning wheel mechanishm for the selection of an individual out of the population."""
    population_fitness = sum(evaluation_list)
    wheel_spin = random() * population_fitness #the position in space [0,population_fitness] which represents the spinning of the wheel
    temp_fitness = 0
    for individual_position,individual_fitness in enumerate(evaluation_list): 
        temp_fitness += individual_fitness
        if temp_fitness > wheel_spin: 
            return individual_position
        

def fitness_function(individual):
    """Assigns an evaluation score to each solution"""
    return sum(individual.binary_array)/len(individual.binary_array)

def crossover_procedure(parent1, parent2):
    ancestor = Individual(parent1.individual_size)
    #half of the genes belong to parent 1, half to parent2
    for i in ancestor.binary_array:
        if 0.5 > random():
            ancestor.binary_array[i] = parent1.binary_array[i]
        else:
            ancestor.binary_array[i] = parent2.binary_array[i]
    return ancestor

def generic_algorithm(fitness_function, fitness_threshold, population, crossover_rate,mutation_rate):
    # create a new, uninitialized generation
    new_population = Population(population.population_size,population.population_list[0].individual_size, False)
    # evaluate 
    evaluation_list = [fitness_function(individual) for individual in population.population_list]
    
    while max(evaluation_list) < fitness_threshold: #fitness_threshold in the testing example is 1
        
        for i, individual in enumerate(population.population_list):
            if crossover_rate > random(): # this happens at 95% of times
                # build  
                parent1 = individual
                parent2 = population.population_list[roulette_wheel_individual_selection(evaluation_list)]
                ancestor = crossover_procedure(parent1, parent2) 
                new_population.population_list[i] = ancestor
            else: #this happens at 5% of times
                #add it to the new_population
                new_population.population_list[i] = individual
        
        
        
    



#===============================================================================
# TESTING
#===============================================================================

p = Population(10,15)

for i in p.population_list:
    print(i.binary_array)

generic_algorithm(fitness_function,1,p,0.95,0.2)