#
#   游戏类文件
#

from Define import *
import Extern as Et
import Resource as Rs

import pygame
from pygame.locals import *
import time

class SingleGame():
    def __init__(self):
        self.player = None  #人物对象
        self.enemy_list = []    #敌人列表
        self.skill_list = []    #技能列表
        self.obstacle_list = [] #障碍物列表
        self.load()

#   资源加载函数
    def load(self):
        pass

