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
        self.player.game = self

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
            enemy.movable = [True]*4
        self.player.movable = [True]*4
        for obstacle in self.obstacle_list:
            for enemy in self.enemy_list:
                dxMin = (enemy.info.size[0] + obstacle.size[0]) / 2
                dyMin = (enemy.info.size[1] + obstacle.size[1]) / 2
                atDown = ((enemy.info.site[1] > obstacle.site[1]) & (
                            enemy.info.site[1] < (obstacle.site[1] + dyMin + COLLISIONTHRESHOLD)))
                atUp = ((enemy.info.site[1] < obstacle.site[1]) & (
                            enemy.info.site[1] > (obstacle.site[1] - dyMin - COLLISIONTHRESHOLD)))
                atRight = ((enemy.info.site[0] > obstacle.site[0]) & (
                            enemy.info.site[0] < (obstacle.site[0] + dxMin + COLLISIONTHRESHOLD)))
                atLeft = ((enemy.info.site[0] < obstacle.site[0]) & (
                            enemy.info.site[0] > (obstacle.site[0] - dxMin - COLLISIONTHRESHOLD)))
                enemy.movable[0] = ((enemy.movable[0]) & (~(atDown & (atLeft | atRight))))
                enemy.movable[1] = ((enemy.movable[1]) & (~(atUp & (atLeft | atRight))))
                enemy.movable[2] = ((enemy.movable[2]) & (~(atRight & (atUp | atDown))))
                enemy.movable[3] = ((enemy.movable[3]) & (~(atLeft & (atUp | atDown))))
            dxMin = (self.player.info.size[0] + obstacle.size[0]) / 2
            dyMin = (self.player.info.size[1] + obstacle.size[1]) / 2
            atDown = ((self.player.info.site[1] > obstacle.site[1]) & (
                        self.player.info.site[1] < obstacle.site[1] + dyMin + COLLISIONTHRESHOLD))
            atUp = ((self.player.info.site[1] < obstacle.site[1]) & (
                        self.player.info.site[1] > obstacle.site[1] - dyMin - COLLISIONTHRESHOLD))
            atRight = ((self.player.info.site[0] > obstacle.site[0]) & (
                        self.player.info.site[0] < obstacle.site[0] + dxMin + COLLISIONTHRESHOLD))
            atLeft = ((self.player.info.site[0] < obstacle.site[0]) & (
                        self.player.info.site[0] > obstacle.site[0] - dxMin - COLLISIONTHRESHOLD))
            self.player.movable[0] = ((self.player.movable[0]) & (~(atDown & (atLeft | atRight))))
            self.player.movable[1] = ((self.player.movable[1]) & (~(atUp & (atLeft | atRight))))
            self.player.movable[2] = ((self.player.movable[2]) & (~(atRight & (atUp | atDown))))
            self.player.movable[3] = ((self.player.movable[3]) & (~(atLeft & (atUp | atDown))))

    def obstacleLoad(self):
        for ob in Et.R_sg.obstacle_list:
            temp = It.ObstacleInfo()
            temp.site = ob["site"]
            temp.size = ob["size"]
            temp.kind = ob["kind"]
            Et.Os_info.append(temp)

    def update(self):
        self.moveJudge()
        self.signalSend()
        for skill in self.skill_list:
            skill.update()
        for enemy in self.enemy_list:
            enemy.update()
        self.player.update()

    def signalSend(self):
        self.playerSignal()

    def playerSignal(self):
        move_state = Et.I_ctr.p1_key["up"] << 3 | Et.I_ctr.p1_key["down"] << 2 | Et.I_ctr.p1_key["left"] << 1 | Et.I_ctr.p1_key["right"]
        move_switch = [None, 3, 2, None, 1, 7, 6, None, 0, 5, 4, None, None, None, None, None]
        self.player.signal = move_switch[move_state]
        if Et.I_ctr.p1_key["atk1"]:
            self.player.signal = SKILL1



        # 信号类
class Signal():
    def __init__(self,type,receiver):
        self.type=type
        self.receiver=receiver