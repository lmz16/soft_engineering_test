from define import *
import extern
import pygame
from pygame.locals import *
import sys
import Game

def mainloop():
    # pygame.quit()
    # sys.exit()
    extern.singleplayergame.game_update()
    #extern.singleplayergame.interface_update()