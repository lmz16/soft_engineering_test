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
        self.velocity = 10
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
            self.info.site[0] = self.info.site[0] + self.velocity*movex[self.direction]
            self.info.site[1] = self.info.site[1] + self.velocity*movey[self.direction]

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


class SkillBlackHole(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)
        self.effect_radius = 500  ##############需要加载资源#######################
        self.displacement = 1  ##############需要加载资源#######################

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True

    def influence(self):
        for enemy in self.game.enemy_list:
            distance = math.sqrt(
                (self.info.site[0] - enemy.info.site[0]) ** 2 + (self.info.site[1] - enemy.info.site[1]) ** 2)
            if distance < self.effect_radius and distance > 0:
                if distance > self.displacement:
                    enemy_move_vector = [(self.info.site[0] - enemy.info.site[0]) / distance * self.displacement,
                        (self.info.site[1] - enemy.info.site[1]) / distance * self.displacement]
                else:
                    enemy_move_vector = [self.info.site[0] - enemy.info.site[0],
                                         self.info.site[1] - enemy.info.site[1]]
                enemy.passiveMove(enemy_move_vector)


class SkillHook(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)
        self.find_obstacle = False
        self.attach = None

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True
        elif not self.find_obstacle:
            self.info.site[0] = self.info.site[0] + self.velocity * movex[self.direction]
            self.info.site[1] = self.info.site[1] + self.velocity * movey[self.direction]
            for obstacle in self.game.obstacle_list:
                if self.collisionJudge(obstacle):
                    self.attach = obstacle
                    self.find_obstacle = True

    def influence(self):
        if self.find_obstacle:
            self.caster.info.site=self.info.site[:]
            lborder=self.attach.info.site[0]-(self.caster.info.size[0]+self.attach.info.size[0])/2
            rborder=self.attach.info.site[0]+(self.caster.info.size[0]+self.attach.info.size[0])/2
            uborder=self.attach.info.site[1]-(self.caster.info.size[1]+self.attach.info.size[1])/2
            dborder=self.attach.info.site[1]+(self.caster.info.size[1]+self.attach.info.size[1])/2
            if self.caster.info.site[0]>lborder-COLLISIONTHRESHOLD and self.caster.info.site[0]<lborder:
                self.caster.info.site[0]=lborder-COLLISIONTHRESHOLD
            elif self.caster.info.site[0]<rborder+COLLISIONTHRESHOLD and self.caster.info.site[0]>rborder:
                self.caster.info.site[0]=rborder+COLLISIONTHRESHOLD
            if self.caster.info.site[1]>uborder-COLLISIONTHRESHOLD and self.caster.info.site[1]<uborder:
                self.caster.info.site[1]=uborder-COLLISIONTHRESHOLD
            elif self.caster.info.site[1]<dborder+COLLISIONTHRESHOLD and self.caster.info.site[1]>dborder:
                self.caster.info.site[1]=dborder+COLLISIONTHRESHOLD
            self.delflag = True
            
            
class SkillBomb(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)
        self.explosion_radius=500  ##############需要加载资源#######################
        self.explosion_flag=False

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True
        elif (Et.fresh_time - self.init_time) == self.duration:
            self.setOff()

    def influence(self):
        pass
            
    def setOff(self):
        for enemy in self.game.enemy_list:
            distance=math.sqrt((self.info.site[0]-enemy.info.site[0])**2+(self.info.site[1]-enemy.info.site[1])**2)
            if distance<self.explosion_radius:
                enemy.info.life_value-=self.damage
        exploding_info=SkillInfo()
        Et.Sk_info.append(exploding_info)
        exploding=SkillBombExploding(exploding_info)
        exploding.resource=Et.R_sk[0]  ##############需要修改资源#######################
        exploding.game=self.game
        exploding.init_site=self.info.site[:]
        exploding.init_time=Et.fresh_time
        exploding.caster=self.caster
        exploding.direction=self.direction
        exploding.info.site=self.info.site[:]
        exploding.info.size=exploding.resource.size
        exploding.damage=exploding.resource.damage
        exploding.duration=exploding.resource.duration
        self.game.skill_list.append(exploding)
        self.delflag=True
            
            
class SkillBombExploding(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True

    def influence(self):
        pass
    
    
class SkillAim(Skill):
    def __init__(self,info):
        Skill.__init__(self,info)
        self.fire_range=500  ##############需要加载资源#######################

    def update(self):
        if Et.fresh_time - self.init_time > self.duration:
            self.delflag = True
        else:
            dx=10*self.velocity*(Et.fresh_time-self.init_time)
            transmat = [
                [0, 1, -1, 0], [0, -1, 1, 0], [-1, 0, 0, -1], [1, 0, 0, 1],
                [-1, 1, -1, -1], [1, 1, -1, 1], [-1, -1, 1, -1], [1, -1, 1, 1]
            ]
            self.info.site=[self.caster.info.site[0]+int(dx*transmat[self.direction][0]),
                            self.caster.info.site[1]+int(dx*transmat[self.direction][2])]

    def influence(self):
        pass
    
    def setOff(self):
        for enemy in self.game.enemy_list:
            distance=math.sqrt((self.info.site[0]-enemy.info.site[0])**2+(self.info.site[1]-enemy.info.site[1])**2)
            if distance<self.fire_range:
                enemy.info.life_value-=self.damage
        fired_info=SkillInfo()
        Et.Sk_info.append(fired_info)
        fired=SkillAimFired(fired_info)
        fired.resource=Et.R_sk[0]  ##############需要修改资源#######################
        fired.game=self.game
        fired.init_site=self.info.site[:]
        fired.init_time=Et.fresh_time
        fired.caster=self.caster
        fired.direction=self.direction
        fired.info.site=self.info.site[:]
        fired.info.size=fired.resource.size
        fired.damage=fired.resource.damage
        fired.duration=fired.resource.duration
        self.game.skill_list.append(fired)
        self.delflag=True
        
        
class SkillAimFired(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True

    def influence(self):
        pass
    
    
class SkillKekkai(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)
        self.radius = 500  ##############需要加载资源#######################

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True

    def influence(self):
        for enemy in self.game.enemy_list:
            distance=math.sqrt((self.info.site[0]-enemy.info.site[0])**2+(self.info.site[1]-enemy.info.site[1])**2)
            enemy_radius=(enemy.info.size[0]+enemy.info.size[1])/4
            if abs(distance-self.radius)<enemy_radius:
                if not enemy in self.ignore_list:
                    enemy.info.life_value-=self.damage
                    self.ignore_list.append(enemy)
            else:
                if enemy in self.ignore_list:
                    self.ignore_list.remove(enemy)
                    
                    
class SkillBallReturn(Skill):
    def __init__(self,info):
        Skill.__init__(self,info)
        self.returning=False
        self.returning_velocity=20  ##############需要加载资源#######################

    def update(self):
        if not self.returning:
            if (Et.fresh_time - self.init_time) > self.duration:
                self.delflag = True
            else:
                self.info.site[0] = self.info.site[0] + self.velocity*movex[self.direction]
                self.info.site[1] = self.info.site[1] + self.velocity*movey[self.direction]
        else:
            distance=math.sqrt((self.caster.info.site[0]-self.info.site[0])**2+(self.caster.info.site[1]-self.info.site[1])**2)
            if distance<self.returning_velocity:
                self.info.site=self.caster.info.site[:]
            else:
                self.info.site=[self.info.site[0]+(self.caster.info.site[0]-self.info.site[0])/distance*self.returning_velocity,
                                self.info.site[1]+(self.caster.info.site[1]-self.info.site[1])/distance*self.returning_velocity]
            if self.info.site==self.caster.info.site:
                self.delflag=True

    def influence(self):
        self.defaultInfluence()