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
        self.life_value='人物生命值'
        self.power='攻击力'
        self.mana='魔法值'
        self.attack_range='射程'
        self.velocity='速度'
        self.state=PLAYERSTATIC
        self.movable=True
        self.direction='人物朝向'
        self.signal=None
        self.size='人物的大小'
        self.game='当前游戏指针'
        self.count='小状态计数器'
        self.skill1time='技能一上次发动的时间'
        self.skill1_cd='技能一冷却时间'
        self.skill_direction='技能方向'
        self.load()
    
    def player_update_blit(self,n):
        if n==0:
            extern.singleplayergame_resource.pic_temp.blit(extern.character_resource.pic_static,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==1:
            extern.singleplayergame_resource.pic_temp.blit(extern.character_resource.pic_move1,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==2:
            extern.singleplayergame_resource.pic_temp.blit(extern.character_resource.pic_move2,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==3:
            extern.singleplayergame_resource.pic_temp.blit(extern.character_resource.pic_attack1,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))  
        elif n==4:
            extern.singleplayergame_resource.pic_temp.blit(extern.character_resource.pic_attack2,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2))) 
        elif n==5:
            extern.singleplayergame_resource.pic_temp.blit(extern.character_resource.pic_attacked,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
              

# 状态更新,有限状态机,每个不同角色单独实现
    def update(self):
        if self.state==PLAYERSTATIC:
            if self.signal == None:
                pass
            elif ((self.signal<8) & (self.signal>-1)):
                self.direction=self.signal
                self.state=PLAYERMOVE
                self.count=0
            elif self.signal==ATTACKED:
                self.state=PLAYERATTACKED
                self.count=0
            elif self.signal==SKILL1:
                self.state=PLAYERSKILL1
                self.count=0
            self.player_update_blit(0)
        elif self.state==PLAYERMOVE:
            if self.signal==None:
                self.state=PLAYERSTATIC
            elif ((self.signal<8) & (self.signal>-1)):
                self.direction=self.signal
                self.count=(self.count+1) % 6
                self.move()
            elif self.signal==ATTACKED:
                self.state=PLAYERATTACKED
                self.count=0
            elif self.signal==SKILL1:
                self.state=PLAYERSKILL1
                self.count=0
            self.player_update_blit((self.count>2)+1)
        elif self.state==PLAYERSKILL1:
            if ((extern.last_fresh_time-self.skill1time)>self.skill1_cd):
                if self.count==0:
                    tempskill=Item.Skill()
                    tempskill.kind=1
                    tempskill.inittime=extern.last_fresh_time
                    tempskill.caster=self
                    tempskill.direction=self.skill_direction
                    tempskill.site=self.site[:]
                    tempskill.size=extern.skill_resource.size
                    tempskill.damage=extern.skill_resource.damage
                    self.game.skill_list.append(tempskill)
                    self.player_update_blit(3)
                elif self.count==10:
                    self.count=0
                    self.state=PLAYERSTATIC
                    self.skill1time=extern.last_fresh_time-10/fps
                    self.player_update_blit(4)
                else:
                    self.player_update_blit((self.count>5)+3)
                self.count=self.count+1
            else:
                self.player_update_blit(0)



# 事实上的构造函数,init里面只是声明一下变量,之所以不赋值,是因为这些值
# 可能要从文件里读取或者是根据游戏设置而定
    def load(self):
        self.size=extern.character_resource.size
        self.count=0
        self.velocity=extern.character_resource.velocity
        self.movex=[self.velocity[0]*x for x in movex]
        self.movey=[self.velocity[1]*y for y in movey]
        self.direction=MOVERIGHT

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
