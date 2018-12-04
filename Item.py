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
    
    def item_blit(self):
        pass

# 敌人类
class Enemy(Item):
    def __init__(self):
        super(Enemy,self).__init__()
        self.life_value='生命值'
        self.signal='接收到的信号'
        self.speedx=10
        self.speedy=10
        self.load()

    def move(self):
        if self.movable:
            self.site[0]=self.site[0]+self.speedx
            if self.site[0]>extern.singleplayer_background_size[0]-int(self.size[0]/2):
                self.site[0]=extern.singleplayer_background_size[0]-int(self.size[0]/2)
            if self.site[0]<int(self.size[0]/2):
                self.site[0]=int(self.size[0]/2)
            self.site[1]=self.site[1]+self.speedy
            if self.site[1]>extern.singleplayer_background_size[1]-int(self.size[1]/2):
                self.site[1]=extern.singleplayer_background_size[1]-int(self.size[1]/2)
            if self.site[1]<int(self.size[1]/2):
                self.site[1]=int(self.size[1]/2)

# 敌人类的状态更新
    def update(self):
        if self.state==ENEMYSTATIC:
            self.enemy_update_blit(0)
    
        elif self.state==ENEMYMOVE:
            self.move()
            self.enemy_update_blit(0)

# 敌人类的初始化函数
    def load(self):
        self.size=extern.singleplayer_enemysize
        self.state=ENEMYMOVE
        self.movable=True

# 敌人的贴图函数
    def enemy_update_blit(self,n):
        if n==0:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_enemy_pic_static,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==1:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_player_pic_move1,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==2:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_player_pic_move2,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==3:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_player_pic_attack1,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))  
        elif n==4:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_player_pic_attack2,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2))) 
        elif n==5:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_player_pic_attacked,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))

# 障碍物类
class Obstacle(Item):
    def __init__(self):
        super(Obstacle,self).__init__()
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
        super(Skill,self).__init__()
        self.damage='伤害值'
        self.duration='技能持续时间'
        self.inittime='初始化时间'
        self.signal='接收到的信号'
        self.caster='技能释放者'
        self.last='击中后是否消失'
        self.load()

    # 技能类的状态更新
    def update(self):
        pass
