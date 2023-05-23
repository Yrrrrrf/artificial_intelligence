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
        Initialize random points and draw them on the screen
        """
        self.points = [(random.randint(0, Config.WIDTH.value), random.randint(0, Config.HEIGHT.value)) for _ in range(self.n_points)]
        self.draw_points()  # draw points


    def draw_points(self) -> None:
        """
        Draw the points and the lines between them
        """
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
                best_fitness, best_solution = fitness, solution  # type: ignore
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
        return best_solution


    def nearest_neighbor(self, points: list[tuple[int, int]]) -> np.ndarray:
        """
        Nearest neighbor algorithm.
        This algorithm selects a node and then selects the node closest to the current node until all nodes have been visited.

        ### Parameters:
            - `points`: list[tuple[int, int]] = List of points

        ### Returns:
            - `nearest_route`: np.ndarray = Array of cities in the best order
        """
        visited = np.zeros(len(points), dtype=bool)  # Create a boolean array to keep track of visited points

        route = np.zeros(len(points), dtype=int)  # Create an array to store the indices of the visited points in the order of the route

        # Function to calculate the Euclidean distance between two points
        def calculate_distance(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return np.hypot(x1 - x2, y1 - y2)

        # Set the starting point as the first point in the list
        current_point = points[0]  # Set the current point to the starting point
        route[0] = 0  # Set the first point in the route to the starting point
        visited[0] = True  # Set the starting point as visited

        for i in range(1, len(points)):  # Iterate over the remaining points
            # Initialize the minimum distance and nearest neighbor
            min_distance = np.inf  # Set the minimum distance to infinity
            nearest_neighbor_index = -1  # Set the nearest neighbor to -1
            for j in range(len(points)):  # Find the nearest neighbor
                if not visited[j]:  # If the point has not been visited
                    distance = calculate_distance(current_point, points[j])  # Calculate the distance between the current point and the point being checked
                    if distance < min_distance:  # If the distance is less than the minimum distance
                        min_distance, nearest_neighbor_index = distance, j  # Update the minimum distance and nearest neighbor

            # Update the current point, route, and visited array
            current_point = points[nearest_neighbor_index]  # Update the current point
            route[i] = nearest_neighbor_index  # Update the route
            visited[nearest_neighbor_index] = True  # Update the visited array

        print(route)
        print(np.sum([self.get_distance_between_cities(points[route[i]], points[route[i + 1]]) for i in range(self.n_points - 1)]))
        return route



    def draw_solution(self, solution: np.ndarray) -> None:
        """
        Draw the best solution.
    
        ### Parameters:
            - `solution`: np.ndarray = Array of cities in the best order
        """
        for i in range(self.n_points - 1):
            pygame.draw.line(self.screen, (0, 127, 0), self.points[solution[i]], self.points[solution[i + 1]], 1)
        pygame.draw.line(self.screen, (0, 127, 0), self.points[solution[-1]], self.points[solution[0]], 1)  # draw line between last and first point

        font = pygame.font.SysFont("Arial", 16)
        text = font.render(f"Total distance: {np.sum([self.get_distance_between_cities(self.points[solution[i]], self.points[solution[i + 1]]) for i in range(self.n_points - 1)])}", True, (0, 127, 0))
        self.screen.blit(text, (8, 8))

        pygame.display.update()  # update screen
                      
