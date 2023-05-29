# """
# This module presents the Knapsack Problem and its solution using a genetic algorithm.

# This problem is a combinatorial optimization problem in which the goal is to maximize the value of objects in a knapsack without exceeding its capacity.
# """

import numpy as np  # import numpy
import EasyGA
# import chromosome from EasyGA
from EasyGA.structure.chromosome import Chromosome
import random  # import random

import matplotlib.pyplot as plt


#? Problem Statement ---------------------------------------------------------------------------

def run_knapsack_problem():
    """
    This function runs the knapsack problem.
    """
    print(f"\033[92mKnapsack Problem\033[0m", end="\n\n")
    # where x is a vector of binary values (0 or 1)
    # Maximize-> Z = sum(values * x)
    # subject to sum(weights * x) <= capacity

    population_size = 4  # number of solutions in each population
    n_generations = 100  # number of generations

    global n_objects
    n_objects = 15

    global bag_capacity
    bag_capacity = 100  # capacity of the bag

    global weights
    weights = np.random.randint(1, 10, n_objects)  # generate random weights
    print(f"Weights: {weights}")

    global fitness_values
    fitness_values = [0]  # list to store the fitness values

    # So any solution (a set of binary values) that has a sum of weights greater than the capacity is not valid.
    # The fitness function should return a low value for such solutions.

    # Create the Genetic algorithm
    ga: EasyGA.GA = EasyGA.GA()  # create the genetic algorithm instance

    # Basic Attributes
    ga.gene_impl = lambda: random.randint(0, 1)  # set the gene implementation  # type: ignore
    ga.chromosome_length = n_objects  # set the number of genes in the chromosome
    ga.fitness_goal = bag_capacity  # set the fitness goal

    # Size Attributes
    ga.population_size = population_size  # number of solutions in each population
    ga.generation_goal = n_generations  # number of generations

    ga.fitness_function_impl = fitness_function  # set the fitness function implementation  # type: ignore


    # ga.evolve()
    while ga.active():  # while the genetic algorithm is active (hasn't reached the goal)  # type: ignore
        ga.evolve(1)  # Evolve only a certain number of generations
        ga.print_generation()  # Print the current generation
        ga.print_best_chromosome()  # Print the best chromosome from that generations population
        print('-'*72, '\n')  # To divide the print to make it easier to look at
        print()  # Print a new line

    print("\033[92mFinal Generation\033[0m")
    ga.print_generation()
    ga.print_population()

    new_fitness_values = []
    for i in range(0, len(fitness_values), population_size):
        new_fitness_values.append(np.mean(fitness_values[i:i+population_size]))

    plt.figure(figsize=(10, 5))
    # plt.plot(fitness_values)
    plt.plot(new_fitness_values)
    plt.xlabel("Generation")
    plt.ylabel("Fitness Value")
    plt.title("Fitness Values")
    plt.show()


#? Fitness Function ----------------------------------------------------------------------------
def fitness_function(chromosome: Chromosome):
    """
    This function calculates the fitness value of a chromosome.
    The fitness function calculates the sum of products between each input and its corresponding weight.
    If the sum of the products is greater than the bag capacity, then the fitness value is set to zero.
    """
    genes: np.ndarray = np.array([gene.value for gene in chromosome.gene_list])  # get the chromosome genes as a numpy array
    
    print("G: ", end=" ")  # print the genes
    [print(f"{genes[i]:3}", end=" ") for i in range(len(genes))]  # print the gene

    print("\nW: ", end=" ")  # print the weights
    [print(f"{weights[i] if genes[i] == 1 else ' ':3}", end=" ") for i in range(len(weights))]  # print the weight only if the gene is 1

    sum_of_products: int = np.sum(genes * weights)  # calculate the sum of products between each input and its corresponding weight
    # print(f"= {sum_of_products}")  # print the sum of products
    # print on red if the sum of products is greater than the bag capacity
    print(f" = \033[91m{sum_of_products}\033[0m\n") if sum_of_products > bag_capacity else print(f" = {sum_of_products}\n")

    # add the fitness value to the fitness values list only if it's better than the previous one
    if len(fitness_values) == 0 or sum_of_products > fitness_values[-1]: fitness_values.append(sum_of_products)
    else: fitness_values.append(fitness_values[-1])  # if the fitness value is not better than the previous one, then add the previous one

    return 0 if sum_of_products > bag_capacity else sum_of_products  # if the sum of products is greater than the bag capacity, then the fitness value is set to zero
