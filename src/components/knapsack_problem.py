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

    num_generations: int = 100  # number of generations
    solves_per_population: int = 4  # number of solutions in each population

    mutation_percent_genes = 5  # percentage of genes to mutate
    crossover_percent_genes: int = 50  # percentage of genes to crossover

    #? Data ---------------------------------------------------------------------------------------

    # where x is a vector of binary values (0 or 1)
    # Maximize-> Z = sum(values * x)
    # subject to sum(weights * x) <= capacity

    # create 2 random lists of integers

    n_objects: int = 12
    # np.random.seed(42)  # set a sed to reproduce results
    # values: np.ndarray = np.random.randint(1, 100, n_objects)  # values of the objects
    # weights: np.ndarray  = np.random.randint(1, 10, n_objects)  # weights of the objects
    bag_capacity: int = 50  # capacity of the bag


    # just for testing
    values: np.ndarray = np.array([1, 4, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16])
    weights: np.ndarray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12])

    # So any solution (a set of binary values) that has a sum of weights greater than the capacity is not valid.
    # The fitness function should return a low value for such solutions.


    # Create the Genetic algorithm
    ga: EasyGA.GA = EasyGA.GA()  # create the genetic algorithm instance

    ga.gene_impl = lambda: random.randint(0, 1)  # set the gene implementation  # type: ignore

    # Basic Attributes
    ga.chromosome_length = n_objects  # set the number of genes in the chromosome
    ga.fitness_goal = 12  # set the fitness goal

    # Size Attributes
    ga.population_size = solves_per_population  # set the population size
    ga.generation_goal = num_generations  # set the number of generations

    # Fitness Attributes
    ga.fitness_function_impl = fitness_function  # set the fitness function  # type: ignore

    ga.evolve()

    # # # Print out the current generation and the population

    # while ga.active():  # while the genetic algorithm is active (hasn't reached the goal)
    #     ga.evolve(1)  # Evolve only a certain number of generations
    #     ga.print_generation()  # Print the current generation
    #     ga.print_best_chromosome()  # Print the best chromosome from that generations population
    #     print('-'*72)  # To divide the print to make it easier to look at

    ga.print_generation()
    ga.print_population()




#? Fitness Function ----------------------------------------------------------------------------
def fitness_function(chromosome: Chromosome):
    """
    This function calculates the fitness value of a chromosome.
    The fitness function calculates the sum of products between each input and its corresponding weight.
    If the sum of the products is greater than the bag capacity, then the fitness value is set to zero.
    """
    # get the chromosome genes
    # print(f"Type: {type(chromosome.gene_list[0].value)}")
    total_weight = 0  # initialize fitness value
    fitness: int = 0  # initialize fitness value

    for gene in chromosome.gene_list:
        if gene.value == 1:  # Check if its value = 1
            # If its value is 1 then add one to the overall fitness of the chromosome.
            fitness += 1

    return fitness  # return fitness value