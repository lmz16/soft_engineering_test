from Define import *
import Extern as Et
import Mainfunc as Mf
import math

class Skill():
    def __init__(self, sinfo):
        self.info = sinfo
        self.direction = MOVERIGHT
        self.game = None
        self.init_time = 0
        self.duration = 0
        self.delflag = False
        self.velocity = [0, 0]
        self.movex = []
        self.movey = []
        self.caster = None
        self.influence_list = []
        self.damage = 0
        self.ignore_list = []
        self.init_site = [0, 0]
        self.load()

    def collisionJudge(self, collider):
        if ((abs(collider.info["site"][0] - self.info["site"][0]) - (collider.info["size"][0] + self.info["size"][0]) / 2 < 0) and
                (abs(collider.info["site"][1] - self.info["site"][1]) - (collider.info["size"][1] + self.info["size"][1]) / 2 < 0)):
            return True
        else:
            return False

    def defaultInfluence(self):
        for obj in self.influence_list:
            if self.collisionJudge(obj):
                if not obj in self.ignore_list:
                    obj.info["life"] -= self.damage
                    obj.signal = ATTACKED
                    self.ignore_list.append(obj)
            else:
                if obj in self.ignore_list:
                    self.ignore_list.remove(obj)

    def load(self):
        self.movex = [self.velocity[0] * x for x in movex]
        self.movey = [self.velocity[1] * y for y in movey]


class SkillBallStraight(Skill):
    def __init__(self,info):
        Skill.__init__(self,info)

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True
        else:
            self.info["site"][0] = self.info["site"][0] + self.movex[self.direction]
            self.info["site"][1] = self.info["site"][1] + self.movey[self.direction]

    def influence(self):
        self.defaultInfluence()


class SkillBallSinus(Skill):
    def __init__(self,info):
        Skill.__init__(self,info)

    def update(self):
        if Et.fresh_time - self.init_time > self.duration:
            self.delflag = True
        else:
            sinmovex = fps * self.velocity[0] * (Et.fresh_time - self.init_time)
            sinmovey = 50 * math.sin(2 * math.pi * (Et.fresh_time - self.init_time))
            transmat = [
                [0, 1, -1, 0], [0, -1, 1, 0], [-1, 0, 0, -1], [1, 0, 0, 1],
                [-1, 1, -1, -1], [1, 1, -1, 1], [-1, -1, 1, -1], [1, -1, 1, 1]
            ]
            self.info["site"] = [
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
            dx = 1.5 * max(self.caster.info["size"]) * math.cos(2 * math.pi * (Et.fresh_time - self.init_time))
            dy = 1.5 * max(self.caster.info["size"]) * math.sin(2 * math.pi * (Et.fresh_time - self.init_time))
            self.info["site"] = [
                self.caster.info["site"][0] + int(dx),
                self.caster.info["site"][1] + int(dy)]

    def influence(self):
        self.defaultInfluence()
        
        
class SkillReturn(Skill):
    def __init__(self,info):
        Skill.__init__(self,info)

    def update(self):
        pass

    def influence(self):
        pass


class SkillBlackHole(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)
        self.effect_radius = 150
        self.displacement = 10

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True

    def influence(self):
        for obj in self.influence_list:
            distance = math.sqrt(
                (self.info["site"][0] - obj.info["site"][0]) ** 2 + (self.info["site"][1] - obj.info["site"][1]) ** 2)
            if distance < self.effect_radius and distance > 0:
                if distance > self.displacement:
                    obj_move_vector = [(self.info["site"][0] - obj.info["site"][0]) / distance * self.displacement,
                        (self.info["site"][1] - obj.info["site"][1]) / distance * self.displacement]
                else:
                    obj_move_vector = [self.info["site"][0] - obj.info["site"][0],
                                         self.info["site"][1] - obj.info["site"][1]]
                obj.passiveMove(obj_move_vector)


class SkillHook(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)
        self.attach = None

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True
        elif not self.delflag:
            self.info["site"][0] = self.info["site"][0] + self.movex[self.direction]
            self.info["site"][1] = self.info["site"][1] + self.movey[self.direction]
            for obstacle in self.game.obstacle_list:
                if self.collisionJudge(obstacle):
                    self.attach = obstacle
                    self.casterMove()
        self.info.draw_line = [self.info["site"], self.caster.info["site"]]

    def influence(self):
        pass
    
    def casterMove(self):
        self.caster.info["site"]=self.info["site"][:]
        lborder=self.attach.info["site"][0]-(self.caster.info["size"][0]+self.attach.info["size"][0])/2
        rborder=self.attach.info["site"][0]+(self.caster.info["size"][0]+self.attach.info["size"][0])/2
        uborder=self.attach.info["site"][1]-(self.caster.info["size"][1]+self.attach.info["size"][1])/2
        dborder=self.attach.info["site"][1]+(self.caster.info["size"][1]+self.attach.info["size"][1])/2
        if self.caster.info["site"][0]>lborder-10 and self.caster.info["site"][0]<lborder+50:
            self.caster.info["site"][0]=lborder-10
        elif self.caster.info["site"][0]<rborder+10 and self.caster.info["site"][0]>rborder-50:
            self.caster.info["site"][0]=rborder+10
        if self.caster.info["site"][1]>uborder-10 and self.caster.info["site"][1]<uborder+50:
            self.caster.info["site"][1]=uborder-10
        elif self.caster.info["site"][1]<dborder+10 and self.caster.info["site"][1]>dborder-50:
            self.caster.info["site"][1]=dborder+10
        self.delflag = True


class SkillBomb(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)
        self.explosion_radius = 200
        self.explosion_flag = False

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.setOff()

    def influence(self):
        pass

    def setOff(self):
        if not self.delflag:
            for obj in self.influence_list:
                distance = math.sqrt(
                    (self.info["site"][0] - obj.info["site"][0]) ** 2 + (self.info["site"][1] - obj.info["site"][1]) ** 2)
                if distance < self.explosion_radius:
                    obj.info["life"] -= self.damage
                    obj.signal = ATTACKED
            exploding_info = Mf.sinfoInit()
            Et.Sk_info.append(exploding_info)
            exploding = SkillBombExploding(exploding_info)
            #exploding.resource = Et.R_sk[SKILLBOMBEXPLODING]
            exploding.game = self.game
            exploding.init_site = self.info["site"][:]
            exploding.init_time = Et.fresh_time
            exploding.caster = self.caster
            exploding.direction = self.direction
            exploding.info["site"] = self.info["site"][:]
            exploding.info["size"] = Et.R_skill[SKILLBOMBEXPLODING]["size"]
            exploding.damage = Et.R_skill[SKILLBOMBEXPLODING]["damage"]
            exploding.duration = Et.R_skill[SKILLBOMBEXPLODING]["duration"]
            self.game.skill_list.append(exploding)
            self.delflag = True


class SkillBombExploding(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True

    def influence(self):
        pass


class SkillAim(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)
        self.fire_range = 50

    def update(self):
        if Et.fresh_time - self.init_time > self.duration:
            self.delflag = True
        else:
            dx = 10 * self.velocity[0] * (Et.fresh_time - self.init_time)
            transmat = [
                [0, 1, -1, 0], [0, -1, 1, 0], [-1, 0, 0, -1], [1, 0, 0, 1],
                [-1, 1, -1, -1], [1, 1, -1, 1], [-1, -1, 1, -1], [1, -1, 1, 1]
            ]
            self.info["site"] = [self.caster.info["site"][0] + int(dx * transmat[self.direction][0]),
                              self.caster.info["site"][1] + int(dx * transmat[self.direction][2])]

    def influence(self):
        pass

    def setOff(self):
        if not self.delflag:
            for obj in self.influence_list:
                distance = math.sqrt(
                    (self.info["site"][0] - obj.info["site"][0]) ** 2 + (self.info["site"][1] - obj.info["site"][1]) ** 2)
                if distance < self.fire_range:
                    obj.info["life"] -= self.damage
                    obj.signal = ATTACKED
            fired_info = SkillInfo()
            Et.Sk_info.append(fired_info)
            fired = SkillAimFired(fired_info)
            #fired.resource = Et.R_sk[SKILLAIMFIRED]
            fired.game = self.game
            fired.init_site = self.info["site"][:]
            fired.init_time = Et.fresh_time
            fired.caster = self.caster
            fired.direction = self.direction
            fired.info["site"] = self.info["site"][:]
            fired.info["size"] = Et.R_skill[SKILLAIMFIRED]["size"]
            fired.damage = Et.R_skill[SKILLAIMFIRED]["damage"]
            fired.duration = Et.R_skill[SKILLAIMFIRED]["duration"]
            self.game.skill_list.append(fired)
            self.delflag = True


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
        self.radius = 150

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            self.delflag = True

    def influence(self):
        for obj in self.influence_list:
            distance = math.sqrt(
                (self.info["site"][0] - obj.info["site"][0]) ** 2 + (self.info["site"][1] - obj.info["site"][1]) ** 2)
            obj_radius = (obj.info["size"][0] + obj.info["size"][1]) / 4
            if abs(distance - self.radius) < obj_radius:
                if not obj in self.ignore_list:
                    obj.info["life"] -= self.damage
                    obj.signal = ATTACKED
                    self.ignore_list.append(obj)
            else:
                if obj in self.ignore_list:
                    self.ignore_list.remove(obj)


class SkillBallReturn(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)
        self.returning = False
        self.returning_velocity = 40

    def update(self):
        if not self.returning:
            if (Et.fresh_time - self.init_time) > self.duration:
                self.delflag = True
            else:
                self.info["site"][0] = self.info["site"][0] + self.movex[self.direction]
                self.info["site"][1] = self.info["site"][1] + self.movey[self.direction]
        else:
            distance = math.sqrt((self.caster.info["site"][0] - self.info["site"][0]) ** 2 + (
                        self.caster.info["site"][1] - self.info["site"][1]) ** 2)
            if distance < self.returning_velocity:
                self.info["site"] = self.caster.info["site"][:]
            else:
                self.info["site"] = [self.info["site"][0] + (
                            self.caster.info["site"][0] - self.info["site"][0]) / distance * self.returning_velocity,
                                  self.info["site"][1] + (self.caster.info["site"][1] - self.info["site"][
                                      1]) / distance * self.returning_velocity]
            if self.info["site"] == self.caster.info["site"]:
                self.delflag = True

    def influence(self):
        self.defaultInfluence()
        
        
class SkillPortal(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)
        self.info.kind = SKILLPORTAL
        self.pair = None
        self.effect_radius = 50

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration and self.pair != None and (Et.fresh_time - self.pair.init_time) > self.pair.duration:
            self.delflag = True

    def influence(self):
        if self.pair != None:
            for obj in self.influence_list:
                distance = math.sqrt(
                    (self.info["site"][0] - obj.info["site"][0]) ** 2 + (self.info["site"][1] - obj.info["site"][1]) ** 2)
                pair_distance = math.sqrt(
                    (self.pair.info["site"][0] - obj.info["site"][0]) ** 2 + (self.pair.info["site"][1] - obj.info["site"][1]) ** 2)
                if distance < self.effect_radius:
                    if not obj in self.ignore_list and not obj in self.pair.ignore_list:
                        obj.info["site"] = self.pair.info["site"][:]
                        self.ignore_list.append(obj)
                        self.pair.ignore_list.append(obj)
                elif pair_distance >= self.pair.effect_radius:
                    if obj in self.ignore_list or obj in self.pair.ignore_list:
                        self.ignore_list.remove(obj)
                        self.pair.ignore_list.remove(obj)
                    
                    
class SkillTriangle(Skill):
    def __init__(self, info):
        Skill.__init__(self, info)
        self.info.kind = SKILLTRIANGLE
        self.next = None
        self.effective = False

    def update(self):
        if (Et.fresh_time - self.init_time) > self.duration:
            if self.effective:
                checker = self
                while True:
                    checker.effective = False
                    checker = checker.next
                    if checker == self:
                        break
            self.delflag = True
        if self.effective:
            self.info.draw_line = [self.info["site"], self.next.info["site"]]
        else:
            self.info.draw_line = None

    def influence(self):
        if self.effective:
            [x1,y1] = self.info["site"][:]
            [x2,y2] = self.next.info["site"][:]
            for obj in self.influence_list:
                [x,y] = obj.info["site"][:]
                distance = abs(((y2-y1)*x-(x2-x1)*y-x1*y2+x2*y1))/math.sqrt((y2-y1)**2+(x2-x1)**2)
                obj_radius = (obj.info["size"][0]+obj.info["size"][1])/4
                if distance < obj_radius and (x-x1)*(x2-x1)+(y-y1)*(y2-y1) >= 0 and (x-x2)*(x1-x2)+(y-y2)*(y1-y2) >= 0:
                    if not obj in self.ignore_list:
                        obj.info["life"] -= self.damage
                        obj.signal = ATTACKED
                        self.ignore_list.append(obj)
                else:
                    if obj in self.ignore_list:
                        self.ignore_list.remove(obj)