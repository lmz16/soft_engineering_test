from define import *
import extern
import pygame
from pygame.locals import *
import time
def startinit():

    extern.screen=pygame.display.set_mode(mainwindow_size,0,32)
    #extern.start_background_surface=pygame.Surface(mainwindow_size)
    extern.start_background=pygame.image.load(start_background_filename).convert()
    extern.start_background=pygame.transform.smoothscale(extern.start_background,mainwindow_size)
    extern.cursor=pygame.image.load(cursor_filename).convert_alpha()
    extern.cursor=pygame.transform.smoothscale(extern.cursor,cursor_size)
    extern.start_button=pygame.image.load(start_button_filename).convert_alpha()
    extern.start_button=pygame.transform.smoothscale(extern.start_button,start_button_size)
    extern.start_button_online=pygame.image.load(start_button_online_filename).convert_alpha()
    extern.start_button_online=pygame.transform.smoothscale(extern.start_button_online,start_button_online_size)
    extern.start_button_setting=pygame.image.load(start_button_setting_filename).convert_alpha()
    extern.start_button_setting=pygame.transform.smoothscale(extern.start_button_setting,start_button_setting_size)
    extern.start_button_help=pygame.image.load(start_button_help_filename).convert_alpha()
    extern.start_button_help=pygame.transform.smoothscale(extern.start_button_help,start_button_help_size)
    extern.start_button_custom=pygame.image.load(start_button_custom_filename).convert_alpha()
    extern.start_button_custom=pygame.transform.smoothscale(extern.start_button_custom,start_button_custom_size)
    extern.game_state=GAMEINIT
    extern.help_text=pygame.image.load(help_text_filename).convert_alpha()
    extern.help_text=pygame.transform.smoothscale(extern.help_text,help_text_size)

def cursorshow():
    [x,y]=pygame.mouse.get_pos()

    x-=extern.cursor.get_width()/2
    y-=extern.cursor.get_width()/2

    extern.screen.blit(extern.cursor,(x,y))


def start_blit():
    extern.screen.blit(extern.start_background,(0,0))
    extern.screen.blit(extern.start_button, \
    ((mainwindow_size[0]-start_button_size[0])/2, \
    mainwindow_size[1]*3/4-start_button_size[1]/2-start_button_size[1]*3))
    extern.screen.blit(extern.start_button_online, \
    ((mainwindow_size[0]-start_button_size[0])/2, \
    mainwindow_size[1]*3/4-start_button_size[1]/2-start_button_size[1]*1.5))
    extern.screen.blit(extern.start_button_setting, \
    ((mainwindow_size[0]-start_button_size[0])/2, \
    mainwindow_size[1]*3/4-start_button_size[1]/2+start_button_size[1]*0))
    extern.screen.blit(extern.start_button_help, \
    ((mainwindow_size[0]-start_button_size[0])/2, \
    mainwindow_size[1]*3/4-start_button_size[1]/2+start_button_size[1]*1.5))
    extern.screen.blit(extern.start_button_custom, \
    ((mainwindow_size[0]-start_button_size[0])/2, \
    mainwindow_size[1]*3/4-start_button_size[1]/2+start_button_size[1]*3))
def help_blit():
    extern.screen.blit(extern.help_text, \
    ((mainwindow_size[0]-help_text_size[0])/2, \
    mainwindow_size[1]/2-help_text_size[1]/2))


def mouseclick_respond(event):
    if(event.type==MOUSEBUTTONDOWN):
        if(event.button==1):
            if((abs(event.pos[0]-mainwindow_size[0]/2)<start_button_size[0]/2) \
            & (abs(event.pos[1]-3/4*mainwindow_size[1]+start_button_size[1]*3)<start_button_size[1]/2)& (extern.game_state == GAMEINIT)):
                extern.game_state=GAMESTART
            elif((abs(event.pos[0]-mainwindow_size[0]/2)<start_button_size[0]/2)  & (abs(event.pos[1]-3/4*mainwindow_size[1]-start_button_size[1]*1.5)<start_button_size[1]/2) & (extern.game_state==GAMEINIT)):
                extern.game_state=GAMEHELP
            elif((abs(event.pos[0]-mainwindow_size[0]/2)<help_text_size[0]/2) \
            & (abs(event.pos[1]-mainwindow_size[1]/2)<help_text_size[1]/2)\
            & (extern.game_state==GAMEHELP2)):
                extern.game_state=GAMEINIT1
    elif(event.type==MOUSEBUTTONUP):
        if(event.button==1 & (extern.game_state == GAMEHELP)):
            extern.game_state=GAMEHELP2
        if(event.button==1 & (extern.game_state == GAMEINIT1)):
            extern.game_state=GAMEINIT
            
            
