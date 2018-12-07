from define import *
import extern
import pygame
from pygame.locals import *
import time
import Resource

def startinit():
    extern.interface_resource=Resource.RInterface('Resource/json/interface')
    extern.game_state=GAMEINIT
    extern.last_fresh_time=time.time()

def cursorshow():
    [x,y]=pygame.mouse.get_pos()

    x-=extern.interface_resource.cursor.get_width()/2
    y-=extern.interface_resource.cursor.get_width()/2

    extern.interface_resource.screen.blit(extern.interface_resource.cursor,(x,y))


def start_blit():
    extern.interface_resource.screen.blit(extern.interface_resource.start_background,(0,0))
    extern.interface_resource.screen.blit(
        extern.interface_resource.start_button, 
        ((mainwindow_size[0]-start_button_size[0])/2, 
        mainwindow_size[1]*3/4-start_button_size[1]/2-start_button_size[1]*3)
        )
    extern.interface_resource.screen.blit(
        extern.interface_resource.start_button_online,
        ((mainwindow_size[0]-start_button_size[0])/2,
        mainwindow_size[1]*3/4-start_button_size[1]/2-start_button_size[1]*1.5)
        )
    extern.interface_resource.screen.blit(
        extern.interface_resource.start_button_setting,
        ((mainwindow_size[0]-start_button_size[0])/2,
        mainwindow_size[1]*3/4-start_button_size[1]/2)
        )
    extern.interface_resource.screen.blit(
        extern.interface_resource.start_button_help,
        ((mainwindow_size[0]-start_button_size[0])/2,
        mainwindow_size[1]*3/4-start_button_size[1]/2+start_button_size[1]*1.5)
        )
    extern.interface_resource.screen.blit(
        extern.interface_resource.start_button_custom,
        ((mainwindow_size[0]-start_button_size[0])/2,
        mainwindow_size[1]*3/4-start_button_size[1]/2+start_button_size[1]*3)
    )

def help_blit():
    extern.interface_resource.screen.blit(
        extern.interface_resource.help_text,
        ((mainwindow_size[0]-help_text_size[0])/2,
        mainwindow_size[1]/2-help_text_size[1]/2)
    )


def mouseclick_respond(event):
    if(event.type==MOUSEBUTTONDOWN):
        if(event.button==1):
            if((abs(event.pos[0]-mainwindow_size[0]/2)<start_button_size[0]/2) \
            & (abs(event.pos[1]-3/4*mainwindow_size[1]+start_button_size[1]*3)<start_button_size[1]/2)& (extern.game_state == GAMEINIT)):
                extern.game_state=GAMELOAD
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

    if pygame.key.get_pressed()[K_ESCAPE]:
        pygame.quit()
        sys.exit()