#
#   人物类
#

from define import *
import extern
import pygame
from pygame.locals import *
from math import pow
import Item

class Player():
    def __init__(self):
        self.site='人物位置(二维)'
        self.max_life='人物最大生命值'
        self.life_value='人物生命值'
        self.power='攻击力'
        self.attack_range='射程'
        self.velocity='速度'
        self.state=PLAYERSTATIC
        self.movable=True
        self.direction='人物朝向'
        self.pic_direction='贴图朝向'
        self.signal=None
        self.size='人物的大小'
        self.game='当前游戏指针'
        self.count='小状态计数器'
        self.skill1type='技能一类型'
        self.skill1time='技能一上次发动的时间'
        self.skill1_cd='技能一冷却时间'
        self.skill2type='技能二类型'
        self.skill2time='技能二上次发动的时间'
        self.skill2_cd='技能二冷却时间'
        self.skill3type='技能三类型'
        self.skill3time='技能三上次发动的时间'
        self.skill3_cd='技能三冷却时间'
        self.skill_direction='技能方向'
        self.freezetime='被攻击冻结时间'
        self.return_x='回归位置技能记录位置'
        self.return_y='回归位置技能记录位置'
        self.return_released='是否释放了回归位置技能'
        self.attacked_skill_list=[]
        self.load()
    
    #贴图
    def player_update_blit(self,n):
        if self.direction==MOVEUPRIGHT or self.direction==MOVERIGHT or self.direction==MOVEDOWNRIGHT:
            self.pic_direction=MOVERIGHT
        elif self.direction==MOVEUPLEFT or self.direction==MOVELEFT or self.direction==MOVEDOWNLEFT:
            self.pic_direction=MOVELEFT
        picname=None
        if n==0:
            picname=extern.character_resource.pic_static1
        elif n==1:
            picname=extern.character_resource.pic_static2
        elif n==2:
            picname=extern.character_resource.pic_static3
        elif n==3:
            picname=extern.character_resource.pic_move1
        elif n==4:
            picname=extern.character_resource.pic_move2
        elif n==5:
            picname=extern.character_resource.pic_move3
        elif n==6:
            picname=extern.character_resource.pic_attack1 
        elif n==7:
            picname=extern.character_resource.pic_attack2
        elif n==8:
            picname=extern.character_resource.pic_attack3
        elif n==9:
            picname=extern.character_resource.pic_attacked1
        elif n==10:
            picname=extern.character_resource.pic_attacked2
        elif n==11:
            picname=extern.character_resource.pic_attacked3
        elif n==12:
            picname=extern.character_resource.pic_dead1
        if self.pic_direction==MOVELEFT:
            extern.singleplayergame_resource.pic_temp.blit(picname[1],
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        else :
            extern.singleplayergame_resource.pic_temp.blit(picname[0],
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))


# 状态更新,有限状态机,每个不同角色单独实现
    def update(self):
        if self.state==PLAYERSTATIC:
            if self.signal == None:
                pass
            elif ((self.signal<8) & (self.signal>-1)):
                self.direction=self.signal
                self.switchState(PLAYERMOVE)
            elif self.signal==ATTACKED:
                self.switchState(PLAYERATTACKED)
            elif self.signal==SKILL1:
                if ((extern.last_fresh_time-self.skill1time)>self.skill1_cd):
                    self.switchState(PLAYERSKILL1)
            elif self.signal==SKILL2:
                if ((extern.last_fresh_time-self.skill1time)>self.skill2_cd):
                    self.switchState(PLAYERSKILL2)
            elif self.signal==SKILL3:
                if ((extern.last_fresh_time-self.skill1time)>self.skill3_cd):
                    self.switchState(PLAYERSKILL3)
            elif self.signal==DIE:
                self.switchState(PLAYERDEAD)
            self.count=(self.count+1)%12
            self.showPic(12,0,1,2)
        elif self.state==PLAYERMOVE:
            if self.signal==None:
                self.switchState(PLAYERSTATIC)
            elif ((self.signal<8) & (self.signal>-1)):
                self.direction=self.signal
                self.count=(self.count+1) % 12
                self.move()
            elif self.signal==ATTACKED:
                self.switchState(PLAYERATTACKED)
            elif self.signal==SKILL1:
                if ((extern.last_fresh_time-self.skill1time)>self.skill1_cd):
                    self.switchState(PLAYERSKILL1)
            elif self.signal==SKILL2:
                if ((extern.last_fresh_time-self.skill2time)>self.skill2_cd):
                    self.switchState(PLAYERSKILL2)
            elif self.signal==SKILL3:
                if ((extern.last_fresh_time-self.skill3time)>self.skill3_cd):
                    self.switchState(PLAYERSKILL3)
            elif self.signal==DIE:
                self.switchState(PLAYERDEAD)
            self.showPic(12,3,4,5)
        elif self.state==PLAYERSKILL1:
            self.skillstate(1)
        elif self.state==PLAYERSKILL2:
            self.skillstate(2)
        elif self.state==PLAYERSKILL3:
            self.skillstate(3)
        elif self.state==PLAYERATTACKED:
            if self.count==self.freezetime:
                self.switchState(PLAYERSTATIC)
            else:
                self.count=self.count+1
            if self.signal==ATTACKED:
                self.switchState(PLAYERATTACKED)
            elif self.signal==DIE:
                self.switchState(PLAYERDEAD)
            self.showPic(self.freezetime,9,10,11)
        elif self.state==PLAYERDEAD:
            self.player_update_blit(12)

    #单独处理正在发起技能的状态
    def skillstate(self,n):
        if self.count==6:
            if n==1:
                self.actSkill(self.skill1type)
                self.skill1time=extern.last_fresh_time-10/fps
            elif n==2:
                self.actSkill(self.skill2type)
                self.skill2time=extern.last_fresh_time-10/fps
            elif n==3:
                self.actSkill(self.skill3type)
                self.skill3time=extern.last_fresh_time-10/fps
        elif self.count==12:
            self.switchState(PLAYERSTATIC)
        if self.signal==ATTACKED:
            self.switchState(PLAYERATTACKED)
        elif self.signal==DIE:
            self.switchState(PLAYERDEAD)
        self.count=self.count+1
        self.showPic(12,6,7,8)

    #状态转换，计数置零
    def switchState(self,state):
        self.count=0
        self.state=state

    #根据当前count显示player_update_blit中编号为n1,n2,n3的三帧图
    def showPic(self,maxcount,n1,n2,n3):
        if self.count<maxcount/3:
            self.player_update_blit(n1)
        elif self.count<maxcount*2/3:
            self.player_update_blit(n2)
        else:
            self.player_update_blit(n3)

    #发起不同的技能，新技能在此添加
    def actSkill(self,skilltype):
        if skilltype==SKILLBALLSTRAIGHT:
            self.releaseBall(1)
        elif skilltype==SKILLBALLSINUS:
            self.releaseBall(2)
        elif skilltype==SKILLBALLCIRCLE:
            self.releaseBall(3)
        elif skilltype==SKILLRETURN:
            if self.return_released==True:
                self.site[0]=self.return_x
                self.site[1]=self.return_y
            else:
                self.return_x=self.site[0]
                self.return_y=self.site[1]
            self.return_released=not self.return_released

    #专门用于扔出实体球的技能，n选择球轨迹
    def releaseBall(self,n):
        tempskill=Item.Skill()
        tempskill.game=self.game
        if n==1:
            tempskill.resource=extern.skill_resource
        elif n==2:
            tempskill.resource=extern.skill_resource2
        elif n==3:
            tempskill.resource=extern.skill_resource3
        tempskill.initsite=self.site[:]
        tempskill.inittime=extern.last_fresh_time
        tempskill.caster=self
        tempskill.direction=self.skill_direction
        tempskill.site=self.site[:]
        tempskill.size=tempskill.resource.size
        tempskill.damage=tempskill.resource.damage
        self.game.skill_list.append(tempskill)

# 事实上的构造函数,init里面只是声明一下变量,之所以不赋值,是因为这些值
# 可能要从文件里读取或者是根据游戏设置而定
    def load(self):
        self.size=extern.character_resource.size
        self.count=0
        self.velocity=extern.character_resource.velocity
        self.movex=[self.velocity[0]*x for x in movex]
        self.movey=[self.velocity[1]*y for y in movey]
        self.direction=MOVERIGHT
        self.freezetime=extern.character_resource.freezetime
        self.return_released=False
        ###以下暂时使用，请改入初始化###
        self.skill1type=SKILLRETURN
        self.skill2type=SKILLBALLSINUS
        self.skill3type=SKILLBALLCIRCLE
        ###以上暂时使用，请改入初始化###

    def move(self):
        if self.movable:
            self.site[0]=self.site[0]+self.movex[self.signal]
            if self.site[0]>(extern.singleplayergame_resource.size[0]-int(self.size[0]/2)):
                self.site[0]=extern.singleplayergame_resource.size[0]-int(self.size[0]/2)
            if self.site[0]<int(self.size[0]/2):
                self.site[0]=int(self.size[0]/2)
            self.site[1]=self.site[1]+self.movey[self.signal]
            if self.site[1]>(extern.singleplayergame_resource.size[1]-int(self.size[1]/2)):
                self.site[1]=extern.singleplayergame_resource.size[1]-int(self.size[1]/2)
            if self.site[1]<int(self.size[1]/2):
                self.site[1]=int(self.size[1]/2)


# 键盘侠类,继承自Player类
class KeyBoardMan(Player):
    def __init__(self):
        super(KeyBoardMan,self).__init__()
        pass
