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
        #↓这里添加picture direction
        self.pic_direction='贴图朝向'
        self.signal=None
        self.size='人物的大小'
        self.game='当前游戏指针'
        self.count='小状态计数器'
        self.skill1time='技能一上次发动的时间'
        self.skill1_cd='技能一冷却时间'
        self.skill2time='技能二上次发动的时间'
        self.skill2_cd='技能二冷却时间'
        self.skill3time='技能三上次发动的时间'
        self.skill3_cd='技能三冷却时间'
        self.skill_direction='技能方向'
        self.freezetime='被攻击冻结时间'
        self.load()
    
    def player_update_blit(self,n):
        #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        #增加了pic_direction，用来反转人物图像
        if self.direction==MOVEUPRIGHT or self.direction==MOVERIGHT or self.direction==MOVEDOWNRIGHT:
            self.pic_direction=MOVERIGHT
        elif self.direction==MOVEUPLEFT or self.direction==MOVELEFT or self.direction==MOVEDOWNLEFT:
            self.pic_direction=MOVELEFT
        #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        #为了增加静止、攻击、被攻击、移动图像接口为三张，将n的值设置成了0到12（dead）取值
        if n==0:
            pic=extern.character_resource.pic_static1
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==1:
            pic=extern.character_resource.pic_static2
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==2:
            pic=extern.character_resource.pic_static3
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==3:
            pic=extern.character_resource.pic_move1
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==4:
            pic=extern.character_resource.pic_move2
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==5:
            pic=extern.character_resource.pic_move3
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==6:
            pic=extern.character_resource.pic_attack1
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))  
        elif n==7:
            pic=extern.character_resource.pic_attack2
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))   
        elif n==8:
            pic=extern.character_resource.pic_attack3
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2))) 
        elif n==9:
            pic=extern.character_resource.pic_attacked1
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==10:
            pic=extern.character_resource.pic_attacked2
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==11:
            pic=extern.character_resource.pic_attacked3
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==12:
            pic=extern.character_resource.pic_dead
            if self.pic_direction==MOVELEFT:
                pic=pygame.transform.flip(pic,True,False)
            extern.singleplayergame_resource.pic_temp.blit(pic,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        #↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
              

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
                if ((extern.last_fresh_time-self.skill1time)>self.skill1_cd):  #将攻击的弛豫时间判定修改到了这里来，update函数内以下同理
                    self.state=PLAYERSKILL1
                    self.count=0
            elif self.signal==SKILL2:
                if ((extern.last_fresh_time-self.skill2time)>self.skill2_cd):
                    self.state=PLAYERSKILL2
                    self.count=0
            elif self.signal==SKILL3:
                if ((extern.last_fresh_time-self.skill3time)>self.skill3_cd):
                    self.state=PLAYERSKILL3
                    self.count=0
            elif self.signal==ATTACKED:
                self.state=PLAYERATTACKED
                self.count=0
            elif self.signal==DIE:
                self.state=PLAYERDEAD
                self.count=0
            self.count=(self.count+1)%12
            #静止贴图分成了三段。以下同理（攻击、移动等）
            if self.count<4:
                self.player_update_blit(0)
            elif self.count<8:
                self.player_update_blit(1)
            else:
                self.player_update_blit(2)
        elif self.state==PLAYERMOVE:
            if self.signal==None:
                self.state=PLAYERSTATIC
            elif ((self.signal<8) & (self.signal>-1)):
                self.direction=self.signal
                self.count=(self.count+1) % 12
                self.move()
            elif self.signal==ATTACKED:
                self.state=PLAYERATTACKED
                self.count=0
            elif self.signal==SKILL1:
                if ((extern.last_fresh_time-self.skill1time)>self.skill1_cd):
                    self.state=PLAYERSKILL1
                    self.count=0
            elif self.signal==SKILL2:
                if ((extern.last_fresh_time-self.skill2time)>self.skill2_cd):
                    self.state=PLAYERSKILL2
                    self.count=0
            elif self.signal==SKILL3:
                if ((extern.last_fresh_time-self.skill3time)>self.skill3_cd):
                    self.state=PLAYERSKILL3
                    self.count=0
            elif self.signal==DIE:
                self.state=PLAYERDEAD
                self.count=0
            if self.count<4:
                self.player_update_blit(3)
            elif self.count<8:
                self.player_update_blit(4)
            else:
                self.player_update_blit(5)
        elif self.state==PLAYERSKILL1:
            if self.count==6:
                tempskill=Item.Skill()
                tempskill.game=self.game
                tempskill.resource=extern.skill_resource
                tempskill.initsite=self.site[:]
                tempskill.inittime=extern.last_fresh_time
                tempskill.caster=self
                tempskill.direction=self.skill_direction
                tempskill.site=self.site[:]
                tempskill.size=extern.skill_resource.size
                tempskill.damage=extern.skill_resource.damage
                self.game.skill_list.append(tempskill)
            elif self.count==12:
                self.count=0
                self.state=PLAYERSTATIC
                self.skill1time=extern.last_fresh_time-10/fps
            if self.signal==ATTACKED:
                self.state=PLAYERATTACKED
                self.count=0
            elif self.signal==DIE:
                self.state=PLAYERDEAD
                self.count=0
            self.count=self.count+1
            if self.count<4:
                self.player_update_blit(6)
            elif self.count<8:
                self.player_update_blit(7)
            else:
                self.player_update_blit(8)
        elif self.state==PLAYERSKILL2:
            if self.count==6:
                tempskill=Item.Skill()
                tempskill.game=self.game
                tempskill.resource=extern.skill_resource2
                tempskill.initsite=self.site[:]
                tempskill.inittime=extern.last_fresh_time
                tempskill.caster=self
                tempskill.direction=self.skill_direction
                tempskill.site=self.site[:]
                tempskill.size=extern.skill_resource2.size
                tempskill.damage=extern.skill_resource2.damage
                self.game.skill_list.append(tempskill)
            elif self.count==12:
                self.count=0
                self.state=PLAYERSTATIC
                self.skill2time=extern.last_fresh_time-10/fps
            if self.signal==ATTACKED:
                self.state=PLAYERATTACKED
                self.count=0
            elif self.signal==DIE:
                self.state=PLAYERDEAD
                self.count=0
            self.count=self.count+1
            if self.count<4:
                self.player_update_blit(6)
            elif self.count<8:
                self.player_update_blit(7)
            else:
                self.player_update_blit(8)
        elif self.state==PLAYERSKILL3:
            if self.count==6:
                tempskill=Item.Skill()
                tempskill.game=self.game
                tempskill.resource=extern.skill_resource3
                tempskill.initsite=self.site[:]
                tempskill.inittime=extern.last_fresh_time
                tempskill.caster=self
                tempskill.direction=self.skill_direction
                tempskill.site=self.site[:]
                tempskill.size=extern.skill_resource3.size
                tempskill.damage=extern.skill_resource3.damage
                self.game.skill_list.append(tempskill)
            elif self.count==12:
                self.count=0
                self.state=PLAYERSTATIC
                self.skill3time=extern.last_fresh_time-10/fps
            if self.signal==ATTACKED:
                self.state=PLAYERATTACKED
                self.count=0
            elif self.signal==DIE:
                self.state=PLAYERDEAD
                self.count=0
            self.count=self.count+1
            if self.count<4:
                self.player_update_blit(6)
            elif self.count<8:
                self.player_update_blit(7)
            else:
                self.player_update_blit(8)
        elif self.state==PLAYERATTACKED:
            if self.count==self.freezetime:
                self.count=0
                self.state=PLAYERSTATIC
            else:
                self.count=self.count+1
            if self.signal==ATTACKED:
                self.count=0
                self.state=PLAYERATTACKED
            elif self.signal==DIE:
                self.state=PLAYERDEAD
                self.count=0
            if self.count<self.freezetime/3:
                self.player_update_blit(9)
            elif self.count<self.freezetime*2/3:
                self.player_update_blit(10)
            else:
                self.player_update_blit(11)
        elif self.state==PLAYERDEAD:
            self.player_update_blit(12)



# 事实上的构造函数,init里面只是声明一下变量,之所以不赋值,是因为这些值
# 可能要从文件里读取或者是根据游戏设置而定
    def load(self):
        self.size=extern.character_resource.size
        self.count=0
        self.velocity=extern.character_resource.velocity
        self.movex=[self.velocity[0]*x for x in movex]
        self.movey=[self.velocity[1]*y for y in movey]
        self.direction=MOVERIGHT
        self.pic_direction=MOVERIGHT

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
