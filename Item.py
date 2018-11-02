#
#   游戏成分类
#

from define import *
import extern
import pygame
import Game
from pygame.locals import *

# Item基类,作为敌人类,障碍物类等的父类
class Item():
    def __init__(self):
        self.site='物体位置'
        self.size='物体大小'
        self.movable='可否移动'
        self.direction='朝向'
        self.game='当前游戏指针'
        self.state='状态'

# 敌人类
class Enemy(Item):
    def __init__(self):
        super(Enemy,self).__init__(self)
        self.life_value='生命值'
        self.signal='接收到的信号'
        self.load()

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
        self.life_value='生命值'
        self.signal='接收到的信号'
        self.load()

    # 障碍物类的状态更新
    def update(self):
        pass

    # 障碍物类的初始化函数
    def load(self):
        pass

# 技能类
class Skill(Item):
    def __init__(self):
        super(Skill,self).__init__(self)
        self.damage='伤害值'
        self.duration='技能持续时间'
        self.inittime='初始化时间'
        self.signal='接收到的信号'
        self.caster='技能释放者'
        self.load()

    # 技能类的状态更新
    def update(self):
            pass
