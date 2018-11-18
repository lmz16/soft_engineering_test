#
#   游戏类
#

from define import *
import extern
import Player
import Item

import pygame
import json
from pygame.locals import *

class Single_player_game():
    def __init__(self):
        self.single_player=Player.Player()
    # 调用初始化函数,加载关卡信息,敌人数量与类型,地图资源
        self.enemy_list=[]
        self.background="背景地图的图片对象"
        self.enemypic='敌人的图片'
        self.playerpic='人物的图片'
        self.world='整个游戏地图'
        self.worldsize='整个游戏地图大小'
        self.gameover='游戏是否结束'
        self.load_from_json()
    # 技能列表
        self.skill_list=[]
    # 信号列表,用于暂存未处理的信号
        self.signal_list=[]
    # 键盘状态
        self.keyboardevent=pygame.key.get_pressed()

# 初始化函数,从json文件读入信息
    def load_from_json(self):
        with open (gametestjson,'r') as checkpointinfo:
            checkpoint1=json.load(checkpointinfo)
            for enemysite in checkpoint1[6]:
                self.enemy_list.append(Item.Enemy())
            for count in list(range(1,len(self.enemy_list)+1)):
                self.enemy_list[count].site=checkpoint1[6][count]
                self.enemy_list[count].size=checkpoint1[4]
            self.worldsize=checkpoint1[1]
            self.playerpic=pygame.image.load(checkpoint1[3]).convert()
            self.enemypic=pygame.image.load(checkpoint1[5]).convert()
            self.background=pygame.image.load(checkpoint1[0]).convert()
            self.single_player.size=checkpoint1[2]
            self.gameover=0


# 攻击判定方法,根据技能列表里的技能判断是否向message_list写入信号
    def attack_judge(self):
        tempplayerskill=[]
        if (len(self.skill_list)==0):
            pass
        else:
            for skill in self.skill_list:
                if (skill.caster==self.single_player):
                    tempplayerskill.append(skill)
                else:
                    if (skill.attack_judge(self.single_player)):
                        self.single_player.signal=SIGNALATTACKED
                        self.single_player.life_value=self.single_player.life_value-skill.damage
                        if (skill.last==0):
                            del skill
            if (len(tempplayerskill)==0):
                pass
            else:
                for skill in tempplayerskill:
                    for enemy in self.enemylist:
                        if (skill.attack_judge(enemy)):
                            enemy.signal=SIGNALATTACKED
                            enemy.life_value=enemy.life_value-skill.damage
                            if (skill.last==0):
                                del skill

# 移动判定方法,判定对象是否可以移动,将结果写入成员对象的movable属性
    def move_judge(self,tempsignal):
        tempsite=tempsignal.receiver.site
        tempsize=tempsignal.receiver.size
        tempsignal.receiver.movable=True
        tempsignal.receiver.signal=SIGNALMOVE
        tempmoveflag=[True,True]
        for enemy in self.enemy_list:
            if (tempsignal.type==MOVEUP):
                if ((abs(enemy.site[1]-tempsite[1]-(enemy.size[1]+tempsize[1])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[0]-tempsite[0])<(enemy.size[0]+tempsize[0])/2)):
                    tempsignal.receiver.movable=False
                    break
            elif (tempsignal.receiver.type==MOVEDOWN):
                if ((abs(-enemy.site[1]+tempsite[1]-(enemy.size[1]+tempsize[1])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[0]-tempsite[0])<(enemy.size[0]+tempsize[0])/2)):
                    tempsignal.receiver.movable=False
                    break
            elif (tempsignal.receiver.type==MOVELEFT):
                if ((abs(enemy.site[0]-tempsite[0]-(enemy.size[0]+tempsize[0])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[1]-tempsite[1])<(enemy.size[1]+tempsize[1])/2)):
                    tempsignal.receiver.movable=False
                    break
            elif (tempsignal.receiver.type==MOVERIGHT):
                if ((abs(-enemy.site[0]+tempsite[0]-(enemy.size[0]+tempsize[0])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[1]-tempsite[1])<(enemy.size[1]+tempsize[1])/2)):
                    tempsignal.receiver.movable=False
                    break
            elif (tempsignal.receiver.type==MOVEUPLEFT):
                if ((abs(enemy.site[1]-tempsite[1]-(enemy.size[1]+tempsize[1])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[0]-tempsite[0])<(enemy.size[0]+tempsize[0])/2)):
                    tempmoveflag[1]=False
                if ((abs(enemy.site[0]-tempsite[0]-(enemy.size[0]+tempsize[0])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[1]-tempsite[1])<(enemy.size[1]+tempsize[1])/2)):
                    tempmoveflag[0]=False
                if (tempmoveflag[1]==False & tempmoveflag[0]==False):
                    break
            elif (tempsignal.receiver.type==MOVEUPRIGHT):
                if ((abs(enemy.site[1]-tempsite[1]-(enemy.size[1]+tempsize[1])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[0]-tempsite[0])<(enemy.size[0]+tempsize[0])/2)):
                    tempmoveflag[1]=False
                if ((abs(-enemy.site[0]+tempsite[0]-(enemy.size[0]+tempsize[0])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[1]-tempsite[1])<(enemy.size[1]+tempsize[1])/2)):
                    tempmoveflag[0]=False
                if (tempmoveflag[1]==False & tempmoveflag[0]==False):
                    break
            elif (tempsignal.receiver.type==MOVEDOWNLEFT):
                if ((abs(-enemy.site[1]+tempsite[1]-(enemy.size[1]+tempsize[1])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[0]-tempsite[0])<(enemy.size[0]+tempsize[0])/2)):
                    tempmoveflag[1]=False
                if ((abs(enemy.site[0]-tempsite[0]-(enemy.size[0]+tempsize[0])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[1]-tempsite[1])<(enemy.size[1]+tempsize[1])/2)):
                    tempmoveflag[0]=False
                if (tempmoveflag[1]==False & tempmoveflag[0]==False):
                    break
            elif (tempsignal.receiver.type==MOVEDOWNRIGHT):
                if ((abs(-enemy.site[1]+tempsite[1]-(enemy.size[1]+tempsize[1])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[0]-tempsite[0])<(enemy.size[0]+tempsize[0])/2)):
                    tempmoveflag[1]=False
                if ((abs(-enemy.site[0]+tempsite[0]-(enemy.size[0]+tempsize[0])/2)<COLLISIONTHRESHOLD) &  \
                (abs(enemy.site[1]-tempsite[1])<(enemy.size[1]+tempsize[1])/2)):
                    tempmoveflag[0]=False
                if (tempmoveflag[1]==False & tempmoveflag[0]==False):
                    break
        if (tempsignal.receiver.type==MOVEUPLEFT):
            if (tempmoveflag[1]==False & tempmoveflag[0]==False):
                tempsignal.receiver.movable=False
            elif (tempmoveflag[1]==False):
                tempsignal.receiver.movable=True
                tempsignal.receiver.type==MOVELEFT
            elif (tempmoveflag[0]==False):
                tempsignal.receiver.movable=True
                tempsignal.receiver.type==MOVEUP
        elif (tempsignal.receiver.type==MOVEUPRIGHT):
            if (tempmoveflag[1]==False & tempmoveflag[0]==False):
                tempsignal.receiver.movable=False
            elif (tempmoveflag[1]==False):
                tempsignal.receiver.movable=True
                tempsignal.receiver.type==MOVERIGHT
            elif (tempmoveflag[0]==False):
                tempsignal.receiver.movable=True
                tempsignal.receiver.type==MOVEUP
        elif (tempsignal.receiver.type==MOVEDOWNLEFT):
            if (tempmoveflag[1]==False & tempmoveflag[0]==False):
                tempsignal.receiver.movable=False
            elif (tempmoveflag[1]==False):
                tempsignal.receiver.movable=True
                tempsignal.receiver.type==MOVELEFT
            elif (tempmoveflag[0]==False):
                tempsignal.receiver.movable=True
                tempsignal.receiver.type==MOVEDOWN
        elif (tempsignal.receiver.type==MOVEDOWNRIGHT):
            if (tempmoveflag[1]==False & tempmoveflag[0]==False):
                tempsignal.receiver.movable=False
            elif (tempmoveflag[1]==False):
                tempsignal.receiver.movable=True
                tempsignal.receiver.type==MOVERIGHT
            elif (tempmoveflag[0]==False):
                tempsignal.receiver.movable=True
                tempsignal.receiver.type==MOVEDOWN


# 信号处理函数,解决信号冲突,向每个对象发送信号
    def message_translate(self):
        pass

# 游戏画面与状态更新
    def game_update(self):
        for skill in skill_list:
            if ():#skill寿命到了的话
                del skill
        for enemy in enemylist:
            if (enemy.state==ENEMYDEAD):
                del enemy
        if (self.single_player.state==PLAYERDEAD):
            self.gameover=1
        if (len(self.enemylist)==0)
            self.gameover=1

# 信号类
class Signal():
    def __init__(type,receiver):
        self.type=type
        self.receiver=receiver
