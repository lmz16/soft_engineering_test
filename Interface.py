#
#   界面显示模块
#

import pygame
from pygame.locals import *

from Define import *
import Extern as Et
import Input as Ip
import Resource as Rs

button_site = {
    "single":(480,400)
}

game_file = [
    "Resource/json/game_choose",
    ["Resource/json/game1",]
]

def update(event):
    if Et.game_state == GAMEINIT:
        Et.R_if.screen.blit(Et.R_if.main_bk_pic,(0,0))
        mouseResponse1(event)
        buttonshow()
        cursorShow()
    elif Et.game_state == GAMEINIT1:
        cursorShow()
        Et.R_gc = Rs.RChoose(game_file[0])
        Et.game_state = GAMESINGLECHOOSE
    elif Et.game_state == GAMESINGLECHOOSE:
        Et.R_if.screen.blit(Et.R_gc.bottom_pic,(0,0))
        cursorShow()
        Et.game_state = GAMELOADSUB
    elif Et.game_state == GAMELOADSUB:
        Et.R_sg = Rs.RSingle(game_file[1][Et.game_choice])
        Et.game_state = GAMELOAD
    elif Et.game_state == GAMELOAD:
        Et.game_state = GAMESTART
    elif Et.game_state == GAMESTART:
        gameBlit()


def cursorShow():
    [x,y]=pygame.mouse.get_pos()
    centerBlit(Et.R_if.screen,Et.R_if.cursor_pic,[x,y])

def mouseResponse1(event):
    if Ip.regionMonitor(event,button_site["single"],start_button_size):
        Et.game_state = GAMEINIT1

def buttonshow():
    centerBlit(Et.R_if.screen,Et.R_if.start_single_pic,button_site["single"])


def centerBlit(surface,pic,center):
    dx = int(pic.get_width()/2)
    dy = int(pic.get_height()/2)
    surface.blit(pic,[center[0] - dx,center[1] - dy])

def gameBlit():
    Et.R_sg.bg_pic_temp = Et.R_sg.bg_pic.copy()
    for enemy in Et.Em_info:
        centerBlit(Et.R_sg.bg_pic_temp,Et.R_em.pic_static[0],enemy.site)
    centerBlit(Et.R_sg.bg_pic_temp, Et.R_pl.pic_static[0], Et.Pr_info[0].site)
    Et.R_if.screen.blit(Et.R_sg.bg_pic_temp, (0, 0))