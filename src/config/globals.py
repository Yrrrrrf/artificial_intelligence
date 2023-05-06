# Global Settings for the application

# ? Imports -------------------------------------------------------------------------------------


from enum import Enum

import pygame


# ? Globals -------------------------------------------------------------------------------------


class Config(Enum):
    """
    Project Config
    """
    # App info
    NAME = "Artificial Intelligence"
    VERSION = "v0.1.0"
    
    # App settings
    WIDTH = 720
    HEIGHT = 480
    FPS = 60  # frames per second
    TILE_SIZE = 128
    GAME_SIZE = 3


# Initialize fonts...
pygame.font.init()  # initialize pygame font

class Theme(Enum):
    """
    App main colors
    """
    # Fonts
    TITLE = (255, 255, 255)
    TITLE_FONT = pygame.font.Font("resources/fonts/CascadiaCodeItalic.ttf", 16)

    # Colors
    BACKGROUND = (32, 32, 32)
    
