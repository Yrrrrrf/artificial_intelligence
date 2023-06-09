"""
Main module for evolutive algorithms

Author: Yrrrrrf
Date: Monday 13th, March 2023
"""


#? Imports ------------------------------------------------------------------------------------

# Own imports
import random

# import pygame
# from config.globals import Config  # import config
# from components.app import App  # import app
# from components.knapsack_problem import run_knapsack_problem  # import app

import numpy as np
import tensorflow as tf

from tensorflow import keras



#? Logic --------------------------------------------------------------------------------------


def main() -> None:
    """
    Application entry point. 

    It is also responsible for setting up the logging system and configuring it.
    """
    # Once created, the app will run until the user closes the window
    # app: App = App()  # create app instance
    # app.run()  # run app
    # run_knapsack_problem()
    pass


if __name__ == "__main__":
    """
    This is the entry point of the application.
    Clean the terminal and print app data before running the main function.
    """
    # import sys
    # print(f"Python version: {sys.version}")

    # print("\033[2J\033[1;1H", end="")  # clear terminal
    # print(f"\033[92m{Config.NAME.value}\033[0m", end=" ")  # print n puzzle solver in green
    # print(f"\033[97m{Config.VERSION.value}\033[0m", end="\n\n")  # print version in white

    # print python version

    main()  # run main function
