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

class SingleGame():
    def __init__(self):
        self.player = None  #人物对象
        self.enemy_list = []    #敌人列表
        self.skill_list = []    #技能列表
        self.obstacle_list = Et.Os_info #障碍物列表
        self.load()

#   资源加载函数
    def load(self):
        self.playerLoad()
        self.enemyLoad()
        self.obstacleLoad()

    def playerLoad(self):
        Et.Pr_info[0] = Pl.PlayerInfo()
        Et.Pr_info[0].max_life = Et.R_pl.max_life
        Et.Pr_info[0].life_value = Et.R_pl.max_life
        self.player = Pl.Player(Et.Pr_info[0])
        self.player.velocity = Et.R_pl.velocity

    def enemyLoad(self):
        for enemy in Et.R_sg.enemy_list:
            temp = It.EnemyInfo()
            temp.site = enemy["site"]
            Et.Em_info.append(
                temp
            )
            tempe = It.Enemy(temp,self)
            tempe.origin_site = enemy["site"]
            self.enemy_list.append(
                tempe
            )

    def moveJudge(self):
        for enemy in self.enemy_list:
            enemy.movable = [True,True,True,True]   #上下左右
            for obstacle in self.obstacle_list:
                pass

    def obstacleLoad(self):
        for ob in Et.R_sg.obstacle_list:
            temp = It.ObstacleInfo()
            temp.site = ob["site"]
            temp.size = ob["size"]
            temp.kind = ob["kind"]
            Et.Os_info.append(temp)

    def update(self):
        for enemy in self.enemy_list:
            enemy.update()
        self.player.update()

def jugde(t1,t2):
    pass