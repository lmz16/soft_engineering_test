#
#   游戏成分类文件
#

from Define import *
import Extern as Et
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
        self.movable = [True, True, True, True]     # 上下左右
        self.can_move = True
        self.signal = None                          # 接受到的信号
        self.target= [0, 0]                         # 目标的坐标
        self.attack_range = 100                     # 攻击范围
        self.skill_time = []                        # 技能上一次发出的时间
        self.skill_cd = []                          # 技能冷却时间
        self.skill_direction = []                   # 技能方向
        self.freezetime = 0                         # 被攻击冻结时间
        self.origin_site = []                       # 出生位置，用于巡逻
        self.direction = random.randint(0,3)        # 决定巡逻方向 上下or左右
        if self.direction == 0:
            self.patrol_towards = MOVELEFT          
        if self.direction == 1:
            self.patrol_towards = MOVERIGHT
        if self.direction == 2:
            self.patrol_towards = MOVEUP
        if self.direction == 3:
            self.patrol_towards = MOVEDOWN
        self.load()                                 # 初始化与显示有关的信息
        self.velocity = Et.R_em.velocity
        self.movex = [self.velocity[0]*x for x in movex]
        self.movey = [self.velocity[1]*y for y in movey]
    
    def load(self):
        self.info.size = Et.R_em.size
        self.size = self.info.size
        self.info.max_life = Et.R_em.max_life
        self.info.life_value = Et.R_em.max_life
        self.info.state = ENEMYPATROL
        self.info.count = 0
        self.info.pic_direction = RIGHT

    # Enemy的攻击判定函数 根据攻击范围和玩家方位进行判定
    def enemy_attack_judge(self):
        judge = False
        if self.target[0] - self.info.site[0] < self.attack_range and self.target[1] == self.info.site[1]:
            judge = True
            self.skill_direction = MOVELEFT
        if self.info.site[0] - self.target[0] < self.attack_range and self.target[1] == self.info.site[1]:
            judge = True
            self.skill_direction = MOVERIGHT
        if self.target[1] - self.info.site[1] < self.attack_range and self.target[0] == self.info.site[0]:
            judge = True
            self.skill_direction = MOVEUP
        if self.info.site[1] - self.target[1] < self.attack_range and self.target[0] == self.info.site[0]:
            judge = True
            self.skill_direction = MOVEDOWN
        return judge

    def judge_direction(self):
        if self.movable[0] == False and self.direction == 2:
            self.direction = 3
        if self.movable[1] == False and self.direction == 3:
            self.direction = 2
        if self.movable[2] == False and self.direction == 0:
            self.direction = 1
        if self.movable[3] == False and self.direction == 1:
            self.direction = 0
        if self.movable == [False, False, False, False]:
            self.can_move = False
        if self.direction == 0:
            self.info.pic_direction = LEFT
        elif self.direction == 1:
            self.pic_direction = RIGHT

    
    # Enemy的巡逻函数 沿某一方向来回移动
    def patrol(self):    
        self.judge_direction()   
        if self.can_move:
            if self.direction == 0 or self.direction == 1:  # 左右巡逻
                range = 50
                #print("下一步位置：", self.site[0]+self.movex[self.patrol_towards])
                #print("容忍范围：", self.origin_site[0] - range)
                if self.info.site[0]+self.movex[self.patrol_towards] < self.origin_site[0] - range: 
                    self.patrol_towards = MOVERIGHT
                if self.info.site[0]+self.movex[self.patrol_towards] > self.origin_site[0] + range: 
                    self.patrol_towards = MOVELEFT
                self.info.site[0]=self.info.site[0]+self.movex[self.patrol_towards]
                if self.info.site[0]>Et.R_sg.size[0]-int(self.size[0]/2):
                    self.info.site[0]=Et.R_sg.size[0]-int(self.size[0]/2)
                    self.patrol_towards = MOVELEFT
                if self.info.site[0]<int(self.size[0]/2):
                    self.info.site[0]=int(self.size[0]/2)
                    self.patrol_towards = MOVERIGHT
            else:
                range = 40
                if self.info.site[1]+self.movey[self.patrol_towards] < self.origin_site[1] - range: 
                    self.patrol_towards = MOVEDOWN
                if self.info.site[1]+self.movey[self.patrol_towards] > self.origin_site[1] + range: 
                    self.patrol_towards = MOVEUP
                self.info.site[1]=self.info.site[1]+self.movey[self.patrol_towards]
                if self.info.site[1]>Et.R_sg.size[1]-int(self.size[1]/2):
                    self.info.site[1]=Et.R_sg.size[1]-int(self.size[1]/2)
                    self.patrol_towards = MOVEUP
                if self.info.site[1]<int(self.size[1]/2):
                    self.info.site[1]=int(self.size[1]/2)
                    self.patrol_towards = MOVEDOWN

    # Enemy进入战斗状态后的移动函数
    def move(self):
        self.move_direction()
        self.judge_direction()
        if self.can_move:
            self.info.site[0]=self.info.site[0]+self.movex[self.direction]
            if self.info.site[0]>Et.R_sg.size[0]-int(self.size[0]/2):
                self.info.site[0]=Et.R_sg.size[0]-int(self.size[0]/2)
            if self.info.site[0]<int(self.size[0]/2):
                self.info.site[0]=int(self.size[0]/2)
            if(abs(self.info.site[1] - self.target[1]) < self.velocity[0]):
                self.info.site[1]=self.target[1]
            else:
                self.info.site[1]=self.info.site[1]+self.movey[self.direction]
            if self.info.site[1]>Et.R_sg.size[1]-int(self.size[1]/2):
                self.info.site[1]=Et.R_sg.size[1]-int(self.size[1]/2)
            if self.info.site[1]<int(self.size[1]/2):
                self.info.site[1]=int(self.size[1]/2)

    def passiveMove(self,mv):
        temp = [self.info.site[0]+mv[0],self.info.site[1]+mv[1]]
        flag = False
        for ob in Et.Os_info:
            if abs(temp[0] - ob.site[0])<ob.size[0] and abs(temp[1] - ob.site[1])<ob.size[1]:
                flag = True
                break
        if not flag:
            self.info.site = temp


    # 针对move的移动方向判定
    def move_direction(self):
        self.direction = MOVELEFT
        if(self.target[0] == self.info.site[0]) and (self.target[1] < self.info.site[1]):
            self.direction = MOVEUP
        elif(self.target[0] == self.info.site[0]) and (self.target[1] > self.info.site[1]):
            self.direction = MOVEDOWN
        elif(self.target[0] > self.info.site[0]) and (self.target[1] == self.info.site[1]):
            self.direction = MOVERIGHT
        elif(self.target[0] < self.info.site[0]) and (self.target[1] == self.info.site[1]):
            self.direction = MOVELEFT
        elif(self.target[0] > self.info.site[0]) and (self.target[1] > self.info.site[1]):
            self.direction = MOVEDOWNRIGHT
        elif(self.target[0] > self.info.site[0]) and (self.target[1] < self.info.site[1]):
            self.direction = MOVEUPRIGHT
        elif(self.target[0] < self.info.site[0]) and (self.target[1] > self.info.site[1]):
            self.direction = MOVEDOWNLEFT
        elif(self.target[0] < self.info.site[0]) and (self.target[1] < self.info.site[1]):
            self.direction = MOVEUPLEFT

    # 敌人类的状态更新
    def update(self):
        self.target=self.game.player.info.site
        if self.info.life_value<0:
            self.info.state=ENEMYDEAD
        if self.info.state==ENEMYSTATIC:
            if self.enemy_attack_judge():
                self.info.state = ENEMYATTACK
                self.info.count = 0
        elif self.info.state == ENEMYPATROL:
            self.patrol()
            if self.signal == ATTACKED:
                self.info.state = ENEMYATTACKED
                self.info.count = 0
            elif abs(self.info.site[0] - self.target[0])+abs(self.info.site[1] - self.target[1]) < 500:
                self.info.state = ENEMYMOVE
        elif self.info.state==ENEMYMOVE:
            self.move()
            if self.signal == ATTACKED:
                self.info.state=ENEMYATTACKED 
                self.info.count=0
            elif self.enemy_attack_judge():
                self.info.state = ENEMYATTACK
                self.info.count = 0
                pass
        elif self.info.state==ENEMYATTACKED: 
            if self.info.count==10:
                self.info.state=ENEMYMOVE
            else:
                self.info.count=self.info.count+1
            if self.signal == ATTACKED:
                self.info.count=0
        elif self.info.state==ENEMYATTACK:
            pass
        #     if ((Et.last_fresh_time-self.skill1time)>self.skill1_cd):
        #         if self.info.count==4:
        #             tempskill=Skill()
        #             tempskill.game=self.game
        #             tempskill.resource=Et.skill_resource
        #             tempskill.initsite=self.info.site[:]
        #             tempskill.inittime=Et.last_fresh_time
        #             tempskill.caster=self
        #             tempskill.direction=self.skill_direction
        #             tempskill.site=self.info.site[:]
        #             tempskill.size=Et.skill_resource.size
        #             tempskill.damage=extern.skill_resource.damage
        #             self.game.skill_list.append(tempskill)
        #         elif self.info.count==10:
        #             self.info.count=0
        #             self.info.state=ENEMYMOVE
        #             self.skill1time=Et.last_fresh_time-10/fps
        #         else:
        #         self.info.count=self.info.count+1
        #     else:
        #     if self.signal==ATTACKED:
        #         self.info.state=ENEMYATTACKED
        #         self.info.count=0
        #     elif self.info.life_value<0:
        #         self.info.state=ENEMYDEAD
        #         self.info.count=0
        #     elif self.enemy_attack_judge == False:
        #         self.info.state = ENEMYMOVE
        #         self.info.count = 0


class ObstacleInfo():
    def __init__(self):
        self.site = [0, 0]
        self.size = [0, 0]
        self.kind = 0

class Obstacle():
    def __init__(self, oinfo):
        self.info = oinfo
        self.load()

    # 障碍物类的初始化函数
    def load(self):
        pass



