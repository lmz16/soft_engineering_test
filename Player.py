#
#   人物类
#

from Define import *
import Extern as Et
import pygame
from pygame.locals import *

class PlayerInfo():
    def __init__(self):
        self.site = [200,400]
        self.max_life = 0
        self.life_value = 0
        self.state = PLAYERSTATIC
        self.pic_direction = RIGHT
        self.size = [0,0]
        self.count = 0
        self.visible = True

class Player():
    def __init__(self,pinfo):
        self.info = pinfo
        self.velocity = [0, 0]
        self.movable = [True,True,True,True]    #上下左右方向是否可移动
        self.game = None    #游戏指针
        self.skill_time = [0,0,0]   #技能123的上次发动时间
        self.skill_cd = [0,0,0] #技能123的冷却时间
        self.freeze_time = 0    #被攻击后僵直时间

