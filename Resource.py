#
#   资源管理类
#

from Define import *
import pygame
from pygame.locals import *
import json

class RInterface():
    def __init__(self,loadfile):
        with open (loadfile,'r') as RIfile:
            data=json.load(RIfile)
            self.screen = pygame.display.set_mode(mainwindow_size,0,32)
            self.main_bk_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["main_bk_pic"]).convert(),
                mainwindow_size
            )
            self.cursor_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["cursor_pic"]).convert_alpha(),
                cursor_size
            )
            self.start_single_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["single_button"]).convert_alpha(),
                start_button_size
            )
            self.start_setting_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["setting_button"]).convert_alpha(),
                start_button_size
            )
            self.start_online_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["online_button"]).convert_alpha(),
                start_button_size
            )
            self.start_help_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["help_button"]).convert_alpha(),
                start_button_size
            )
            self.start_custom_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["custom_button"]).convert_alpha(),
                start_button_size
            )
            self.help_text_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["help_text"]).convert_alpha(),
                help_text_size
            )
            self.setting_text_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["setting_text"]).convert_alpha(),
                help_text_size
            )
            self.setting_choose_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["setting_choose"]).convert_alpha(),
                single_game_p_size
            )
            self.single_frame_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["single_frame_pic"]).convert_alpha(),
                mainwindow_size
            )
            self.single_hp_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["single_hp"]).convert_alpha(),
                single_game_hp_size
            )
            self.single_game_smallplayer_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["single_game_smallplayer"]).convert_alpha(),
                single_game_p_size
            )
            self.custom_choose_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["custom_choose"]).convert_alpha(),
                mainwindow_size
            )
            self.custom_choose_bk_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["custom_choose_bk"]).convert_alpha(),
                mainwindow_size
            )
            self.pic_choose_bk_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["pic_choose_bk"]).convert_alpha(),
                custom_pic_choose_size
            )
            self.custom_frame_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["custom_frame"]).convert_alpha(),
                (custom_pic_choose_size[0] + 20, custom_pic_choose_size[1] + 20)
            )
            self.custom_choose_choose_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["custom_choose_choose"]).convert_alpha(),
                (mainwindow_size)
            )
            self.vic_pic = pygame.transform.smoothscale(
                pygame.image.load("Resource/interface/vic.png").convert_alpha(),
                (250,70)
            )
            self.lose_pic = pygame.transform.smoothscale(
                pygame.image.load("Resource/interface/lose.png").convert_alpha(),
                (300, 70)
            )


    
    def __del__(self):
        del self.main_bk_pic
        del self.cursor_pic
        del self.start_single_pic
        del self.start_setting_pic
        del self.start_online_pic
        del self.start_help_pic
        del self.start_custom_pic
        del self.help_text_pic
        del self.setting_text_pic
        del self.setting_choose_pic
        del self.screen
        del self.single_frame_pic
        del self.single_hp_pic
        del self.single_game_smallplayer_pic
        del self.custom_choose_pic
        del self.custom_choose_bk_pic
        del self.pic_choose_bk_pic
        del self.custom_frame_pic
        del self.custom_choose_choose_pic



class RChoose():
    def __init__(self,loadfile):
        with open (loadfile,'r') as RCfile:
            data=json.load(RCfile)
            self.bottom_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["bottom_pic"]).convert_alpha(),
                mainwindow_size
            )
            self.single_choose_frame = pygame.transform.smoothscale(
                pygame.image.load(data[0]["single_choose_frame"]).convert_alpha(),
                mainwindow_size
            )
            self.single_choose_b = []
            for i in range(0,len((data[0]["single_choose_b"]))):
                self.single_choose_b.append(pygame.transform.smoothscale(
                    pygame.image.load(data[0]["single_choose_b"][i]).convert_alpha(),
                    single_choose_b_size)
                )
            self.single_choose_p = []
            self.character_file = []
            self.single_choose_play = pygame.transform.smoothscale(
                pygame.image.load(data[0]["single_choose_play"]).convert_alpha(),
                start_button_size
            )
            self.single_choose_bc = pygame.transform.smoothscale(
                pygame.image.load(data[0]["single_choose_choose"]).convert_alpha(),
                single_choose_bc_size
            )
            self.single_choose_pc = pygame.transform.smoothscale(
                pygame.image.load(data[0]["single_choose_choose"]).convert_alpha(),
                single_choose_pc_size
            )
        with open ("Resource/json/player_choose",'r') as RCfile:
            data = json.load(RCfile)
            for i in range(0,len(data[0]["data"])):
                self.single_choose_p.append(pygame.transform.smoothscale(
                    pygame.image.load(data[0]["data"][i]["pic"]).convert_alpha(),
                    single_choose_p_size)
                )
                self.character_file.append(data[0]["data"][i]["config_file"])
            self.single_portrait = []
            for i in range(0, len(data[0]["data"])):
                self.single_portrait.append(pygame.transform.smoothscale(
                    pygame.image.load(data[0]["data"][i]["pic"]).convert_alpha(),
                    single_game_portrait_size)
                )


class RSingle():
    def __init__(self,loadfile):
        with open(loadfile, 'r') as RSfile:
            data = json.load(RSfile)
            self.bg_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["bg_pic"]).convert_alpha(),
                data[0]["bg_size"]
            )
            self.size = data[0]["bg_size"]
            self.bg_pic_temp = self.bg_pic.copy()
            self.enemy_list = data[0]["enemy"]
            self.obstacle_list = data[0]["obstacle"]
            self.small_map_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["bg_pic"]).convert_alpha(),
                single_game_map_size
            )


class RCharacter():
    def __init__(self, loadfile):
        with open(loadfile, 'r') as RCfile:
            data = json.load(RCfile)
            self.max_life = data[0]["life_value"]
            self.pic_static = []
            self.pic_move = []
            self.pic_attack = []
            self.pic_attacked = []
            self.size = data[0]["realsize"]
            for p in data[0]["static"]:
                temp = pygame.transform.smoothscale(
                    pygame.image.load(p).convert_alpha(),
                    data[0]["size"])
                tempf = pygame.transform.flip(temp, True, False)
                self.pic_static.append(
                    [temp, tempf]
                )
            for p in data[0]["move"]:
                temp = pygame.transform.smoothscale(
                        pygame.image.load(p).convert_alpha(),
                        data[0]["size"])
                tempf = pygame.transform.flip(temp,True,False)
                self.pic_move.append(
                    [temp,tempf]
                )
            for p in data[0]["attack"]:
                temp = pygame.transform.smoothscale(
                    pygame.image.load(p).convert_alpha(),
                    data[0]["size"])
                tempf = pygame.transform.flip(temp, True, False)
                self.pic_attack.append(
                    [temp, tempf]
                )
            for p in data[0]["attacked"]:
                temp = pygame.transform.smoothscale(
                    pygame.image.load(p).convert_alpha(),
                    data[0]["size"])
                tempf = pygame.transform.flip(temp, True, False)
                self.pic_attacked.append(
                    [temp, tempf]
                )
            self.velocity = data[0]["v"]
            self.skill = data[0]["skill"]

    def __del__(self):
        for p in self.pic_static:
            del p
        for p in self.pic_move:
            del p
        for p in self.pic_attack:
            del p
        for p in self.pic_attacked:
            del p


class REnemy():
    def __init__(self,loadfile):
        with open(loadfile, 'r') as REfile:
            data = json.load(REfile)
            self.max_life = data[0]["life_value"]
            self.pic_static = []
            self.pic_move = []
            self.pic_attack = []
            self.pic_attacked = []
            self.size = data[0]["realsize"]
            for p in data[0]["static"]:
                temp = pygame.transform.smoothscale(
                    pygame.image.load(p).convert_alpha(),
                    data[0]["size"])
                tempf = pygame.transform.flip(temp, True, False)
                self.pic_static.append(
                    [temp, tempf]
                )
            for p in data[0]["move"]:
                temp = pygame.transform.smoothscale(
                        pygame.image.load(p).convert_alpha(),
                        data[0]["size"])
                tempf = pygame.transform.flip(temp,True,False)
                self.pic_move.append(
                    [temp,tempf]
                )
            for p in data[0]["attack"]:
                temp = pygame.transform.smoothscale(
                    pygame.image.load(p).convert_alpha(),
                    data[0]["size"])
                tempf = pygame.transform.flip(temp, True, False)
                self.pic_attack.append(
                    [temp, tempf]
                )
            for p in data[0]["attacked"]:
                temp = pygame.transform.smoothscale(
                    pygame.image.load(p).convert_alpha(),
                    data[0]["size"])
                tempf = pygame.transform.flip(temp, True, False)
                self.pic_attacked.append(
                    [temp, tempf]
                )
            self.velocity = data[0]["v"]


class RObstacle():
    def __init__(self,loadfile):
        with open(loadfile, 'r') as ROfile:
            data = json.load(ROfile)
            self.pic = pygame.transform.smoothscale(
                    pygame.image.load(data[0]["pic"]).convert_alpha(),
                    data[0]["size"])


class RSkill():
    def __init__(self,loadfile):
        with open(loadfile, 'r') as RSfile:
            data = json.load(RSfile)
            self.duration = data[0]["life"]
            self.pic = pygame.transform.smoothscale(
                    pygame.image.load(data[0]["pic"]).convert_alpha(),
                    data[0]["size"])
            self.single_game_skill = pygame.transform.smoothscale(
                pygame.image.load(data[0]["pic"]).convert_alpha(),
                single_game_skill_size)
            self.size = data[0]["realsize"]
            self.damage = data[0]["damage"]
            self.velocity = data[0]["v"]
            self.extra_param1 = data[0]["extra_param1"]
            self.extra_param2 = data[0]["extra_param2"]


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