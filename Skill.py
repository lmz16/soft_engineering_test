#
#   技能类文件
#

#   会调用update(),修改技能状态
#   调用influence(),对单位造成影响
#   应有忽略单位列表ignore_list
#   delflag

from Define import *
import Extern as Et
import Player
import Game
import Item
import math


class SkillInfo():
    def __init__(self):  ##############需要加载资源#######################
        self.site = [0, 0]
        self.size = 0
        self.visible = True


class Skill():
    def __init__(self, sinfo):  ##############需要加载资源#######################
        self.info = sinfo
        self.direction = MOVERIGHT
        self.game = None
        self.init_time = 0
        self.duration = 0
        self.delflag = False
        self.velocity = 0
        self.movex = []
        self.movey = []
        self.caster = None
        self.damage = 0
        self.ignore_list = []
        self.ignore_player = False
        self.init_site = [0, 0]
        self.resource = None

    def collisionJudge(self, collider):
        if ((abs(collider.info.site[0] - self.info.site[0]) - (collider.info.size[0] + self.info.size[0]) / 2 < 0) &
                (abs(collider.info.site[1] - self.info.site[1]) - (collider.info.size[1] + self.info.size[1]) / 2 < 0)):
            return True
        else:
            return False

    def defaultInfluence(self):
        if self.caster == self.game.player:
            for enemy in self.game.enemy_list:
                if self.collisionJudge(enemy):
                    if not enemy in self.ignore_list:
                        enemy.info.life_value -= self.damage
                        self.ignore_list.append(enemy)
                else:
                    if enemy in self.ignore_list:
                        self.ignore_list.remove(enemy)
        else:
            if self.collisionJudge(self.game.player):
                self.game.player.info.life_value -= self.damage
                self.ignore_player = True
            else:
                self.ignore_player = False

    def load(self):
        self.movex = [self.velocity * x for x in movex]
        self.movey = [self.velocity * y for y in movey]


class SkillBallStraight(Skill):
    def __init__(self,info):
        Skill.__init__(self,info)

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True
        else:
            print()
            self.info.site[0] = self.info.site[0] + movex[self.direction]
            self.info.site[1] = self.info.site[1] + movey[self.direction]

    def influence(self):
        self.defaultInfluence()


class SkillBallSinus(Skill):
    def __init__(self,info):
        Skill.__init__(self,info)

    def update(self):
        if Et.fresh_time - self.init_time > self.duration:
            self.delflag = True
        else:
            sinmovex = 10 * self.velocity * (Et.fresh_time - self.init_time)
            sinmovey = 50 * math.sin(2 * math.pi * (Et.fresh_time - self.init_time))
            transmat = [
                [0, 1, -1, 0], [0, -1, 1, 0], [-1, 0, 0, -1], [1, 0, 0, 1],
                [-1, 1, -1, -1], [1, 1, -1, 1], [-1, -1, 1, -1], [1, -1, 1, 1]
            ]
            self.info.site = [
                self.init_site[0] + int(
                    sinmovex * transmat[self.direction][0] + sinmovey * transmat[self.direction][1]),
                self.init_site[1] + int(sinmovex * transmat[self.direction][2] + sinmovey * transmat[self.direction][3])
            ]

    def influence(self):
        self.defaultInfluence()


class SkillBallCircle(Skill):
    def __init__(self,info):
        Skill.__init__(self,info)

    def update(self):
        if Et.fresh_time - self.init_time > self.duration:
            self.delflag = True
        else:
            dx = 1.5 * max(self.caster.info.size) * math.cos(2 * math.pi * (Et.fresh_time - self.init_time))
            dy = 1.5 * max(self.caster.info.size) * math.sin(2 * math.pi * (Et.fresh_time - self.init_time))
            self.info.site = [
                self.caster.info.site[0] + int(dx),
                self.caster.info.site[1] + int(dy)]

    def influence(self):
        self.defaultInfluence()