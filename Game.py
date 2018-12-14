#
#   游戏类
#

from define import *
import extern
import Player
import Item
import copy
import Resource 

import pygame
import json
import time
from pygame.locals import *

class Single_player_game():
    def __init__(self):
        self.single_player='人物'
    # 调用初始化函数,加载关卡信息,敌人数量与类型,地图资源
        self.enemy_list=[]
        self.gameover='游戏是否结束'
        self.load_from_json()
    # 技能列表
        self.skill_list=[]
    # 信号列表,用于暂存未处理的信号
        self.signal_list=[]
    # 障碍物列表
        self.obstacle_list=[]
    # 键盘状态
        self.keyboardevent=pygame.key.get_pressed()

# 初始化函数,从json文件读入信息
    def load_from_json(self):
        extern.gameinterface=pygame.image.load(gameinterface_filename).convert()
        extern.singleplayergame_resource=Resource.RSingleplayergame('Resource/json/singlegame1')
        if extern.single_play_choose2==1:
            extern.character_resource=Resource.RCharacter('Resource/json/jpx')
        elif single_play_choose2==2:
            extern.character_resource=Resource.RCharacter('Resource/json/jpx')
        extern.enemy_resource=Resource.REnemy('Resource/json/enemy1')
        extern.skill_resource=Resource.RSkill('Resource/json/skill1')
        extern.skill_resource2=Resource.RSkill('Resource/json/skill2')
        extern.skill_resource3=Resource.RSkill('Resource/json/skill3')
        for index,location in enumerate(extern.singleplayergame_resource.enemysite):
            tempenemy=Item.Enemy(self)
            tempenemy.site=location
            tempenemy.life_value=extern.enemy_resource.life[index]
            self.enemy_list.append(tempenemy)
        self.single_player=Player.Player()
        self.single_player.site=extern.character_resource.site
        self.single_player.game=self
        self.single_player.skill1time=0
        self.single_player.skill2time=0
        self.single_player.skill3time=0
        self.single_player.skill1_cd=extern.character_resource.skill1_cd
        self.single_player.skill2_cd=extern.character_resource.skill2_cd
        self.single_player.skill3_cd=extern.character_resource.skill3_cd
        self.single_player.skill_direction=MOVERIGHT
        self.single_player.max_life=extern.character_resource.max_life
        self.single_player.max_mana=extern.character_resource.max_mana
        self.gameover=False

# 攻击判定方法,根据技能列表里的技能判断是否向message_list写入信号
    def attack_judge(self):
        for enemy in self.enemy_list:
            enemy.signal=None
        if (len(self.skill_list)==0):
            pass
        else:
            for inx,skill in enumerate(self.skill_list):
                if (skill.caster==self.single_player):
                    for enemy in self.enemy_list:
                        if (skill.attack_judge(enemy)):
                            if skill not in enemy.ignore_skill:
                                enemy.signal=ATTACKED
                                enemy.life_value=enemy.life_value-skill.damage
                                enemy.ignore_skill.append(skill)
                                if (not skill.last):
                                    del self.skill_list[inx]
                                    break
                else:
                    # 技能打到了人物而且人物之前没有被这个技能打到
                    if (skill.attack_judge(self.single_player) & \
                    (skill not in self.single_player.attacked_skill_list)):
                        self.single_player.signal=SIGNALATTACKED
                        self.single_player.life_value=self.single_player.life_value-skill.damage
                        if (skill.last==0):
                            del skill
                        else:
                            #被哪些技能攻击到的列表
                            self.single_player.attacked_skill_list.append(skill)

# 移动判定方法,判定对象是否可以移动,将结果写入成员对象的movable属性
    def move_judge(self,tempsignal):
        tempsite=tempsignal.receiver.site
        tempsize=tempsignal.receiver.size
        tempsignal.receiver.movable=True
        tempmoveflag=[True,True]
        for enemy in self.enemy_list:
            umovable=((abs(-enemy.site[1]+tempsite[1]-(enemy.size[1]+tempsize[1])/2)<COLLISIONTHRESHOLD) &  \
                    (abs(enemy.site[0]-tempsite[0])<(enemy.size[0]+tempsize[0])/2))
            dmovable=((abs(enemy.site[1]-tempsite[1]-(enemy.size[1]+tempsize[1])/2)<COLLISIONTHRESHOLD) &  \
                    (abs(enemy.site[0]-tempsite[0])<(enemy.size[0]+tempsize[0])/2))
            lmovable=((abs(-enemy.site[0]+tempsite[0]-(enemy.size[0]+tempsize[0])/2)<COLLISIONTHRESHOLD) &  \
                    (abs(enemy.site[1]-tempsite[1])<(enemy.size[1]+tempsize[1])/2))
            rmovable=((abs(enemy.site[0]-tempsite[0]-(enemy.size[0]+tempsize[0])/2)<COLLISIONTHRESHOLD) &  \
                    (abs(enemy.site[1]-tempsite[1])<(enemy.size[1]+tempsize[1])/2))
            if (tempsignal.type==MOVEUP):
                if (umovable):
                    tempsignal.receiver.movable=False
                    tempmoveflag=[False,False]
                    break
            elif (tempsignal.type==MOVEDOWN):
                if (dmovable):
                    tempsignal.receiver.movable=False
                    tempmoveflag=[False,False]
                    break
            elif (tempsignal.type==MOVELEFT):
                if (lmovable):
                    tempsignal.receiver.movable=False
                    tempmoveflag=[False,False]
                    break
            elif (tempsignal.type==MOVERIGHT):
                if (rmovable):
                    tempsignal.receiver.movable=False
                    tempmoveflag=[False,False]
                    break
            elif (tempsignal.type==MOVEUPLEFT):
                if (umovable):
                    tempmoveflag[1]=False
                if (lmovable):
                    tempmoveflag[0]=False
                if ((tempmoveflag[1]==False) & (tempmoveflag[0]==False)):
                    break
            elif (tempsignal.type==MOVEUPRIGHT):
                if (umovable):
                    tempmoveflag[1]=False
                if (rmovable):
                    tempmoveflag[0]=False
                if ((tempmoveflag[1]==False) & (tempmoveflag[0]==False)):
                    break
            elif (tempsignal.type==MOVEDOWNLEFT):
                if (dmovable):
                    tempmoveflag[1]=False
                if (lmovable):
                    tempmoveflag[0]=False
                if ((tempmoveflag[1]==False) & (tempmoveflag[0]==False)):
                    break
            elif (tempsignal.type==MOVEDOWNRIGHT):
                if (dmovable):
                    tempmoveflag[1]=False
                if (rmovable):
                    tempmoveflag[0]=False
                if ((tempmoveflag[1]==False) & (tempmoveflag[0]==False)):
                    break
        if (tempsignal.type==MOVEUPLEFT):
            if ((tempmoveflag[1]==False) & (tempmoveflag[0]==False)):
                tempsignal.receiver.movable=False
            elif (tempmoveflag[1]==False):
                tempsignal.type=MOVELEFT
            elif (tempmoveflag[0]==False):
                tempsignal.type=MOVEUP
        elif (tempsignal.type==MOVEUPRIGHT):
            if ((tempmoveflag[1]==False) & (tempmoveflag[0]==False)):
                tempsignal.receiver.movable=False
            elif (tempmoveflag[1]==False):
                tempsignal.type=MOVERIGHT
            elif (tempmoveflag[0]==False):
                tempsignal.type=MOVEUP
        elif (tempsignal.type==MOVEDOWNLEFT):
            if ((tempmoveflag[1]==False) & (tempmoveflag[0]==False)):
                tempsignal.receiver.movable=False
            elif (tempmoveflag[1]==False):
                tempsignal.type=MOVELEFT
            elif (tempmoveflag[0]==False):
                tempsignal.type=MOVEDOWN
        elif (tempsignal.type==MOVEDOWNRIGHT):
            if ((tempmoveflag[1]==False) & (tempmoveflag[0]==False)):
                tempsignal.receiver.movable=False
            elif (tempmoveflag[1]==False):
                tempsignal.type=MOVERIGHT
            elif (tempmoveflag[0]==False):
                tempsignal.type=MOVEDOWN
        if ((tempmoveflag[1]==True) | (tempmoveflag[0]==True)):
            tempsignal.receiver.movable=True


# 信号处理函数,解决信号冲突,向每个对象发送信号
    def message_translate(self):
        move_state = self.keyboardevent[K_w]<<3 | self.keyboardevent[K_s]<<2 | \
                    self.keyboardevent[K_a]<<1 | self.keyboardevent[K_d]
        move_switch = [None,3,2,None,1,7,6,None,0,5,4,None,None,None,None,None]
        #if (not move_switch[move_state] is None):
        tempsignal=Signal(move_switch[move_state],self.single_player)
        if move_switch[move_state] is not None:
            self.single_player.skill_direction=move_switch[move_state]
        skill_state = self.keyboardevent[K_j]<<2 | self.keyboardevent[K_k]<<1 | self.keyboardevent[K_l]
        skill_switch = [None,10,9,None,8,None,None,None]
        #J      SKILL1=8
        # #K      SKILL2=9
        # #L      SKILL3=10
        # #可改变skill_switch定义组合技
        self.move_judge(tempsignal)
        if (not skill_switch[skill_state] is None):
            if ((extern.last_fresh_time-self.single_player.skill1time)>self.single_player.skill1_cd):
                tempsignal=Signal(skill_switch[skill_state],self.single_player)
        self.signal_list.append(tempsignal)
        #再考虑攻击判定，这样被打到就会取消之前的移动信号
        self.attack_judge()
        for signal in self.signal_list:
            signal.receiver.signal=signal.type
            del signal
        if self.keyboardevent[K_ESCAPE]:
            extern.game_state=GAMEINIT
            for inx,signal in enumerate(self.signal_list):
                del self.signal_list[inx]
            for index,enemy in enumerate(self.enemy_list):
                del self.enemy_list[index]
            del self.single_player
            self.gameover=True
            extern.init_time=extern.last_fresh_time

# 游戏画面与状态更新
    def game_update(self):
        extern.singleplayergame_resource.pic_temp=extern.singleplayergame_resource.pic.copy()
        for enemy in self.enemy_list:
            enemy.update()
        extern.interface_resource.screen.blit(extern.gameinterface,(0,0))
        self.keyboardevent=pygame.key.get_pressed()
        self.message_translate()
        if not self.gameover:
            self.single_player.update()
            for inx,skill in enumerate(self.skill_list):
                if (skill.delflag):#skill寿命到了的话
                    for enemy in self.enemy_list:
                        if skill in enemy.ignore_skill:
                            enemy.ignore_skill.remove(skill)
                    del self.skill_list[inx]
                else:
                    skill.update()
            extern.interface_resource.screen.blit(
                extern.singleplayergame_resource.pic_temp,
                self.blit_startpoint()
                )
            self.state_update()
            for index,enemy in enumerate(self.enemy_list):
                if (enemy.state==ENEMYDEAD):
                    del self.enemy_list[index]
        # if (self.single_player.state==PLAYERDEAD):
        #     self.gameover=1
        # if (len(self.enemylist)==0):
        #     self.gameover=1

    def blit_startpoint(self):
        sx=0
        if ((self.single_player.site[0]>mainwindow_size[0]/2) &
        (self.single_player.site[0]<(extern.singleplayergame_resource.size[0]-mainwindow_size[0]/2))):
            sx=self.single_player.site[0]-mainwindow_size[0]/2
        elif self.single_player.site[0]>=(extern.singleplayergame_resource.size[0]-mainwindow_size[0]/2):
            sx=extern.singleplayergame_resource.size[0]-mainwindow_size[0]
        return (-sx,0)

    def state_update(self):
        extern.interface_resource.screen.blit(extern.singleplayergame_resource.single_game_hpmp,
        (mainwindow_size[0]/3-single_game_hp_size[0]/2,
        mainwindow_size[1]*5/6-2*single_game_hp_size[1])
    )
        extern.interface_resource.screen.blit(extern.singleplayergame_resource.single_game_hpmp,
        (mainwindow_size[0]/3-single_game_hp_size[0]/2,
        mainwindow_size[1]*5/6-1*single_game_hp_size[1])
    )
        extern.interface_resource.screen.set_clip((mainwindow_size[0]/3-single_game_hp_size[0]/2,
        mainwindow_size[1]*5/6-2*single_game_hp_size[1]),
        (mainwindow_size[0]/3+single_game_hp_size[0]/2,
        mainwindow_size[1]*5/6+0*single_game_hp_size[1])
    )
        extern.interface_resource.screen.blit(extern.singleplayergame_resource.single_game_hp,
        (mainwindow_size[0]/3-single_game_hp_size[0]/2+(self.single_player.max_life)/10/2-(self.single_player.max_life)/10,
        mainwindow_size[1]*5/6-2*single_game_hp_size[1])
    )
        extern.interface_resource.screen.blit(extern.singleplayergame_resource.single_game_mp,
        (mainwindow_size[0]/3-single_game_hp_size[0]/2+(self.single_player.max_mana)/10/2-(self.single_player.max_mana)/10,
        mainwindow_size[1]*5/6-1*single_game_hp_size[1])
    )
        extern.interface_resource.screen.set_clip((0,0),mainwindow_size)

        extern.interface_resource.screen.blit(extern.singleplayergame_resource.gameinterface,
        (mainwindow_size[0]-single_game_map_size[0],
        mainwindow_size[1]-single_game_map_size[1])
    )
        extern.interface_resource.screen.blit(extern.singleplayergame_resource.single_game_smallplayer,
        (mainwindow_size[0]-single_game_map_size[0]+self.single_player.site[0]/extern.singleplayergame_resource.size[0]*single_game_map_size[0],
        mainwindow_size[1]-single_game_map_size[1]+self.single_player.site[1]/extern.singleplayergame_resource.size[1]*single_game_map_size[1])
    )
        
        extern.interface_resource.screen.blit(extern.singleplayergame_resource.single_game_k,
        (mainwindow_size[0]-single_game_map_size[0]-self.blit_startpoint()[0]/extern.singleplayergame_resource.size[0]*single_game_map_size[0],
        mainwindow_size[1]-single_game_map_size[1]-self.blit_startpoint()[1]/extern.singleplayergame_resource.size[1]*single_game_map_size[1])
    )
        extern.interface_resource.screen.blit(extern.character_resource.pic_portrait,
        (mainwindow_size[0]/4+0*single_game_portrait_size[0]/2,
        mainwindow_size[1]*5/6-1*single_game_portrait_size[1])
    )
        extern.interface_resource.screen.blit(extern.character_resource.skill_1,
        (mainwindow_size[0]/4+3/2*single_game_skill_size[0],
        mainwindow_size[1]*5/6-2*single_game_skill_size[1])
        )
        extern.interface_resource.screen.blit(extern.character_resource.skill_1,
        (mainwindow_size[0]/4+5/2*single_game_skill_size[0],
        mainwindow_size[1]*5/6-2*single_game_skill_size[1])
        )    
        extern.interface_resource.screen.blit(extern.character_resource.skill_1,
        (mainwindow_size[0]/4+7/2*single_game_skill_size[0],
        mainwindow_size[1]*5/6-2*single_game_skill_size[1])
    )

# 信号类
class Signal():
    def __init__(self,type,receiver):
        self.type=type
        self.receiver=receiver
