# this module contains the code to show (in pygame) the solution of the n-travelers problem

#? Imports ------------------------------------------------------------------------------------

# Python imports
from threading import Thread
import pygame
import random
import time
from dataclasses import dataclass  # dataclass decorator

# Own imports
from config.globals import Config, Theme
from components.tsp import TSP

#? Logic --------------------------------------------------------------------------------------


#  create app class
@dataclass
class App:
    """
    App class
    This class contains the logic for the GUI
    """
    # App data (App State)
    screen: pygame.Surface = pygame.Surface((Config.WIDTH.value, Config.HEIGHT.value))
    running: bool = True
    play: bool = True

    def _init_(self) -> None:
        """
        Initialize the app
        """
        # print "App Running" on blue text
        print(f"\033[94mApp Running\033[0m")


    def run(self) -> None:
        """
        Pop up the window and run the app while the user doesn't close the window
        """
        pygame.init()  # initialize pygame
        self.screen = pygame.display.set_mode((Config.WIDTH.value, Config.HEIGHT.value))  # set window size
        pygame.display.set_caption(f"{Config.NAME.value} {Config.VERSION.value}")  # set window title
        pygame.display.set_icon(pygame.image.load("resources/img/puzzle.png"))
        self.clock = pygame.time.Clock()  # Initialize the clock

        # ? Test code --------------------------------------------------------------------------------

        selected_algorithm = "TSP"  # Traveling Salesman Problem
        tsp: TSP = TSP(self.screen)
        pygame.display.update()  # update screen

        if self.play:  # if the game is running
            self.screen.fill(Theme.BACKGROUND.value)  # fill the screen with the background color
            text = Theme.TITLE_FONT.value.render("Traveling Salesman Problem", True, Theme.TITLE.value)  # render the text
            self.screen.blit(text, (Config.WIDTH.value // 2 - text.get_width() // 2, 10))  # center the text

            match (selected_algorithm):  # switch statement                    
                case "TSP":
                    tsp.run()
                    # tsp.draw_solution(tsp.exhaustive_search(tsp.points))
                    tsp.draw_solution(tsp.nearest_neighbor(tsp.points))
                case _:  # Any other case
                    print(f"\033[91m{selected_algorithm} is not implemented\033[0m")


        # ? End of test code -------------------------------------------------------------------------

        while self.running:  # while the app is running
            self.clock.tick(60)  # set the fps to 60
            for event in pygame.event.get():  # get all events (user input)
                if event.type == pygame.QUIT:  # if the user clicks the close button
                    self.running = False  # stop the app
