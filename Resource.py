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

    def __del__(self):
        del self.screen
        del self.start_background
        del self.cursor
        del self.start_button
        del self.start_button_setting
        del self.start_button_help
        del self.start_button_custom
        del self.help_text


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
            self.skill1_cd=playerinfo[4]
        
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