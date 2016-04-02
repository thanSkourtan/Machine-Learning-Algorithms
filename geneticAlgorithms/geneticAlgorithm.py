""""

@author: than_skourtan

"""

from random import random
from geneticAlgorithms.crossovers import uniform_crossover, ordered_crossover
from geneticAlgorithms.mutators import bit_string_mutation, swap_mutation
from geneticAlgorithms.encodings import Binary_encoding, Permutation_encoding
from geneticAlgorithms.fitnessFunctions import fitness_function, City, fitness_TSP
from utility.diagrams import Diagram
from tkinter import *


class Population:
    """Represents a population of individuals"""
    def __init__(self,population_size,individual_list, initialization = True):
        self.population_size = population_size
        #self.population_list = [(Binary_encoding(individual_list) if initialization == True else None) for i in range(population_size)] first problem
        self.population_list = [(Permutation_encoding(individual_list) if initialization == True else None) for i in range(population_size)]


def evaluation(population, cities):
    #evaluation_list = [None] * population.population_list[0].individual_size
    evaluation_list = []
    for i, individual in enumerate(population.population_list):
        individual.fitness = fitness_TSP(individual, cities)
        #evaluation_list[i] = individual.fitness
        evaluation_list.append(individual.fitness)
    
    evaluation_list = sorted(evaluation_list, reverse = True)
    population.population_list = sorted(population.population_list, key = lambda x:x.fitness, reverse = True)
    return evaluation_list


def generic_algorithm(fitness_function, fitness_threshold, population, crossover_rate,mutation_rate, cities, elitism):
    
    # evaluate 
    # evaluation_list = [fitness_function(individual) for individual in population.population_list] first problem
    
    evaluation_list = evaluation(population, cities)
    
    starting_distance = 1/max(evaluation_list)
    current_population = population
    generations = 0
    #while max(evaluation_list) < fitness_threshold: #fitness_threshold in the testing example is 1
    while generations < 15000:
        # crossover
        cross_over_population = Population(population.population_size,population.population_list[0].individual_size, False)
        
        #uniform_crossover(crossover_rate, population, cross_over_population, evaluation_list, elitism) 1o provlima
        ordered_crossover(crossover_rate, current_population, cross_over_population, evaluation_list, elitism) 
              
        #evaluation_list = evaluation(cross_over_population, cities)        
        # mutation
        mutate_population = Population(cross_over_population.population_size,cross_over_population.population_list[0].individual_size, False)
        #bit_string_mutation(mutation_rate, cross_over_population, mutate_population, elitism) 1o problima
        
        swap_mutation(mutation_rate, cross_over_population, mutate_population, elitism)
        
        #evaluation_list = [fitness_function(individual) for individual in mutate_population.population_list] 1o provlima
        current_population = mutate_population
        
        evaluation_list = evaluation(current_population, cities)        
        current_best_distance = 0
        
        if 1/max(evaluation_list) != current_best_distance:
            task(current_population.population_list[0].individual_list)
        
        current_best_distance = 1/max(evaluation_list)
        
        generations += 1
        print(generations, "The shortest distance is " , current_best_distance )#, "and the route is ", current_population.population_list[0].individual_list)
        
    print("The starting distance was ", starting_distance, ". The best distance reached by the algorithm is ", 1/max(evaluation_list), ".")    
    return current_population.population_list[0].individual_list
    

#===============================================================================
# TESTING
#===============================================================================

def oe():
    p = Population(100, 100)
    best_route = generic_algorithm(fitness_function,1,p,0.95,0.001,cities,2)

def task(best_route):
    
    canvas.delete("all")
    best_route_of_cities = []
    
    for city_idn in best_route:
        for city in cities:
            if city_idn == city.idn:
                best_route_of_cities.append(city)
                
    x_axis = []
    y_axis = []
    
    for city in best_route_of_cities:
        x_axis.append(city.x)
        y_axis.append(city.y)
    
    largest_x = max(x_axis)
    largest_y = max(y_axis)
    
    r = 2
    point_height = lambda y : 100/2 + (700 - 100) * (1 - y/largest_y)  #because y-axis is reversed
    point_width = lambda x :  100/2 + (1000 * x/largest_x) # because the largest x will have width equal to width - hor_margins/2
    
    #draw the cities
    for i in range(len(x_axis)):
        canvas.create_oval(( point_width(x_axis[i]) - r,point_height(y_axis[i]) - r,point_width(x_axis[i]) + r,point_height(y_axis[i]) + r), outline="red", fill="red")
        
    #draw the route
    x_first = -1
    y_first = -1
    for i in range(len(x_axis)):
        if i == 0: # if first 
            x_previous = x_axis[i]
            y_previous = y_axis[i]
            x_first = x_axis[i]
            y_first = y_axis[i]
        elif i == (len(x_axis) - 1):
            canvas.create_line((point_width(x_axis[i]),point_height(y_axis[i]), point_width(x_previous), point_height(y_previous)),fill="blue")
            canvas.create_line((point_width(x_axis[i]),point_height(y_axis[i]), point_width(x_first), point_height(y_first)),  fill="blue")
        else:
            canvas.create_line((point_width(x_axis[i]),point_height(y_axis[i]), point_width(x_previous), point_height(y_previous)), fill="blue")
            x_previous = x_axis[i]
            y_previous = y_axis[i]
    
    root.update()
    
    


 



root=Tk() #make a window
canvas = Canvas(root,bg="white", height=700, width=1100)        
    
cities = [City(int(random() * 100), int(random() * 100), i) for i in range(100)]









#i = Binary_array(10)


root.after(200,oe)
canvas.pack() #pack the canvas into the root window

root.mainloop()



"""
best_route_of_cities = []

for city_idn in best_route:
    for city in cities:
        if city_idn == city.idn:
            best_route_of_cities.append(city)




x_axis = []
y_axis = []
for city in best_route_of_cities:
    x_axis.append(city.x)
    y_axis.append(city.y)
    
""" 
#d = Diagram()
#d.scatter_plot(x_axis,y_axis)    











