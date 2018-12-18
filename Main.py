#
#	游戏入口
#

from Define import *
import Extern as Et
import MainFunc as MF
import Interface as IF

import pygame
from pygame.locals import *

import os
import time

MF.init()	#pygame初始化

#	主循环
while True:
#	退出机制
    for event in pygame.event.get():
        MF.gameQuit(event)

#   时间刷新
    if MF.timeUpdate():
        IF.update(event)
        MF.gameStateManager()

        pygame.display.update()	#更新显示