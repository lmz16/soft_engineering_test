#
#   游戏成分类文件
#

from Define import *
import Extern as Et
import pygame
from pygame.locals import *
import math
import random

class EnemyInfo():
    def __init__(self):
        self.site = [0,0]
        self.max_life = 0
        self.life_value = 0
        self.state = PLAYERSTATIC
        self.pic_direction = RIGHT
        self.size = [0,0]
        self.count = 0

class Enemy():
    def __init__(self, einfo, game):
        self.info = einfo
        self.velocity = []
        self.game = game
        self.movable = [True,True,True,True]
        self.signal = None                          # 接受到的信号
        self.target= [0, 0]                         # 目标的坐标
        self.attack_range = 100                     # 攻击范围
        self.skill_time = []                        # 技能上一次发出的时间
        self.skill_cd = []                          # 技能冷却时间
        self.skill_direction = []                   # 技能方向
        self.freezetime = 0                         # 被攻击冻结时间
        self.origin_site = []                       # 出生位置，用于巡逻
        self.patrol_direction = random.randint(0,3) # 决定巡逻方向 上下or左右
        if self.patrol_direction == 0:
            self.patrol_towards = MOVELEFT
        if self.patrol_direction == 1:
            self.patrol_towards = MOVERIGHT
        if self.patrol_direction == 2:
            self.patrol_towards = MOVEUP
        if self.patrol_direction == 3:
            self.patrol_towards = MOVEDOWN