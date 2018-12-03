#
#   人物类
#

from define import *
import extern
import pygame
from pygame.locals import *
from math import pow

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
        self.load()

# 根据人物类型与位置的贴图函数
    def player_blit(self):
        extern.singleplayer_background_pic.blit(extern.singleplayer_player_pic_static,
        (int(self.site[0][0]+self.size[0]/2),int(self.site[0][1]+self.size[1]/2)))
    
    def player_update_blit(self,n):
        if n==0:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_player_pic_static,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==1:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_player_pic_move1,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==2:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_player_pic_move2,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
        elif n==3:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_player_pic_attack1,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))  
        elif n==4:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_player_pic_attack2,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2))) 
        elif n==5:
            extern.singleplayer_background_pic_temp.blit(extern.singleplayer_player_pic_attacked,
            (int(self.site[0]-self.size[0]/2),int(self.site[1]-self.size[1]/2)))
              

# 状态更新,有限状态机,每个不同角色单独实现
    def update(self):
        if self.state==PLAYERSTATIC:
            self.player_update_blit(0)
            if self.signal == None:
                pass
            elif ((self.signal<8) & (self.signal>-1)):
                self.state=PLAYERMOVE
                self.count=0
            elif self.signal==ATTACKED:
                self.state=PLAYERATTACKED
                self.count=0
        elif self.state==PLAYERMOVE:
            if self.signal==None:
                self.state=PLAYERSTATIC
                self.player_update_blit(0)
            elif ((self.signal<8) & (self.signal>-1)):
                self.count=(self.count+1) % 6
                self.move()
                self.player_update_blit((self.count>2)+1)
            elif self.signal==ATTACKED:
                self.state=PLAYERATTACKED
                self.count=0


# 事实上的构造函数,init里面只是声明一下变量,之所以不赋值,是因为这些值
# 可能要从文件里读取或者是根据游戏设置而定
    def load(self):
        self.size=extern.singleplayer_playersize
        self.count=0
        self.velocity=extern.singleplayer_player_velocity
        self.movex=[0,0,-1,1,-1,1,-1,1]
        self.movex=[self.velocity[0]*x for x in self.movex]
        self.movey=[-1,1,0,0,-1,-1,1,1]
        self.movey=[self.velocity[1]*y for y in self.movey]

    def move(self):
        if self.movable:
            self.site[0]=self.site[0]+self.movex[self.signal]
            if self.site[0]>extern.singleplayer_background_size[0]-int(self.size[0]/2):
                self.site[0]=extern.singleplayer_background_size[0]-int(self.size[0]/2)
            if self.site[0]<int(self.size[0]/2):
                self.site[0]=int(self.size[0]/2)
            self.site[1]=self.site[1]+self.movey[self.signal]
            if self.site[1]>extern.singleplayer_background_size[1]-int(self.size[1]/2):
                self.site[1]=extern.singleplayer_background_size[1]-int(self.size[1]/2)
            if self.site[1]<int(self.size[1]/2):
                self.site[1]=int(self.size[1]/2)


# 键盘侠类,继承自Player类
class KeyBoardMan(Player):
    def __init__(self):
        super(KeyBoardMan,self).__init__()
        pass
