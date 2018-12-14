#
#   游戏成分类
#

from define import *
import extern
import pygame
import Game
import math
from pygame.locals import *

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
        self.ignore_skill=[]
        self.count = "計數器"
        self.attack_range=100
        self.skill1time='技能一上次发动的时间'
        self.skill1_cd='技能一冷却时间'
        self.skill_direction=0
        self.freezetime='被攻击冻结时间'
        self.load()

    def move(self):
        self.move_direction()
        if self.movable:
            self.site[0]=self.site[0]+self.movex[self.direction]
            if self.site[0]>extern.singleplayergame_resource.size[0]-int(self.size[0]/2):
                self.site[0]=extern.singleplayergame_resource.size[0]-int(self.size[0]/2)
            if self.site[0]<int(self.size[0]/2):
                self.site[0]=int(self.size[0]/2)
            if(abs(self.site[1] - self.target[1]) < self.velocity):
                self.site[1]=self.target[1]
            else:
                self.site[1]=self.site[1]+self.movey[self.direction]
            if self.site[1]>extern.singleplayergame_resource.size[1]-int(self.size[1]/2):
                self.site[1]=extern.singleplayergame_resource.size[1]-int(self.size[1]/2)
            if self.site[1]<int(self.size[1]/2):
                self.site[1]=int(self.size[1]/2)

    def patrol(self):        # AI巡逻
        pass

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
            if self.enemy_attack_judge():
                #self.state = ENEMYATTACK
                self.count = 0
            self.enemy_update_blit(0)
        elif self.state==ENEMYMOVE:
            self.move()
            self.enemy_update_blit(0)
            if self.signal == ATTACKED:
                self.state=ENEMYATTACKED 
                self.count=0
            elif self.enemy_attack_judge():
                self.state = ENEMYATTACK
                self.count = 0
                pass
        elif self.state==ENEMYATTACKED: 
            if self.count==10:
                self.state=ENEMYMOVE
            else:
                self.count=self.count+1
            if self.signal == ATTACKED:
                self.count=0
            self.enemy_update_blit(0)
        elif self.state==ENEMYATTACK:
            if ((extern.last_fresh_time-self.skill1time)>self.skill1_cd):
                if self.count==4:
                    tempskill=Skill()
                    tempskill.game=self.game
                    tempskill.resource=extern.skill_resource
                    tempskill.initsite=self.site[:]
                    tempskill.inittime=extern.last_fresh_time
                    tempskill.caster=self
                    tempskill.direction=self.skill_direction
                    tempskill.site=self.site[:]
                    tempskill.size=extern.skill_resource.size
                    tempskill.damage=extern.skill_resource.damage
                    self.game.skill_list.append(tempskill)
                    self.enemy_update_blit(0)
                elif self.count==10:
                    self.count=0
                    self.state=ENEMYMOVE
                    self.skill1time=extern.last_fresh_time-10/fps
                    self.enemy_update_blit(0)
                else:
                    self.enemy_update_blit(0)
                self.count=self.count+1
            else:
                self.enemy_update_blit(0)
            if self.signal==ATTACKED:
                self.state=ENEMYATTACKED
                self.count=0
            elif self.life_value<0:
                self.state=ENEMYDEAD
                self.count=0
            elif self.enemy_attack_judge == False:
                self.state = ENEMYMOVE
                self.count = 0

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

    def enemy_attack_judge(self):
        judge = False
        if self.target[0] - self.site[0] < self.attack_range and self.target[1] == self.site[1]:
            judge = True
            self.skill_direction = MOVELEFT
        if self.site[0] - self.target[0] < self.attack_range and self.target[1] == self.site[1]:
            judge = True
            self.skill_direction = MOVERIGHT
        if self.target[1] - self.site[1] < self.attack_range and self.target[0] == self.site[0]:
            judge = True
            self.skill_direction = MOVEUP
        if self.site[1] - self.target[1] < self.attack_range and self.target[0] == self.site[0]:
            judge = True
            self.skill_direction = MOVEDOWN
        return judge


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
        self.resource='资源指针'
        self.load()

    # 技能类的状态更新
    def update(self):
        if extern.last_fresh_time-self.inittime>self.duration:
            self.delflag=True
        else:
            if self.resource.kind == 1:
                self.skill_move()
            elif self.resource.kind == 2:
                self.skill_move2()
            elif self.resource.kind == 3:
                self.skill_move3()
            self.item_blit()

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
    
    def skill_move2(self):
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

    def skill_move3(self):
        dx=1.5*max(self.caster.size)*math.cos(2*math.pi*(extern.last_fresh_time-self.inittime))
        dy=1.5*max(self.caster.size)*math.sin(2*math.pi*(extern.last_fresh_time-self.inittime))
        self.site=[
            self.caster.site[0]+int(dx),
            self.caster.site[1]+int(dy)]

    def load(self):
        self.delflag=0
        self.duration=extern.skill_resource.duration
        self.velocity=extern.skill_resource.velocity
        self.movex=[self.velocity*x for x in movex]
        self.movey=[self.velocity*y for y in movey]
        self.size=extern.skill_resource.size
        self.last=extern.skill_resource.last

    def item_blit(self):
        extern.singleplayergame_resource.pic_temp.blit(self.resource.pic1,
        (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))

    def attack_judge(self,target):
        return (
            (abs(self.site[0]-target.site[0])<(self.size[0]+target.size[0])/2) &
            (abs(self.site[1]-target.site[1])<(self.size[1]+target.size[1])/2)
        )


# 障碍物类
class Obstacle(Item):
    def __init__(self, ):
        super(Obstacle,self).__init__()
        self.life_value='生命值'
        self.signal='接收到的信号'
        self.load()

    # 障碍物类的状态更新
    def update(self):
        self.obstacle_blit()

    # 障碍物类的初始化函数
    def load(self):
        self.site = extern.obstacle_resource.site
        self.size = extern.obstacle_resource.size
        self.transparent = extern.obstacle_resource.transparent

    def obstacle_blit(self):
        if self.transparent:
            extern.singleplayergame_resource.pic_temp.blit(extern.obstacle_resource.pic_transparent,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        else:
            extern.singleplayergame_resource.pic_temp.blit(extern.obstacle_resource.pic_non_transparent,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
