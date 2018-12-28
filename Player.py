#
#   人物类
#

from Define import *
import Extern as Et
import Skill

direct_list = [
    "up","down","left","right"
]

class PlayerInfo():
    def __init__(self):
        self.site = [200,400]
        self.max_life = 0
        self.life_value = 0
        self.state = PLAYERSTATIC
        self.pic_direction = RIGHT
        self.size = [0,0]
        self.count = 0
        self.visible = True
        self.kind = 0
        self.camp = 0

class Player():
    def __init__(self,pinfo):
        self.info = pinfo
        self.velocity = [0, 0]
        self.movable = [True,True,True,True]    #上下左右方向是否可移动
        self.game = None    #游戏指针
        self.skill_time = [0,0,0]   #技能123的上次发动时间
        self.skill_cd = [0,0,0] #技能123的冷却时间
        self.freeze_time = 0    #被攻击后僵直时间
        self.signal = None
        self.direction = MOVERIGHT
        self.skill_type = [0, 0, 0]
        self.max_count = 12
        self.skill_list = [[], [], []]

    def update(self):
        if self.info.state == PLAYERSTATIC:
            if self.signal == None:
                pass
            elif ((self.signal < 8) & (self.signal > -1)):
                self.direction = self.signal
                self.switchState(PLAYERMOVE)
            elif self.signal == ATTACKED:
                self.switchState(PLAYERATTACKED)
            elif self.signal == SKILL1:
                if ((Et.fresh_time - self.skill_time[0]) > self.skill_cd[0]):
                    self.switchState(PLAYERSKILL1)
            elif self.signal == SKILL2:
                if ((Et.fresh_time - self.skill_time[1]) > self.skill_cd[1]):
                    self.switchState(PLAYERSKILL2)
            elif self.signal == SKILL3:
                if ((Et.fresh_time - self.skill_time[2]) > self.skill_cd[2]):
                    self.switchState(PLAYERSKILL3)
            elif self.signal == DIE:
                self.switchState(PLAYERDEAD)
            self.info.count = (self.info.count + 1) % self.max_count
        elif self.info.state == PLAYERMOVE:
            if self.signal == None:
                self.switchState(PLAYERSTATIC)
            elif ((self.signal < 8) & (self.signal > -1)):
                self.direction = self.signal
                self.info.count = (self.info.count + 1) % self.max_count
                self.move()
            elif self.signal == ATTACKED:
                self.switchState(PLAYERATTACKED)
            elif self.signal == SKILL1:
                if ((Et.fresh_time - self.skill_time[0]) > self.skill_cd[0]):
                    self.switchState(PLAYERSKILL1)
            elif self.signal == SKILL2:
                if ((Et.fresh_time - self.skill_time[1]) > self.skill_cd[1]):
                    self.switchState(PLAYERSKILL2)
            elif self.signal == SKILL3:
                if ((Et.fresh_time - self.skill_time[2]) > self.skill_cd[2]):
                    self.switchState(PLAYERSKILL3)
            elif self.signal == DIE:
                self.switchState(PLAYERDEAD)
        elif self.info.state == PLAYERSKILL1:
            self.skillstate(1)
        elif self.info.state == PLAYERSKILL2:
            self.skillstate(2)
        elif self.info.state == PLAYERSKILL3:
            self.skillstate(3)
        elif self.info.state == PLAYERATTACKED:
            if self.info.count == self.max_count-1:
                self.switchState(PLAYERSTATIC)
            else:
                self.info.count = self.info.count + 1
            if self.signal == ATTACKED:
                self.switchState(PLAYERATTACKED)
            elif self.signal == DIE:
                self.switchState(PLAYERDEAD)
        elif self.info.state == PLAYERDEAD:
            pass

    #单独处理正在发起技能的状态
    def skillstate(self,n):
        if self.info.count==int(self.max_count/2):
            self.actSkill(n)
            self.skill_time[n-1]=Et.fresh_time-10/fps
        elif self.info.count==self.max_count - 1:
            self.switchState(PLAYERSTATIC)
        if self.signal==ATTACKED:
            self.switchState(PLAYERATTACKED)
        elif self.signal==DIE:
            self.switchState(PLAYERDEAD)
        self.info.count=self.info.count+1

    #状态转换，计数置零
    def switchState(self,state):
        self.info.count=0
        self.info.state=state

    # 发起不同的技能，新技能在此添加
    def actSkill(self, n):
        skill_type = self.skill_type[n - 1]
        if skill_type in[SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE,SKILLBLACKHOLE,SKILLHOOK,SKILLKEKKAI]:
            new_skill = self.releaseEntitySkill(skill_type)
            self.skill_list[n - 1].append(new_skill)
            if skill_type == SKILLBLACKHOLE:
                new_skill.effect_radius = (new_skill.info.size[0] + new_skill.info.size[1]) / 4
                new_skill.displacement = new_skill.resource.extra_param1
            elif skill_type == SKILLKEKKAI:
                new_skill.radius = (new_skill.info.size[0] + new_skill.info.size[1]) / 4
        elif skill_type == SKILLRETURN:
            if not self.skill_list[n - 1]:
                new_skill = self.releaseEntitySkill(SKILLRETURN)
                self.skill_list[n - 1].append(new_skill)
            else:
                self.info.site = self.skill_list[n - 1][0].init_site[:]
                self.skill_list[n - 1][0].delflag = True
        elif skill_type in [SKILLBOMB, SKILLAIM]:
            if not self.skill_list[n - 1]:
                new_skill = self.releaseEntitySkill(skill_type)
                if skill_type == SKILLBOMB:
                    follow = Et.R_sk[SKILLBOMBEXPLODING]
                    new_skill.explosion_radius = (follow.size[0] + follow.size[1]) / 4
                elif skill_type == SKILLAIM:
                    follow = Et.R_sk[SKILLAIMFIRED]
                    new_skill.fire_range = (follow.size[0] + follow.size[1]) / 4
                self.skill_list[n - 1].append(new_skill)
            else:
                self.skill_list[n - 1][0].setOff()
        elif skill_type == SKILLBALLRETURN:
            if not self.skill_list[n - 1]:
                for direction in [MOVELEFT, MOVERIGHT, MOVEUP, MOVEDOWN, MOVEUPLEFT, MOVEUPRIGHT, MOVEDOWNLEFT,
                                  MOVEDOWNRIGHT]:
                    new_skill = self.releaseEntitySkill(SKILLBALLRETURN)
                    new_skill.direction = direction
                    new_skill.returning_velocity = new_skill.resource.extra_param1
                    self.skill_list[n - 1].append(new_skill)
            else:
                for ball in self.skill_list[n - 1]:
                    ball.returning = True
        elif skill_type == SKILLPORTAL:
            if not self.skill_list[n - 1]:
                new_skill = self.releaseEntitySkill(SKILLPORTAL)
                new_skill.effect_radius = (new_skill.info.size[0] + new_skill.info.size[1]) / 4
                self.skill_list[n - 1].append(new_skill)
            elif len(self.skill_list[n - 1]) == 1:
                new_skill = self.releaseEntitySkill(SKILLPORTAL)
                new_skill.effect_radius = (new_skill.info.size[0] + new_skill.info.size[1]) / 4
                new_skill.pair = self.skill_list[n - 1][0]
                self.skill_list[n - 1][0].pair = new_skill
                new_skill.ignore_list.append(self)
                self.skill_list[n - 1][0].ignore_list.append(self)
                self.skill_list[n - 1].append(new_skill)
            else:
                self.skill_list[n - 1][0].delflag = True
                self.skill_list[n - 1][1].delflag = True
        elif skill_type == SKILLTRIANGLE:
            if len(self.skill_list[n - 1]) < 3:
                new_skill = self.releaseEntitySkill(SKILLTRIANGLE)
                if self.skill_list[n - 1]:
                    self.skill_list[n - 1][-1].next = new_skill
                    new_skill.next = self.skill_list[n - 1][0]
                self.skill_list[n - 1].append(new_skill)
                if len(self.skill_list[n - 1]) == 3:
                    for vertex in self.skill_list[n - 1]:
                        vertex.effective = True


    #专门用于扔出实体球的技能，n选择球轨迹
    def releaseEntitySkill(self,skill_type):
        new_skill = None
        new_skill_info = Skill.SkillInfo()
        Et.Sk_info.append(new_skill_info)
        if skill_type==SKILLBALLSTRAIGHT:
            new_skill=Skill.SkillBallStraight(new_skill_info)
            new_skill.influence_list = self.game.enemy_list[:]
        elif skill_type==SKILLBALLSINUS:
            new_skill=Skill.SkillBallSinus(new_skill_info)
            new_skill.influence_list = self.game.enemy_list[:]
        elif skill_type==SKILLBALLCIRCLE:
            new_skill=Skill.SkillBallCircle(new_skill_info)
            new_skill.influence_list = self.game.enemy_list[:]
        elif skill_type==SKILLRETURN:
            new_skill=Skill.SkillReturn(new_skill_info)
        elif skill_type == SKILLBLACKHOLE:
            new_skill = Skill.SkillBlackHole(new_skill_info)
            new_skill.influence_list = self.game.enemy_list[:]
        elif skill_type == SKILLHOOK:
            new_skill = Skill.SkillHook(new_skill_info)
        elif skill_type == SKILLBOMB:
            new_skill = Skill.SkillBomb(new_skill_info)
            new_skill.influence_list = self.game.enemy_list[:]
        elif skill_type == SKILLAIM:
            new_skill = Skill.SkillAim(new_skill_info)
            new_skill.influence_list = self.game.enemy_list[:]
        elif skill_type == SKILLKEKKAI:
            new_skill = Skill.SkillKekkai(new_skill_info)
            new_skill.influence_list = self.game.enemy_list[:]
        elif skill_type == SKILLBALLRETURN:
            new_skill = Skill.SkillBallReturn(new_skill_info)
            new_skill.influence_list = self.game.enemy_list[:]
        elif skill_type == SKILLPORTAL:
            new_skill = Skill.SkillPortal(new_skill_info)
            new_skill.influence_list = self.game.enemy_list[:]
            new_skill.influence_list.append(self)
            new_skill.ignore_list.append(self)
        elif skill_type == SKILLTRIANGLE:
            new_skill = Skill.SkillTriangle(new_skill_info)
            new_skill.influence_list = self.game.enemy_list[:]
        new_skill.resource=Et.R_sk[skill_type]
        new_skill.game=self.game
        new_skill.init_site=self.info.site[:]
        new_skill.init_time=Et.fresh_time
        new_skill.caster=self
        new_skill.direction=self.direction
        new_skill.info.site=self.info.site[:]
        new_skill.info.size=new_skill.resource.size
        new_skill.damage=new_skill.resource.damage
        new_skill.velocity=new_skill.resource.velocity
        new_skill.duration=new_skill.resource.duration
        self.game.skill_list.append(new_skill)
        return new_skill


    def move(self):
        for i in range(0,4):
            if self.movable[i]&(Et.I_ctr.p1_key[direct_list[i]] == True):
                self.info.site = [
                    self.info.site[0] + ((i == 3) - (i == 2)) * self.velocity[0],
                    self.info.site[1] + ((i == 1) - (i == 0)) * self.velocity[1],
                ]
                if i == 2:
                    self.info.pic_direction = LEFT
                elif i == 3:
                    self.info.pic_direction = RIGHT
        if self.info.site[0] > (Et.R_sg.size[0] - int(self.info.size[0] / 2)):
            self.info.site[0] = Et.R_sg.size[0] - int(self.info.size[0] / 2)
        if self.info.site[0] < int(self.info.size[0] / 2):
            self.info.site[0] = int(self.info.size[0] / 2)
        if self.info.site[1] > (Et.R_sg.size[1] - int(self.info.size[1] / 2)):
            self.info.site[1] = Et.R_sg.size[1] - int(self.info.size[1] / 2)
        if self.info.site[1] < int(self.info.size[1] / 2):
            self.info.site[1] = int(self.info.size[1] / 2)