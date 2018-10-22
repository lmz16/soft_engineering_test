from define import *
import extern
import pygame
from pygame.locals import *

def startinit():

    extern.screen=pygame.display.set_mode(mainwindow_size,0,32)
    #extern.start_background_surface=pygame.Surface(mainwindow_size)
    extern.start_background=pygame.image.load(start_background_filename).convert()
    extern.start_background=pygame.transform.smoothscale(extern.start_background,mainwindow_size)
    extern.cursor=pygame.image.load(cursor_filename).convert_alpha()
    extern.cursor=pygame.transform.smoothscale(extern.cursor,cursor_size)
    extern.start_button=pygame.image.load(start_button_filename).convert_alpha()
    extern.start_button=pygame.transform.smoothscale(extern.start_button,start_button_size)

    extern.game_state=GAMEINIT


def cursorshow():
    [x,y]=pygame.mouse.get_pos()

    x-=extern.cursor.get_width()/2
    y-=extern.cursor.get_width()/2

    extern.screen.blit(extern.cursor,(x,y))

def start_blit():
    extern.screen.blit(extern.start_background,(0,0))
    extern.screen.blit(extern.start_button, \
    ((mainwindow_size[0]-start_button_size[0])/2, \
    mainwindow_size[1]*3/4-start_button_size[1]/2))

def mouseclick_respond(event):
    if(event.type==MOUSEBUTTONDOWN):
        if(event.button==1):
            if((abs(event.pos[0]-mainwindow_size[0]/2)<start_button_size[0]/3) \
            & (abs(event.pos[1]-3/4*mainwindow_size[1])<start_button_size[1]/7)):
                extern.game_state=GAMESTART
