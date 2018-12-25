#
#   人物类
#

from Define import *
import Extern as Et
import Skill

direct_list = [
    "up", "down", "left", "right"
]


class PlayerInfo():
    def __init__(self):
        self.site = [200, 400]
        self.max_life = 0
        self.life_value = 0
        self.state = PLAYERSTATIC
        self.pic_direction = RIGHT
        self.size = [0, 0]
        self.count = 0
        self.visible = True


class Player():
    def __init__(self, pinfo):
        self.info = pinfo
        self.velocity = [0, 0]
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
            if self.info.count == self.freeze_time:
                self.switchState(PLAYERSTATIC)
            else:
                self.info.count = self.info.count + 1
            if self.signal == ATTACKED:
                self.switchState(PLAYERATTACKED)
            elif self.signal == DIE:
                self.switchState(PLAYERDEAD)
        elif self.info.state == PLAYERDEAD:
            pass

    # 单独处理正在发起技能的状态
    def skillstate(self, n):
        if self.info.count == int(self.max_count / 2):
            self.actSkill(n)
            self.skill_time[n - 1] = Et.fresh_time - 10 / fps
        elif self.info.count == self.max_count - 1:
            self.switchState(PLAYERSTATIC)
        if self.signal == ATTACKED:
            self.switchState(PLAYERATTACKED)
        elif self.signal == DIE:
            self.switchState(PLAYERDEAD)
        self.info.count = self.info.count + 1

    # 状态转换，计数置零
    def switchState(self, state):
        self.info.count = 0
        self.info.state = state

    # 发起不同的技能，新技能在此添加
    def actSkill(self, n):
        skill_type = self.skill_type[n - 1]
        if skill_type in [SKILLBALLSTRAIGHT, SKILLBALLSINUS, SKILLBALLCIRCLE, SKILLBLACKHOLE, SKILLHOOK]:
            new_skill = self.releaseBall(skill_type, n - 1)
            self.skill_list[n - 1].append(new_skill)
        elif skill_type == SKILLRETURN:
            if self.return_released == True:
                self.info.site = self.return_site[:]
            else:
                self.return_site = self.info.site[:]
            self.return_released = not self.return_released
        elif skill_type in [SKILLBOMB, SKILLAIM]:
            if not self.skill_list[n - 1]:
                new_skill = self.releaseBall(skill_type, n - 1)
                self.skill_list[n - 1].append(new_skill)
            else:
                self.skill_list[n - 1][0].setOff()
        elif skill_type == SKILLBALLRETURN:
            if not self.skill_list[n - 1]:
                for direction in [MOVELEFT, MOVERIGHT, MOVEUP, MOVEDOWN, MOVEUPLEFT, MOVEUPRIGHT, MOVEDOWNLEFT,
                                  MOVEDOWNRIGHT]:
                    new_skill = self.releaseBall(SKILLBALLRETURN, n - 1)
                    new_skill.direction = direction
                    self.skill_list[n - 1].append(new_skill)
            else:
                for ball in self.skill_list[n - 1]:
                    ball.returning = True
                    '''
        elif skill_type == SKILLBACKFIRE:
            new_skill = self.releaseBall(skill_type,n-1)
            if len(self.skill_list[n - 1]):
                self.skill_list[n - 1].append(new_skill)
            else:
                self.skill_list[n - 1].append(new_skill)
                #此处加载几个点的坐标
                site1 = self.skill_list[n-1][0].site
                site2 = self.skill_list[n-1][1].site
                #此处在中间的敌人被攻击，遍历
                for enemy in self.game.enemy_list:

                self.skill_list[n - 1][0].delflag = True
                '''

    # 专门用于扔出实体球的技能，n选择球轨迹
    def releaseBall(self, skill_type, n):
        new_skill = None
        if skill_type == SKILLBALLSTRAIGHT:
            temp = Skill.SkillInfo()
            Et.Sk_info.append(temp)
            new_skill = Skill.SkillBallStraight(temp)
            new_skill.resource = Et.R_sk[n]
        elif skill_type == SKILLBALLSINUS:
            temp = Skill.SkillInfo()
            Et.Sk_info.append(temp)
            new_skill = Skill.SkillBallSinus(temp)
            new_skill.resource = Et.R_sk[n]
        elif skill_type == SKILLBALLCIRCLE:
            temp = Skill.SkillInfo()
            Et.Sk_info.append(temp)
            new_skill = Skill.SkillBallCircle(temp)
            new_skill.resource = Et.R_sk[n]
        elif skill_type == SKILLBLACKHOLE:
            temp = Skill.SkillInfo()
            Et.Sk_info.append(temp)
            new_skill = Skill.SkillBlackHole(temp)
            new_skill.resource = Et.R_sk[n]  ##############需要修改资源#######################
        elif skill_type == SKILLHOOK:
            temp = Skill.SkillInfo()
            Et.Sk_info.append(temp)
            new_skill = Skill.SkillHook(temp)
            new_skill.resource = Et.R_sk[n]
        elif skill_type == SKILLBOMB:
            temp = Skill.SkillInfo()
            Et.Sk_info.append(temp)
            new_skill = Skill.SkillBomb(temp)
            new_skill.resource = Et.R_sk[0]  ##############需要修改资源#######################
        elif skill_type == SKILLAIM:
            temp = Skill.SkillInfo()
            Et.Sk_info.append(temp)
            new_skill = Skill.SkillAim(temp)
            new_skill.resource = Et.R_sk[0]  ##############需要修改资源#######################
        elif skill_type == SKILLKEKKAI:
            temp = Skill.SkillInfo()
            Et.Sk_info.append(temp)
            new_skill = Skill.SkillKekkai(temp)
            new_skill.resource = Et.R_sk[0]  ##############需要修改资源#######################
        elif skill_type == SKILLBALLRETURN:
            temp = Skill.SkillInfo()
            Et.Sk_info.append(temp)
            new_skill = Skill.SkillBallReturn(temp)
            new_skill.resource = Et.R_sk[0]
        elif skill_type == SKILLBACKFIRE:  # 我的backfire
            temp = Skill.SkillInfo()
            Et.Sk_info.append(temp)
            new_skill = Skill.SkillBackFire(temp)
            new_skill.resource = Et.R_sk[0]
        new_skill.game = self.game
        new_skill.init_site = self.info.site[:]
        new_skill.init_time = Et.fresh_time
        new_skill.caster = self
        new_skill.direction = self.direction
        new_skill.info.site = self.info.site[:]
        new_skill.info.size = new_skill.resource.size
        new_skill.damage = new_skill.resource.damage
        new_skill.duration = new_skill.resource.duration
        self.game.skill_list.append(new_skill)
        return new_skill

    def move(self):
        for i in range(0, 4):
            if self.movable[i] & (Et.I_ctr.p1_key[direct_list[i]] == True):
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
