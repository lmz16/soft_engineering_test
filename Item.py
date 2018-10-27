#
#   游戏成分类
#

from define import *
import extern
import pygame
from pygame.locals import *

# Item基类,作为敌人类,障碍物类等的父类
class Item():
    def __init__(self):
        self.site='物体位置'
        self.size='物体大小'
        self.movable='可否移动'
        self.direction='朝向'
        self.life_value='生命值'

# 敌人类
class Enemy(Item):
    def __init__(self):
        super(Enemy,self).__init__(self)
        self.state='状态'

# 敌人类的状态更新
    def update(self):
        pass

# 敌人类的初始化函数
    def load(self):
        pass

# 障碍物类
class Obstacle(Item):
        def __init__(self):
            super(Obstacle,self).__init__(self)
            self.state='状态'

    # 障碍物类的状态更新
        def update(self):
            pass

    # 障碍物类的初始化函数
        def load(self):
            pass
