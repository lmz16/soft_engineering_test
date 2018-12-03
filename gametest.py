#
#   游戏主函数
#

from define import *

import extern

import pygame

import main
import start

import Game
import Player
import Item

from pygame.locals import *
from sys import exit

#   pygame初始化
pygame.init()
#   开始画面初始化
start.startinit()
#   隐藏鼠标
pygame.mouse.set_visible(False)

extern.game_state==GAMELOAD

#   主循环
while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            exit()

    if(extern.game_state==GAMELOAD):
#   单人游戏加载状态
        extern.main_game=Single_player_game()
        extern.game_state==GAMESINGLERUNNING
    elif(extern.game_state==GAMESINGLERUNNING):
#   游戏循环
        main.mainloop()

    pygame.display.update()
