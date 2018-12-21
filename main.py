from define import *
import extern
import pygame
from pygame.locals import *
import os
import Game
import threading

def mainloop():
    extern.singleplayergame.game_update()
    