"""
Main module for evolutive algorithms
This module contains the script that launch the GUI that shows the n-puzzle game. (TODO)

Author: Yrrrrrf
Date: Monday 13th, March 2023
"""


#? Imports ------------------------------------------------------------------------------------

# Own imports
import random
from config.globals import Config  # import config

from test.unit_test import Test  # import test class

#? Logic --------------------------------------------------------------------------------------


def main() -> None:
    """
    Application entry point. 

    It is also responsible for setting up the logging system and configuring it.
    """
    # Once created, the app will run until the user closes the window


if __name__ == "__main__":
    """
    This is the entry point of the application.
    Clean the terminal and print app data before running the main function.
    """
    print("\033[2J\033[1;1H", end="")  # clear terminal
    print(f"\033[92m{Config.NAME.value}\033[0m", end=" ")  # print n puzzle solver in green
    print(f"\033[97m{Config.VERSION.value}\033[0m", end="\n\n")  # print version in white

    main()  # run main function
