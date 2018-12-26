#
#   游戏成分类文件
#

from Define import *
import Extern as Et
import math
import Skill
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
        self.skill_time = 0                        # 技能上一次发出的时间
        self.skill_cd = 1                          # 技能冷却时间
        self.skill_direction = []                   # 技能方向
        self.freezetime = 0                         # 被攻击冻结时间
        self.origin_site = []                       # 出生位置，用于巡逻
        self.direction = [0,0,0,0]                  # 上下左右
        self.patrol_direction = [0,0,0,0]
        m=random.randint(0,3)
        self.patrol_direction[m] = 1
        self.count = 0
        self.load()                                 # 初始化与显示有关的信息
        self.velocity = [1,1] #Et.R_em.velocity
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
        if self.count < 30:
            if self.patrol_direction[0] == 1 and self.movable[0] == True:
                self.info.site[1] = self.info.site[1] + self.velocity[1]
            if self.patrol_direction[1] == 1 and self.movable[1] == True:
                self.info.site[1] = self.info.site[1] - self.velocity[1]
            if self.patrol_direction[2] == 1 and self.movable[2] == True:
                self.info.site[0] = self.info.site[0] - self.velocity[0]
            if self.patrol_direction[3] == 1 and self.movable[3] == True:
                self.info.site[0] = self.info.site[0] + self.velocity[0]  
            self.count = self.count + 1
        if self.count == 30:
            if self.patrol_direction[0] == 1:
                self.patrol_direction[0] = 0 
                self.patrol_direction[1] = 1
            elif self.patrol_direction[1] == 1:
                self.patrol_direction[0] = 1 
                self.patrol_direction[1] = 0
            elif self.patrol_direction[2] == 1:
                self.patrol_direction[2] = 0 
                self.patrol_direction[3] = 1
            elif self.patrol_direction[3] == 1:
                self.patrol_direction[2] = 1 
                self.patrol_direction[3] = 0
            self.count = self.count + 1
        if self.count > 30:
            if self.patrol_direction[0] == 1 and self.movable[0] == True:
                self.info.site[1] = self.info.site[1] + self.velocity[1]
            if self.patrol_direction[1] == 1 and self.movable[1] == True:
                self.info.site[1] = self.info.site[1] - self.velocity[1]
            if self.patrol_direction[2] == 1 and self.movable[2] == True:
                self.info.site[0] = self.info.site[0] - self.velocity[0]
            if self.patrol_direction[3] == 1 and self.movable[3] == True:
                self.info.site[0] = self.info.site[0] + self.velocity[0]  
            self.count = self.count + 1
        if self.count == 60:
            self.count = 0
        if self.info.site[0] > (Et.R_sg.size[0] - int(self.info.size[0] / 2)):
            self.info.site[0] = Et.R_sg.size[0] - int(self.info.size[0] / 2)
        if self.info.site[0] < int(self.info.size[0] / 2):
            self.info.site[0] = int(self.info.size[0] / 2)
        if self.info.site[1] > (Et.R_sg.size[1] - int(self.info.size[1] / 2)):
            self.info.site[1] = Et.R_sg.size[1] - int(self.info.size[1] / 2)
        if self.info.site[1] < int(self.info.size[1] / 2):
            self.info.site[1] = int(self.info.size[1] / 2)
        if self.patrol_direction[2] == 1:
            self.info.pic_direction = RIGHT
        elif self.patrol_direction[3] == 1:
            self.info.pic_direction = LEFT

    # Enemy进入战斗状态后的移动函数
    def move(self):
        # self.move_direction()
        # self.judge_direction()
        self.direction = [0,0,0,0]
        if self.target[0] > self.info.site[0]:
            self.direction[3] = 1
        if self.target[0] < self.info.site[0]:
            self.direction[2] = 1
        if self.target[1] > self.info.site[1]:
            self.direction[0] = 1
        if self.target[1] < self.info.site[1]:
            self.direction[1] = 1
        if self.direction[0] == 1 and self.movable[0] == True:
            self.info.site[1] = self.info.site[1] + self.velocity[1]
        if self.direction[1] == 1 and self.movable[1] == True:
            self.info.site[1] = self.info.site[1] - self.velocity[1]
        if self.direction[2] == 1 and self.movable[2] == True:
            self.info.site[0] = self.info.site[0] - self.velocity[0]
        if self.direction[3] == 1 and self.movable[3] == True:
            self.info.site[0] = self.info.site[0] + self.velocity[0]
        if self.direction[2] == 1:
            self.info.pic_direction = RIGHT
        elif self.direction[3] == 1:
            self.info.pic_direction = LEFT


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
        #print(self.signal)
        #print(self.info.state)
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
            self.info.count = (self.info.count + 1) % 12 
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
            if ((Et.fresh_time-self.skill_time)>self.skill_cd):
                if self.info.count==4:
                    tempinfo = Skill.SkillInfo()
                    Et.Sk_info.append(tempinfo)
                    new_skill=Skill.SkillBallStraight(tempinfo)
                    new_skill.influence_list.append(self.game.player)
                    new_skill.resource=Et.R_sk[0]
                    new_skill.game=self.game
                    new_skill.init_site=self.info.site[:]
                    new_skill.init_time=Et.fresh_time
                    new_skill.caster=self
                    new_skill.direction=self.skill_direction
                    new_skill.info.site=self.info.site[:]
                    new_skill.info.size=new_skill.resource.size
                    new_skill.damage=new_skill.resource.damage
                    new_skill.duration=new_skill.resource.duration
                    self.game.skill_list.append(new_skill)
                    self.info.count = self.info.count + 1
                elif self.info.count==10:
                    self.info.count=0
                    self.info.state=ENEMYMOVE
                    self.skill_time=Et.fresh_time-10/fps
                else:
                    self.info.count=self.info.count+1
            else:
                if self.signal==ATTACKED:
                    self.info.state=ENEMYATTACKED
                    self.info.count=0
                elif self.info.life_value<0:
                    self.info.state=ENEMYDEAD
                    self.info.count=0
                elif self.enemy_attack_judge == False:
                    self.info.state = ENEMYMOVE
                    self.info.count = 0


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

