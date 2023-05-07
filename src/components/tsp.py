"""
Traveling Salesman Problem
"""

#? Imports ------------------------------------------------------------------------------------

from dataclasses import dataclass

import itertools
import pygame
import random
import numpy as np

from config.globals import Config, Theme

#? Logic --------------------------------------------------------------------------------------

#  create app class
@dataclass
class TSP:  # Traveling Salesman Problem
    n_points: int = 7
    screen: pygame.Surface = pygame.Surface((Config.WIDTH.value, Config.HEIGHT.value))


    def __init__(self, screen:pygame.Surface) -> None:
        """
        Initialize the app
        """
        self.screen = screen  # set surface
        print(f"\033[94mTraveling Salesman Problem\033[0m")


    def run(self) -> None:
        """
        Pop up the window and run the app while the user doesn't close the window
        """
        self.points = [(random.randint(0, Config.WIDTH.value), random.randint(0, Config.HEIGHT.value)) for _ in range(self.n_points)]
        [pygame.draw.circle(self.screen, (0, 255, 0), point, 5) for point in self.points]  # draw points
        pygame.display.update()  # update screen


    def get_distance_between_cities(self, city1: np.ndarray, city2: np.ndarray) -> float:
        """Get distance between two cities."""
        return np.hypot(city1[0] - city2[0], city1[1] - city2[1])  # return distance between two cities


    def exhaustive_search(self, cities: np.ndarray) -> np.ndarray:
        """
        Exhaustive search algorithm.
        This algorithm iterates over all possible solutions and returns the best one.
        
        ### Parameters:
            - `cities`: np.ndarray = Array of cities

        ### Returns:
            - `best_solution`: np.ndarray = Array of cities in the best order
        """
        best_solution: np.ndarray = np.arange(self.n_points)  # initialize best solution (any solution)
        best_fitness: float = np.sum([self.get_distance_between_cities(cities[best_solution[i]], cities[best_solution[i + 1]]) for i in range(self.n_points - 1)])  # initialize best fitness (any fitness)
        print(f"{best_fitness}", end="")  # print best fitness

        for solution in itertools.permutations(np.arange(self.n_points)):  # iterate over all possible solutions
            fitness: float = np.sum([self.get_distance_between_cities(cities[solution[i]], cities[solution[i + 1]]) for i in range(self.n_points - 1)])  # calculate fitness
            if fitness < best_fitness:
                # print(f"\n{solution}")  # print the current solution
                best_fitness, best_solution = fitness, solution  # update best fitness and best solution
                print(f" -> {best_fitness:4f}", end="")  # print best fitness
        print(f"\nBest fitness: {best_fitness}")  # print best fitness
        return best_solution  # return best solution (sequence of cities in the best order)


    def heaps_algorithm(self, cities: np.ndarray) -> np.ndarray:
        """
        Heap's algorithm.
        This algorithm iterates over all possible solutions and returns the best one.
        
        ### Parameters:
            - `cities`: np.ndarray = Array of cities

        ### Returns:
            - `best_solution`: np.ndarray = Array of cities in the best order
        """
        best_solution: np.ndarray = np.arange(self.n_points)


    # def heapPermutation(a, size):
    
    #     # if size becomes 1 then prints the obtained
    #     # permutation
    #     if size == 1:
    #         print(a)
    #         return
    
    #         for i in range(size):
    #         heapPermutation(a, size-1)
    
    #         # if size is odd, swap 0th i.e (first)
    #         # and (size-1)th i.e (last) element
    #         # else If size is even, swap ith
    #         # and (size-1)th i.e (last) element
    #         if size & 1:
    #             a[0], a[size-1] = a[size-1], a[0]
    #         else:
    #             a[i], a[size-1] = a[size-1], a[i]

    # # Driver code
    # a = [1, 2, 3]
    # n = len(a)
    # heapPermutation(a, n)



    




    # todo: implement nearest neighbor algorithm
    def nearest_neighbor(self, cities: np.ndarray) -> np.ndarray:
        """
        Nearest neighbor algorithm.
        This algorithm iterates over all possible solutions and returns the best one.
        
        ### Parameters:
            - `cities`: np.ndarray = Array of cities

        ### Returns:
            - `best_solution`: np.ndarray = Array of cities in the best order
        """
        best_solution: np.ndarray = np.arange(self.n_points)  # initialize best solution (any solution)
        best_fitness: float = np.sum([self.get_distance_between_cities(cities[best_solution[i]], cities[best_solution[i + 1]]) for i in range(self.n_points - 1)])  # initialize best fitness (any fitness)
        print(f"{best_fitness}", end="")  # print best fitness

        nearest_sequence: np.ndarray = np.array([best_solution[0]])  # select random city (first element of the best solution)
        pygame.draw.circle(self.screen, (0, 0, 255), self.points[nearest_sequence[0]], 5)  # repaint the first point in blue
        pygame.display.update()  # update screen

        for i in range(self.n_points):  # iterate over all possible solutions
            # get the nearest city of the last city in the sequence
            nearest_city: np.ndarray
            # get the distance from the last city in the sequence to all the other cities
            distances: np.ndarray = np.array([self.get_distance_between_cities(cities[nearest_sequence[-1]], cities[j]) for j in range(self.n_points)])
            # get the nearest city
            nearest_city = np.argmin(distances)
            # get the fitness of the new solution
            print(nearest_city)
            nearest_sequence = np.append(nearest_sequence, nearest_city)  # add nearest city to the sequence
        print(f"\nTotal fitness: {best_fitness}")  # print best fitness
        print(best_solution)
        return best_solution  # return best solution



    def draw_solution(self, best_solution: np.ndarray) -> None:
        """
        Draw the best solution.
    
        ### Parameters:
            - `best_solution`: np.ndarray = Array of cities in the best order
        """
        for i in range(self.n_points - 1):
            pygame.draw.line(self.screen, (0, 127, 0), self.points[best_solution[i]], self.points[best_solution[i + 1]], 1)
        pygame.draw.line(self.screen, (0, 127, 0), self.points[best_solution[-1]], self.points[best_solution[0]], 1)  # draw line between last and first point
        # draw total distance on screen
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(f"Total distance: {np.sum([self.get_distance_between_cities(self.points[best_solution[i]], self.points[best_solution[i + 1]]) for i in range(self.n_points - 1)])}", True, (0, 127, 0))
        self.screen.blit(text, (10, 10))

        pygame.display.update()  # update screen
                      

