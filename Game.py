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

class SingleGame():
    def __init__(self):
        self.player = None  #人物对象
        self.enemy_list = []    #敌人列表
        self.skill_list = []    #技能列表
        self.obstacle_list = [] #障碍物列表
        self.load()

#   资源加载函数
    def load(self):
        self.playerLoad()
        self.enemyLoad()

    def playerLoad(self):
        Et.R_pl = Rs.RCharacter(character_file[Et.player_choice])
        Et.Pr_info[0] = Pl.PlayerInfo()
        Et.Pr_info[0]["max_life"] = Et.R_pl.max_life
        Et.Pr_info[0]["life_value"] = Et.R_pl.max_life
        self.player = Pl.Player(Et.Pr_info[0])

    def enemyLoad(self):
        Et.R_em = Rs.REnemy(enemy_file[Et.game_choice])
        for enemy in Et.R_sg.enemy_list:
            temp = It.EnemyInfo()
            temp.site = enemy["site"]
            Et.Em_info.append(
                temp
            )
            self.enemy_list.append(
                It.Enemy(temp,self)
            )

    def moveJudge(self):
        for enemy in self.enemy_list:
            for obstacle in self.obstacle_list:
                pass
