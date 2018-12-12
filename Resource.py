# 资源管理类

from define import *
import pygame
from pygame.locals import *
import json
import time

class RInterface():
    def __init__(self,loadfile):
        with open (loadfile,'r') as Rinterfacefile:
            data=json.load(Rinterfacefile)
            self.screen=pygame.display.set_mode(mainwindow_size,0,32)
            self.start_background=pygame.transform.smoothscale(
                pygame.image.load(data[0]).convert(),mainwindow_size)
            self.cursor=pygame.transform.smoothscale(
                pygame.image.load(data[1]).convert_alpha(),cursor_size)
            self.start_button=pygame.transform.smoothscale(
                pygame.image.load(data[2]).convert_alpha(),start_button_size)
            self.start_button_online=pygame.transform.smoothscale(
                pygame.image.load(data[3]).convert_alpha(),start_button_size)
            self.start_button_setting=pygame.transform.smoothscale(
                pygame.image.load(data[4]).convert_alpha(),start_button_size)
            self.start_button_help=pygame.transform.smoothscale(
                pygame.image.load(data[5]).convert_alpha(),start_button_size)
            self.start_button_custom=pygame.transform.smoothscale(
                pygame.image.load(data[6]).convert_alpha(),start_button_size)
            self.help_text=pygame.transform.smoothscale(
                pygame.image.load(data[7]).convert_alpha(),help_text_size)
            self.single_choose_background=pygame.transform.smoothscale(
                pygame.image.load(data[8]).convert_alpha(),mainwindow_size)
            self.single_choose_b1=pygame.transform.smoothscale(
                pygame.image.load(data[9]).convert_alpha(),single_choose_b_size)
            self.single_choose_b2=pygame.transform.smoothscale(
                pygame.image.load(data[10]).convert_alpha(),single_choose_b_size)
            self.single_choose_b3=pygame.transform.smoothscale(
                pygame.image.load(data[11]).convert_alpha(),single_choose_b_size)
            self.single_choose_p1=pygame.transform.smoothscale(
                pygame.image.load(data[12]).convert_alpha(),single_choose_p_size)
            self.single_choose_p2=pygame.transform.smoothscale(
                pygame.image.load(data[13]).convert_alpha(),single_choose_p_size)
            self.single_choose_p3=pygame.transform.smoothscale(
                pygame.image.load(data[14]).convert_alpha(),single_choose_p_size)
            self.single_choose_play=pygame.transform.smoothscale(
                pygame.image.load(data[15]).convert_alpha(),start_button_size)
            self.single_choose_bc=pygame.transform.smoothscale(
                pygame.image.load(data[16]).convert_alpha(),single_choose_bc_size)
            self.single_choose_pc=pygame.transform.smoothscale(
                pygame.image.load(data[16]).convert_alpha(),single_choose_pc_size)
            self.custom_choose_bk1=pygame.transform.smoothscale(
                pygame.image.load(data[17][0]).convert_alpha(),mainwindow_size)
            self.custom_choose_bk2=pygame.transform.smoothscale(
                pygame.image.load(data[17][1]).convert_alpha(),mainwindow_size)
            self.custom_pic_choose_bk=pygame.transform.smoothscale(
                pygame.image.load(data[18]).convert_alpha(),custom_pic_choose_size)
            self.custom_frame=pygame.transform.smoothscale(
                pygame.image.load(data[19]).convert_alpha(),
                (custom_pic_choose_size[0]+30,custom_pic_choose_size[1]+30))

    def __del__(self):
        del self.screen
        del self.start_background
        del self.cursor
        del self.start_button
        del self.start_button_setting
        del self.start_button_help
        del self.start_button_custom
        del self.help_text
        del self.single_choose_background
        del self.single_choose_b1
        del self.single_choose_b2
        del self.single_choose_b3
        del self.single_choose_p1
        del self.single_choose_p2
        del self.single_choose_p3
        del self.single_choose_play
        del self.single_choose_bc
        del self.single_choose_pc
        del self.custom_choose_bk


class RCharacter():
    def __init__(self,loadfile):
        with open (loadfile,'r') as Rcharacterfile:
            playerinfo=json.load(Rcharacterfile)
            self.pic_static=pygame.transform.smoothscale(
                pygame.image.load(playerinfo[0][0]).convert_alpha(),playerinfo[1])
            self.pic_move1=pygame.transform.smoothscale(
                pygame.image.load(playerinfo[0][1]).convert_alpha(),playerinfo[1])
            self.pic_move2=pygame.transform.smoothscale(
                pygame.image.load(playerinfo[0][2]).convert_alpha(),playerinfo[1])
            self.pic_attack1=pygame.transform.smoothscale(
                pygame.image.load(playerinfo[0][3]).convert_alpha(),playerinfo[1])
            self.pic_attack2=pygame.transform.smoothscale(
                pygame.image.load(playerinfo[0][4]).convert_alpha(),playerinfo[1])
            self.pic_attacked=pygame.transform.smoothscale(
                pygame.image.load(playerinfo[0][5]).convert_alpha(),playerinfo[1])
            self.size=playerinfo[1]
            self.site=playerinfo[2][0]
            self.velocity=playerinfo[3]
            self.skill1_cd=playerinfo[4][0]
            self.skill2_cd=playerinfo[4][1]
            self.skill3_cd=playerinfo[4][2]
        
    def __del__(self):
        del self.pic_static
        del self.pic_move1
        del self.pic_move2
        del self.pic_attack1
        del self.pic_attack2


class RSingleplayergame():
    def __init__(self,loadfile):
        with open (loadfile,'r') as Rsingleplayergame:
            gameinfo=json.load(Rsingleplayergame)
            self.size=gameinfo[1]
            self.pic=pygame.transform.smoothscale(
                pygame.image.load(gameinfo[0]).convert_alpha(),self.size)
            self.pic_temp=self.pic.copy()
            self.enemysite=gameinfo[2]

    def __del__(self):
        del self.pic
        del self.pic_temp


class REnemy():
    def __init__(self,loadfile):
        with open (loadfile,'r') as Renemy:
            enemyinfo=json.load(Renemy)
            self.pic_static=pygame.transform.smoothscale(
                pygame.image.load(enemyinfo[0][0]).convert_alpha(),enemyinfo[1])
            self.pic_move1=pygame.transform.smoothscale(
                pygame.image.load(enemyinfo[0][1]).convert_alpha(),enemyinfo[1])
            self.pic_move2=pygame.transform.smoothscale(
                pygame.image.load(enemyinfo[0][2]).convert_alpha(),enemyinfo[1])
            self.pic_attack1=pygame.transform.smoothscale(
                pygame.image.load(enemyinfo[0][3]).convert_alpha(),enemyinfo[1])
            self.pic_attack2=pygame.transform.smoothscale(
                pygame.image.load(enemyinfo[0][4]).convert_alpha(),enemyinfo[1])
            self.size=enemyinfo[1]
            self.life=enemyinfo[2]
            self.velocity=enemyinfo[3]

    def __del__(self):
        del self.pic_static
        del self.pic_move1
        del self.pic_move2
        del self.pic_attack1
        del self.pic_attack2

class RSkill():
    def __init__(self,loadfile):
        with open (loadfile,'r') as Rskill:
            skillinfo=json.load(Rskill)
            self.pic1=pygame.transform.smoothscale(
                pygame.image.load(skillinfo[0][0]).convert_alpha(),skillinfo[1])
            self.size=skillinfo[1]
            self.duration=skillinfo[2]
            self.velocity=skillinfo[3]
            self.damage=skillinfo[4]
            self.last=skillinfo[5]
            self.kind=skillinfo[6]

class RCustom():
    def __init__(self,loadfile):
        with open (loadfile,'r') as Rcustom:
            custominfo=json.load(Rcustom)
            self.pic=[]
            self.picpath=custominfo[0]
            for picpath in custominfo[0]:
                self.pic.append(
                    pygame.transform.smoothscale(
                        pygame.image.load('Resource/custom/'+picpath).convert_alpha(),custom_thumbnail_size)
                )

    def __del__(self):
        for x in self.pic:
            del x