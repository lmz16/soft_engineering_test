#
#   游戏主函数
#

from define import *

import extern

import pygame

import main
import start

from pygame.locals import *
from sys import exit

#   pygame初始化
pygame.init()
#   开始画面初始化
start.startinit()
#   隐藏鼠标
pygame.mouse.set_visible(False)

#   主循环
while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    if(extern.game_state==GAMEINIT):
#   开始画面贴图
        start.start_blit()
#   光标绘制
        start.cursorshow()
#   鼠标动作响应
        start.mouseclick_respond(event)
    if(extern.game_state==GAMEINIT1):
#   开始画面贴图
        start.start_blit()
#   光标绘制
        start.cursorshow()
#   鼠标动作响应
        start.mouseclick_respond(event)
    elif(extern.game_state==GAMEHELP):
        start.start_blit()
#   光标绘制
        start.cursorshow()
#   鼠标动作响应
        start.mouseclick_respond(event)
    elif(extern.game_state==GAMEHELP2):
        start.start_blit()
        start.help_blit()
#   光标绘制
        start.cursorshow()
#   鼠标动作响应
        start.mouseclick_respond(event)
    elif(extern.game_state==GAMESTART):
#   游戏循环
        main.mainloop()

    pygame.display.update()
