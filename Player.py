#
#   人物类
#

from Define import *
import Extern as Et
import Skill
#import pygame
#from pygame.locals import *

class PlayerInfo():
    def __init__(self):##############需要加载资源#######################
        self.site = [200,400]
        self.max_life = 0
        self.life_value = 0
        self.state = PLAYERSTATIC
        self.pic_direction = RIGHT
        self.size = [0,0]
        self.count = 0
        self.visible = True

class Player():
    def __init__(self,pinfo):##############需要加载资源#######################
        self.info = pinfo
        self.velocity = [0, 0]
        self.movable = [True,True,True,True]    #上下左右方向是否可移动
        self.game = None    #游戏指针
        self.skill_time = [0,0,0]   #技能123的上次发动时间
        self.skill_cd = [0,0,0] #技能123的冷却时间
        self.freeze_time = 0    #被攻击后僵直时间
        self.signal = None
        self.direction = MOVERIGHT
        self.skill_type = [0,0,0]
        self.max_count = 12
        self.return_site = [0,0]
        self.return_released = False
        self.skill_list = [[],[],[]]

# 状态更新,有限状态机,每个不同角色单独实现
    def update(self):
        if self.info.state==PLAYERSTATIC:
            if self.signal == None:
                pass
            elif ((self.signal<8) & (self.signal>-1)):
                self.direction=self.signal
                self.switchState(PLAYERMOVE)
            elif self.signal==ATTACKED:
                self.switchState(PLAYERATTACKED)
            elif self.signal==SKILL1:
                if ((Et.fresh_time-self.skill_time[0])>self.skill_cd[0]):
                    self.switchState(PLAYERSKILL1)
            elif self.signal==SKILL2:
                if ((Et.fresh_time-self.skill_time[1])>self.skill_cd[1]):
                    self.switchState(PLAYERSKILL2)
            elif self.signal==SKILL3:
                if ((Et.fresh_time-self.skill_time[2])>self.skill_cd[2]):
                    self.switchState(PLAYERSKILL3)
            elif self.signal==DIE:
                self.switchState(PLAYERDEAD)
            self.info.count=(self.info.count+1)%self.max_count
        elif self.info.state==PLAYERMOVE:
            if self.signal==None:
                self.switchState(PLAYERSTATIC)
            elif ((self.signal<8) & (self.signal>-1)):
                self.direction=self.signal
                self.info.count=(self.info.count+1)%self.max_count
                self.move()
            elif self.signal==ATTACKED:
                self.switchState(PLAYERATTACKED)
            elif self.signal==SKILL1:
                if ((Et.fresh_time-self.skill_time[0])>self.skill_cd[0]):
                    self.switchState(PLAYERSKILL1)
            elif self.signal==SKILL2:
                if ((Et.fresh_time-self.skill_time[1])>self.skill_cd[1]):
                    self.switchState(PLAYERSKILL2)
            elif self.signal==SKILL3:
                if ((Et.fresh_time-self.skill_time[2])>self.skill_cd[2]):
                    self.switchState(PLAYERSKILL3)
            elif self.signal==DIE:
                self.switchState(PLAYERDEAD)
        elif self.info.state==PLAYERSKILL1:
            self.skillstate(1)
        elif self.info.state==PLAYERSKILL2:
            self.skillstate(2)
        elif self.info.state==PLAYERSKILL3:
            self.skillstate(3)
        elif self.info.state==PLAYERATTACKED:
            if self.info.count==self.freeze_time:
                self.switchState(PLAYERSTATIC)
            else:
                self.info.count=self.info.count+1
            if self.signal==ATTACKED:
                self.switchState(PLAYERATTACKED)
            elif self.signal==DIE:
                self.switchState(PLAYERDEAD)
        elif self.info.state==PLAYERDEAD:
            pass

    #单独处理正在发起技能的状态
    def skillstate(self,n):
        if self.info.count==int(self.max_count/2):
            self.actSkill(n)
            self.skill_time[n-1]=Et.fresh_time-10/fps
        elif self.info.count==self.max_count:
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

    #发起不同的技能，新技能在此添加
    def actSkill(self,n):
        skill_type=self.skill_type[n-1]
        if skill_type==SKILLBALLSTRAIGHT or skill_type==SKILLBALLSINUS or skill_type==SKILLBALLCIRCLE:
            new_skill=self.releaseBall(skill_type)
        elif skill_type==SKILLRETURN:
            if self.return_released==True:
                self.info.site=self.return_site[:]
            else:
                self.return_site=self.info.site[:]
            self.return_released=not self.return_released
            new_skill=None
        self.skill_list[n-1].append(new_skill)

    #专门用于扔出实体球的技能，n选择球轨迹
    def releaseBall(self,skill_type):
        if skill_type==SKILLBALLSTRAIGHT:
            new_skill=Skill.SkillBallStraight()
            #new_skill.resource=Et.skill_resource##############需要加载资源#######################
        elif skill_type==SKILLBALLSINUS:
            new_skill=Skill.SkillBallSinus()
            #new_skill.resource=Et.skill_resource2##############需要加载资源#######################
        elif skill_type==SKILLBALLCIRCLE:
            new_skill=Skill.SkillBallCircle()
            #new_skill.resource=Et.skill_resource3##############需要加载资源#######################
        new_skill.game=self.game
        new_skill.init_site=self.info.site[:]
        new_skill.init_time=Et.fresh_time
        new_skill.caster=self
        new_skill.direction=self.direction
        new_skill.info.site=self.info.site[:]
        #new_skill.info.size=tempskill.resource.size##############需要加载资源#######################
        #new_skill.damage=new_skill.resource.damage##############需要加载资源#######################
        self.game.skill_list.append(new_skill)
        return new_skill

# 事实上的构造函数,init里面只是声明一下变量,之所以不赋值,是因为这些值
# 可能要从文件里读取或者是根据游戏设置而定
        '''
    def load(self):
        self.size=Et.character_resource.size
        self.info.count=0
        self.velocity=Et.character_resource.velocity
        self.movex=[self.velocity[0]*x for x in movex]
        self.movey=[self.velocity[1]*y for y in movey]
        self.direction=MOVERIGHT
        self.freezetime=Et.character_resource.freezetime
        self.return_released=False
        ###以下暂时使用，请改入初始化###
        self.skill1type=SKILLRETURN
        self.skill2type=SKILLBALLSINUS
        self.skill3type=SKILLBALLCIRCLE
        ###以上暂时使用，请改入初始化###
        '''

    def move(self):##############需要加载资源#######################
        if self.movable:
            self.info.site[0]=self.info.site[0]+self.movex[self.signal]
            if self.info.site[0]>(Et.singleplayergame_resource.size[0]-int(self.size[0]/2)):
                self.info.site[0]=Et.singleplayergame_resource.size[0]-int(self.size[0]/2)
            if self.info.site[0]<int(self.size[0]/2):
                self.info.site[0]=int(self.size[0]/2)
            self.info.site[1]=self.info.site[1]+self.movey[self.signal]
            if self.info.site[1]>(Et.singleplayergame_resource.size[1]-int(self.size[1]/2)):
                self.info.site[1]=Et.singleplayergame_resource.size[1]-int(self.size[1]/2)
            if self.info.site[1]<int(self.size[1]/2):
                self.info.site[1]=int(self.size[1]/2)