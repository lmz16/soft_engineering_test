#
#   联机版本专用人物文件
#

from Define import *
import Skill
import Extern as Et
import Mainfunc as Mf

direct_list = [
    "up","down","left","right"
]

class Player():
    def __init__(self,info):
        self.id = 0 #玩家id,用于区分控制对应的是哪一个玩家对象
        self.camp = 0   #玩家阵营,用于区分技能伤害
        self.info = info
        self.velocity = [10, 10]
        self.movable = [True, True, True, True]  # 上下左右方向是否可移动
        self.game = None  # 游戏指针
        self.skill_time = [0, 0, 0]  # 技能123的上次发动时间
        self.skill_cd = [0, 0, 0]  # 技能123的冷却时间
        self.freeze_time = 0  # 被攻击后僵直时间
        self.signal = None
        self.direction = MOVERIGHT
        self.skill_type = [0, 0, 0]
        self.max_count = 12
        self.return_site = [0, 0]
        self.return_released = False
        self.skill_list = [[], [], []]

    def update(self):
        if self.info["state"] == PLAYERSTATIC:
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
            self.info["count"] = (self.info["count"] + 1) % self.max_count
        elif self.info["state"] == PLAYERMOVE:
            if self.signal == None:
                self.switchState(PLAYERSTATIC)
            elif ((self.signal < 8) & (self.signal > -1)):
                self.direction = self.signal
                self.info["count"] = (self.info["count"] + 1) % self.max_count
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
        elif self.info["state"] == PLAYERSKILL1:
            self.skillstate(1)
        elif self.info["state"] == PLAYERSKILL2:
            self.skillstate(2)
        elif self.info["state"] == PLAYERSKILL3:
            self.skillstate(3)
        elif self.info["state"] == PLAYERATTACKED:
            if self.info["count"] == self.freeze_time:
                self.switchState(PLAYERSTATIC)
            else:
                self.info["count"] = self.info["count"] + 1
            if self.signal == ATTACKED:
                self.switchState(PLAYERATTACKED)
            elif self.signal == DIE:
                self.switchState(PLAYERDEAD)
        elif self.info["state"] == PLAYERDEAD:
            pass

    #单独处理正在发起技能的状态
    def skillstate(self,n):
        if self.info["count"]==int(self.max_count/2):
            self.actSkill(n)
            self.skill_time[n-1]=Et.fresh_time-10/fps
        elif self.info["count"]==self.max_count - 1:
            self.switchState(PLAYERSTATIC)
        if self.signal==ATTACKED:
            self.switchState(PLAYERATTACKED)
        elif self.signal==DIE:
            self.switchState(PLAYERDEAD)
        self.info["count"]=self.info["count"]+1

    #状态转换，计数置零
    def switchState(self,state):
        self.info["count"]=0
        self.info["state"]=state

    # 发起不同的技能，新技能在此添加
    def actSkill(self, n):
        skill_type = self.skill_type[n - 1]
        if skill_type in[SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE,SKILLBLACKHOLE,SKILLHOOK]:
            new_skill = self.releaseBall(skill_type)
            self.skill_list[n - 1].append(new_skill)
            self.game.skill_list.append(new_skill)
        elif skill_type == SKILLRETURN:
            if self.return_released == True:
                self.info["site"] = self.return_site[:]
            else:
                self.return_site = self.info["site"][:]
            self.return_released = not self.return_released
        elif skill_type in [SKILLBOMB, SKILLAIM]:
            if not self.skill_list[n - 1]:
                new_skill = self.releaseBall(skill_type)
                self.skill_list[n - 1].append(new_skill)
            else:
                self.skill_list[n - 1][0].setOff()
        # elif skill_type == SKILLBALLRETURN:
        #     if not self.skill_list[n - 1]:
        #         for direction in [MOVELEFT, MOVERIGHT, MOVEUP, MOVEDOWN, MOVEUPLEFT, MOVEUPRIGHT, MOVEDOWNLEFT,
        #                           MOVEDOWNRIGHT]:
        #             new_skill = self.releaseBall(SKILLBALLRETURN,n-1)
        #             new_skill.direction = direction
        #             self.skill_list[n - 1].append(new_skill)
        #     else:
        #         for ball in self.skill_list[n - 1]:
        #             ball.returning = True


    #专门用于扔出实体球的技能，n选择球轨迹
    def releaseBall(self,skill_type):
        new_skill = None
        temp = Mf.sinfoInit()
        Et.Sk_info.append(temp)
        if skill_type==SKILLBALLSTRAIGHT:
            new_skill=Skill.SkillBallStraight(temp)
        elif skill_type==SKILLBALLSINUS:
            new_skill=Skill.SkillBallSinus(temp)
        elif skill_type==SKILLBALLCIRCLE:
            new_skill=Skill.SkillBallCircle(temp)
        elif skill_type == SKILLBLACKHOLE:
            new_skill = Skill.SkillBlackHole(temp)
        elif skill_type == SKILLHOOK:
            new_skill = Skill.SkillHook(temp)
        elif skill_type == SKILLBOMB:
            new_skill = Skill.SkillBomb(temp)
        elif skill_type == SKILLAIM:
            new_skill = Skill.SkillAim(temp)
        elif skill_type == SKILLKEKKAI:
            new_skill = Skill.SkillKekkai(temp)
        elif skill_type == SKILLBALLRETURN:
            new_skill = Skill.SkillBallReturn(temp)
        self.configSkill(new_skill, skill_type)
        return new_skill


    def move(self):
        for i in range(0,4):
            if self.movable[i]&(self.game.ctr[self.id][direct_list[i]] == True):
                self.info["site"] = [
                    self.info["site"][0] + ((i == 3) - (i == 2)) * self.velocity[0],
                    self.info["site"][1] + ((i == 1) - (i == 0)) * self.velocity[1],
                ]
                if i == 2:
                    self.info["pic_direction"] = LEFT
                elif i == 3:
                    self.info["pic_direction"] = RIGHT
        if self.info["site"][0] > (self.game.size[0] - int(self.info["size"][0] / 2)):
            self.info["site"][0] = self.game.size[0] - int(self.info["size"][0] / 2)
        if self.info["site"][0] < int(self.info["size"][0] / 2):
            self.info["site"][0] = int(self.info["size"][0] / 2)
        if self.info["site"][1] > (self.game.size[1] - int(self.info["size"][1] / 2)):
            self.info["site"][1] = self.game.size[1] - int(self.info["size"][1] / 2)
        if self.info["site"][1] < int(self.info["size"][1] / 2):
            self.info["site"][1] = int(self.info["size"][1] / 2)



    def configSkill(self,skill,type):
        skill.damage = Et.R_skill[type]["damage"]
        skill.velocity = Et.R_skill[type]["velocity"]
        skill.duration = Et.R_skill[type]["duration"]
        skill.info["size"] = Et.R_skill[type]["size"]
        skill.init_time = Et.fresh_time
        skill.info["kind"] = type
        skill.caster = self
        skill.game = self.game
        skill.init_site=self.info["site"][:]
        skill.direction=self.direction
        skill.info["site"]=self.info["site"][:]
        skill.load()


    def passiveMove(self,mv):
        temp = [self.info["site"][0] + mv[0], self.info["site"][1] + mv[1]]
        flag = False
        for ob in self.game.obstacle_list:
            if abs(temp[0] - ob.info["site"][0]) < ob.info["size"][0] and abs(temp[1] - ob.info["site"][1]) < ob.info["size"][1]:
                flag = True
                break
        if not flag:
            self.info.site = temp