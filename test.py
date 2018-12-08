#
#   游戏主函数
#

from define import *

import extern

import pygame

import main
import start
import Game

from pygame.locals import *
import sys
import time

#   pygame初始化
pygame.init()
#   开始画面初始化
start.startinit()
#   隐藏鼠标
pygame.mouse.set_visible(False)

#   主循环
while True:
        temptime=time.time()
        if (temptime-extern.last_fresh_time >1/fps):
                extern.last_fresh_time=temptime
                for event in pygame.event.get():
                        if event.type==QUIT:
                                pygame.quit()
                                sys.exit()

                if(extern.game_state==GAMEINIT):
                #   开始画面贴图
                        start.start_blit()
                #   光标绘制
                        start.cursorshow()
                #   鼠标动作响应
                        start.mouseclick_respond(event)
                        
                elif(extern.game_state==GAMEINIT1):
                #   开始画面贴图
                        start.start_blit()
                #   光标绘制
                        start.cursorshow()
                #   鼠标动作响应
                        start.mouseclick_respond(event)
                        
                elif(extern.game_state==GAMEHELP):
                #帮助画面贴图
                        start.start_blit()
                #   光标绘制
                        start.cursorshow()
                #   鼠标动作响应
                        start.mouseclick_respond(event)
                        
                elif(extern.game_state==GAMEHELP2):
                #帮助画面贴图
                        start.start_blit()
                        start.help_blit()
                #   光标绘制
                        start.cursorshow()
                #   鼠标动作响应
                        start.mouseclick_respond(event)
                elif(extern.game_state==GAMESINGLECHOOSE):
                #单人游戏选择画面贴图
                        start.single_play_blit()
                        start.cursorshow()
                        start.mouseclick_respond(event)
                        
                elif(extern.game_state==GAMELOAD): 
                        extern.singleplayergame=Game.Single_player_game()
                        extern.game_state=GAMESTART
                        
                elif(extern.game_state==GAMESTART):
                #   游戏循环
                        main.mainloop()

                pygame.display.update()
