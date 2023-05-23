"""
This module presents the Knapsack Problem and its solution using a genetic algorithm.

This problem is a combinatorial optimization problem in which the goal is to maximize the value of objects in a knapsack without exceeding its capacity.
"""

import numpy as np  # import numpy
import pygad # import pygad


#? Fitness Function ----------------------------------------------------------------------------

def fitness_func(ga_instance, solution, solution_idx) -> float:
    """
    The fitness function. It accepts a solution (a set of numbers) and returns its fitness value.
    """
    output = np.sum(solution * function_inputs)
    return 1.0 / np.abs(output - desired_output)


#? Callbacks ----------------------------------------------------------------------------------

def callback_generation(ga_instance) -> None:
    """
    A callback function called for every generation.
    """
    pass
    # print(f"Generation = {ga_instance.generations_completed} | Best fitness = {ga_instance.best_solution()[1]} | Population = {ga_instance.population}")

#? Problem Statement ---------------------------------------------------------------------------

def run_knapscak_problem():
    """
    This function runs the knapsack problem.
    """
    print(f"\033[92mKnapsack Problem\033[0m", end="\n\n")

    num_generations: int = 100  # number of generations
    solves_per_population: int = 4  # number of solutions in each population

    mutation_percent_genes = 5  # percentage of genes to mutate
    mutation_type: str = "random"  # type of mutation operator

    crossover_percent_genes: int = 50  # percentage of genes to crossover

    #? Data ---------------------------------------------------------------------------------------

    # where x is a vector of binary values (0 or 1)
    # Maximize-> Z = sum(values * x)
    # subject to sum(weights * x) <= capacity


    np.random.seed(42)  # set a sed to reproduce results

    # create 2 random lists of integers
    n_objects: int = 12
    values: np.ndarray = np.random.randint(1, 100, n_objects)  # values of the objects
    weights: np.ndarray  = np.random.randint(1, 10, n_objects)  # weights of the objects


    global desired_output  # the desired output of the function
    desired_output = 15  # the desired output of the function

    global function_inputs  # function inputs
    function_inputs = {
        "weights": weights,
        "values": values,
    }


    #? Genetic Algorithm ---------------------------------------------------------------------------
    ga_instance = pygad.GA(
        num_generations=num_generations,
        num_parents_mating=solves_per_population,
        fitness_func=fitness_func,
        sol_per_pop=solves_per_population,
        num_genes=n_objects,
        gene_type=int,
        # gene_space={"low": 0, "high": 1}
    )



    # ga_instance.run()  # run the GA

