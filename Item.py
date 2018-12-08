#
#   游戏成分类
#

from define import *
import extern
import pygame
import Game
import math
from pygame.locals import *
import random

# Item基类,作为敌人类,障碍物类等的父类
class Item():
    def __init__(self):
        self.site='物体位置'
        self.size='物体大小'
        self.movable='可否移动'
        self.direction='朝向'
        self.game='游戏指针'
        self.state='状态'
        self.count='状态计数器'

    def item_blit(self):
        pass

# 敌人类
class Enemy(Item):
    def __init__(self, game):
        super(Enemy,self).__init__()
        self.life_value='生命值'
        self.signal='接收到的信号'
        self.target='攻击目标的site'
        self.game=game
        self.speedx=2
        self.speedy=2
        self.ignore_skill=[]
        self.load()

    def move(self):
        self.move_direction()
        if self.movable:
            self.site[0]=self.site[0]+self.movex[self.direction]
            if self.site[0]>extern.singleplayergame_resource.size[0]-int(self.size[0]/2):
                self.site[0]=extern.singleplayergame_resource.size[0]-int(self.size[0]/2)
            if self.site[0]<int(self.size[0]/2):
                self.site[0]=int(self.size[0]/2)
            if(abs(self.site[1] - self.target[1]) < self.speedy):
                self.site[1]=self.target[1]
            else:
                self.site[1]=self.site[1]+self.movey[self.direction]
            if self.site[1]>extern.singleplayergame_resource.size[1]-int(self.size[1]/2):
                self.site[1]=extern.singleplayergame_resource.size[1]-int(self.size[1]/2)
            if self.site[1]<int(self.size[1]/2):
                self.site[1]=int(self.size[1]/2)

    def move_direction(self):
        self.direction = MOVELEFT
        if(self.target[0] == self.site[0] and self.target[1] < self.site[1]):
            self.direction = MOVEUP
        elif(self.target[0] == self.site[0] and self.target[1] > self.site[1]):
            self.direction = MOVEDOWN
        elif(self.target[0] > self.site[0] and self.target[1] == self.site[1]):
            self.direction = MOVERIGHT
        elif(self.target[0] < self.site[0] and self.target[1] == self.site[1]):
            self.direction = MOVELEFT
        elif(self.target[0] > self.site[0] and self.target[1] > self.site[1]):
            self.direction = MOVEDOWNRIGHT
        elif(self.target[0] > self.site[0] and self.target[1] < self.site[1]):
            self.direction = MOVEUPRIGHT
        elif(self.target[0] < self.site[0] and self.target[1] > self.site[1]):
            self.direction = MOVEDOWNLEFT
        elif(self.target[0] < self.site[0] and self.target[1] < self.site[1]):
            self.direction = MOVEUPLEFT

# 敌人类的状态更新
    def update(self):
        self.target=self.game.single_player.site
        if self.life_value<0:
            self.state=ENEMYDEAD
        if self.state==ENEMYSTATIC:
            self.enemy_update_blit(0)
        elif self.state==ENEMYMOVE:
            self.move()
            self.enemy_update_blit(0)
            if self.signal == None:
                pass
            elif self.signal == ATTACKED:
                self.state=ENEMYATTACKED 
                self.count=0
        elif self.state==ENEMYATTACKED: 
            if self.count==10:
                self.state=ENEMYMOVE
            else:
                self.count=self.count+1
            if self.signal == ATTACKED:
                self.count=0
            self.enemy_update_blit(0)

# 敌人类的初始化函数
    def load(self):
        self.size=extern.enemy_resource.size
        self.state=ENEMYMOVE
        self.movable=True
        self.velocity=extern.enemy_resource.velocity
        self.movex=[self.velocity*x for x in movex]
        self.movey=[self.velocity*y for y in movey]
        self.count=0

# 敌人的贴图函数
    def enemy_update_blit(self,n):
        if n==0:
            extern.singleplayergame_resource.pic_temp.blit(extern.enemy_resource.pic_static,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==1:
            extern.singleplayergame_resource.pic_temp.blit(extern.enemy_resource.pic_move1,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==2:
            extern.singleplayergame_resource.pic_temp.blit(extern.enemy_resource.pic_move2,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==3:
            extern.singleplayergame_resource.pic_temp.blit(extern.enemy_resource.pic_attack1,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==4:
            extern.singleplayergame_resource.pic_temp.blit(extern.enemy_resource.pic_attack2,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==5:
            extern.singleplayergame_resource.pic_temp.blit(extern.enemy_resource.pic_attacked,
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
        self.initsite='初始化位置'
        self.signal='接收到的信号'
        self.caster='技能释放者'
        self.last='击中后是否消失'
        self.delflag='技能是否应该被删除'
        self.kind='技能类型'
        self.velocity='技能速度'
        self.load()

    # 技能类的状态更新
    def update(self):
        if extern.last_fresh_time-self.inittime>self.duration:
            self.delflag=True
        else:
            if self.kind == 1:
                self.skill_move_straight()
            elif self.kind ==2:
                self.skill_move_sinus()
            elif self.kind ==3:
                self.skill_move_quadratic()
            elif self.kind ==4:
                self.skill_move_random()
            elif self.kind ==5:
                self.skill_move_circle()
            self.item_blit()
            
    def check_boundary(self):
        if self.site[0]>(extern.singleplayergame_resource.size[0]-int(self.size[0]/2)):
            self.delflag=True
        if self.site[0]<int(self.size[0]/2):
            self.delflag=True
        if self.site[1]>(extern.singleplayergame_resource.size[1]-int(self.size[1]/2)):
            self.delflag=True
        if self.site[1]<int(self.size[1]/2):
            self.delflag=True

    def skill_move(self):
        self.site[0]=self.site[0]+self.movex[self.direction]
        if self.site[0]>(extern.singleplayergame_resource.size[0]-int(self.size[0]/2)):
            self.delflag=True
        if self.site[0]<int(self.size[0]/2):
            self.delflag=True
        self.site[1]=self.site[1]+self.movey[self.direction]
        if self.site[1]>(extern.singleplayergame_resource.size[1]-int(self.size[1]/2)):
            self.delflag=True
        if self.site[1]<int(self.size[1]/2):
            self.delflag=True
    
    def skill_move_straight(self):
        dx=10*self.velocity*(extern.last_fresh_time-self.inittime)
        transmat=[
            [0,1,-1,0],[0,-1,1,0],[-1,0,0,-1],[1,0,0,1],
            [-1,1,-1,-1],[1,1,-1,1],[-1,-1,1,-1],[1,-1,1,1]
        ]
        self.site=[
            self.initsite[0]+int(dx*transmat[self.direction][0]),
            self.initsite[1]+int(dx*transmat[self.direction][2])
        ]
        self.check_boundary()
    
    def skill_move_sinus(self):
        sinmovex=10*self.velocity*(extern.last_fresh_time-self.inittime)
        sinmovey=50*math.sin(2*math.pi*(extern.last_fresh_time-self.inittime))
        transmat=[
            [0,1,-1,0],[0,-1,1,0],[-1,0,0,-1],[1,0,0,1],
            [-1,1,-1,-1],[1,1,-1,1],[-1,-1,1,-1],[1,-1,1,1]
        ]
        self.site=[
            self.initsite[0]+int(sinmovex*transmat[self.direction][0]+sinmovey*transmat[self.direction][1]),
            self.initsite[1]+int(sinmovex*transmat[self.direction][2]+sinmovey*transmat[self.direction][3])
        ]
        self.check_boundary()
    
    def skill_move_quadratic(self):
        dx=10*self.velocity*(extern.last_fresh_time-self.inittime)
        dy=0.5*dx*dx
        transmat=[
            [0,1,-1,0],[0,-1,1,0],[-1,0,0,-1],[1,0,0,1],
            [-1,1,-1,-1],[1,1,-1,1],[-1,-1,1,-1],[1,-1,1,1]
        ]
        self.site=[
            self.initsite[0]+int(dx*transmat[self.direction][0]+dy*transmat[self.direction][1]),
            self.initsite[1]+int(dx*transmat[self.direction][2]+dy*transmat[self.direction][3])
        ]
        self.check_boundary()
    
    def skill_move_random(self):
        dx=random.random()*10*self.velocity
        dy=random.random()*10*self.velocity
        self.site=self.site+[int(dx),int(dy)]
        self.check_boundary()
    
    def skill_move_circle(self):
        dx=10*math.cos(2*math.pi*(extern.last_fresh_time-self.inittime))
        dy=10*math.sin(2*math.pi*(extern.last_fresh_time-self.inittime))
        self.site=self.initsite+[int(dx),int(dy)]
        self.check_boundary()

    def load(self):
        self.delflag=0
        self.duration=extern.skill_resource.duration
        self.velocity=extern.skill_resource.velocity
        self.movex=[self.velocity*x for x in movex]
        self.movey=[self.velocity*y for y in movey]
        self.size=extern.skill_resource.size
        self.last=extern.skill_resource.last

    def item_blit(self):
        extern.singleplayergame_resource.pic_temp.blit(extern.skill_resource.pic1,
        (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))

    def attack_judge(self,target):
        return (
            (abs(self.site[0]-target.site[0])<(self.size[0]+target.size[0])/2) &
            (abs(self.site[1]-target.site[1])<(self.size[1]+target.size[1])/2)
        )
