#
#	Main文件的函数实现
#

import pygame
from pygame.locals import *
import os
import time 

import Extern as Et
import Resource as Rs
import Input as Ip
import Game as Gm
from Define import *

#   游戏程序初始化函数
def init():
    pygame.init()	#pygame初始化
    pygame.mouse.set_visible(False)	#隐藏鼠标
    Et.game_state = GAMEINIT #初始化游戏状态
    Et.R_if = Rs.RInterface("Resource/json/interface") #加载界面资源
    Et.I_ctr = Ip.Control()     #初始化键盘控制


#   游戏退出函数
def gameQuit(event):
    if event.type==QUIT:
        pygame.quit()
        os._exit(0)

#   时间更新函数
def timeUpdate():
    temptime = time.time()
    if (temptime - Et.fresh_time) > 1/fps:
        Et.fresh_time = temptime
        return True
    else:
        return False 

def gameStateManager():
    if Et.game_state == GAMEINIT:
        print("GAMEINIT")
    elif Et.game_state == GAMEINIT1:
        print("in GAMEINIT1")
    elif Et.game_state == GAMESINGLECHOOSE:
        print("in GAMESINGLECHOOSE")
    elif Et.game_state == GAMELOAD:
        print("in GAMELOAD")

        # Et.I_ctr.update()
        # for key,value in Et.I_ctr.p1_key.items():
        #         if value:
        #                 print(key)
        