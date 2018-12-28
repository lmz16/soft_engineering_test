#
#   游戏类文件
#

from Define import *
import Extern as Et
import Resource as Rs
import Player as Pl
import Item as It

import pygame
from pygame.locals import *
import time

character_file = [
    "Resource/json/character1",
]

enemy_file = [
    "Resource/json/enemy1",
]

obstacle_file = [
    "Resource/json/ob1",
]

skill_file = [
    "Resource/json/sk1"
]

class SingleGame():
    def __init__(self):
        self.player = None  #人物对象
        self.enemy_list = []    #敌人列表
        self.skill_list = []    #技能列表
        self.obstacle_list = [] #障碍物列表
        self.over = 0
        self.load()

#   资源加载函数
    def load(self):
        Et.Em_info = []
        Et.Sk_info = []
        self.playerLoad()
        self.enemyLoad()
        self.obstacleLoad()

    def playerLoad(self):
        Et.Pr_info[0] = Pl.PlayerInfo()
        Et.Pr_info[0].max_life = Et.R_pl.max_life
        Et.Pr_info[0].life_value = Et.R_pl.max_life
        self.player = Pl.Player(Et.Pr_info[0])
        self.player.velocity = Et.R_pl.velocity
        self.player.skill_type = Et.R_pl.skill
        self.player.info.size = Et.R_pl.size
        self.player.game = self

    def enemyLoad(self):
        for enemy in Et.R_sg.enemy_list:
            temp = It.EnemyInfo()
            temp.site = enemy["site"]
            Et.Em_info.append(
                temp
            )
            temp.kind = enemy["kind"]
            tempe = It.Enemy(temp,self)
            tempe.origin_site = enemy["site"]
            self.enemy_list.append(
                tempe
            )

    def moveJudge(self):
        for enemy in self.enemy_list:
            enemy.movable = [True] * 4
            self.player.movable = [True] * 4
        for obstacle in self.obstacle_list:
            for enemy in self.enemy_list:
                self.__collisionJudge(obstacle.info, enemy)
            self.__collisionJudge(obstacle.info, self.player)

    def __collisionJudge(self, obstacleInfo, obj):
        dxMin = (obj.info.size[0] + obstacleInfo.size[0]) / 2
        dyMin = (obj.info.size[1] + obstacleInfo.size[1]) / 2
        if ((abs(obj.info.site[0] - obstacleInfo.site[0]) < (dxMin + COLLISIONTHRESHOLD)) &
                (abs(obj.info.site[1] - obstacleInfo.site[1]) < (dyMin + COLLISIONTHRESHOLD))):
            obj.movable[3] &= ~(obj.info.site[0] < obstacleInfo.site[0] - dxMin)
            obj.movable[2] &= ~(obj.info.site[0] > obstacleInfo.site[0] + dxMin)
            obj.movable[1] &= ~(obj.info.site[1] < obstacleInfo.site[1] - dyMin)
            obj.movable[0] &= ~(obj.info.site[1] > obstacleInfo.site[1] + dyMin)

    def obstacleLoad(self):
        for ob in Et.R_sg.obstacle_list:
            temp = It.ObstacleInfo()
            temp.site = ob["site"]
            temp.size = ob["size"]
            temp.kind = ob["kind"]
            Et.Os_info.append(temp)
            self.obstacle_list.append(It.Obstacle(temp))

    def update(self):
        if self.over == 0:
            self.moveJudge()
            self.signalSend()
            for skill in self.skill_list:
                skill.update()
                skill.influence()
                self.deskill(skill)
            for enemy in self.enemy_list:
                enemy.update()
                enemy.signal = None
                self.deenemy(enemy)
            self.player.update()
            if len(self.enemy_list) == 0:
                self.over = 1
            if self.player.info.life_value < 0:
                self.over = 2

    def signalSend(self):
        self.playerSignal()

    def playerSignal(self):
        move_state = Et.I_ctr.p1_key["up"] << 3 | Et.I_ctr.p1_key["down"] << 2 | Et.I_ctr.p1_key["left"] << 1 | Et.I_ctr.p1_key["right"]
        move_switch = [None, 3, 2, None, 1, 7, 6, None, 0, 5, 4, None, None, None, None, None]
        self.player.signal = move_switch[move_state]
        if Et.I_ctr.p1_key["atk1"]:
            self.player.signal = SKILL1
        elif Et.I_ctr.p1_key["atk2"]:
            self.player.signal = SKILL2
        elif Et.I_ctr.p1_key["atk3"]:
            self.player.signal = SKILL3

    def deskill(self,s):
        if s.delflag:
            if s.info in Et.Sk_info:
                Et.Sk_info.remove(s.info)
            self.skill_list.remove(s)
            if s in self.player.skill_list[0]:
                self.player.skill_list[0].remove(s)
            if s in self.player.skill_list[1]:
                self.player.skill_list[1].remove(s)
            if s in self.player.skill_list[2]:
                self.player.skill_list[2].remove(s)
            del s

    def deenemy(self,e):
        if e.info.life_value < 0:
            if e.info in Et.Em_info:
                Et.Em_info.remove(e.info)
            self.enemy_list.remove(e)
            del e



        # 信号类
class Signal():
    def __init__(self,type,receiver):
        self.type=type
        self.receiver=receiver