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

    
    def __del__(self):
        del self.main_bk_pic
        del self.cursor_pic
        del self.start_single_pic
        del self.screen


class RChoose():
    def __init__(self,loadfile):
        with open (loadfile,'r') as RCfile:
            data=json.load(RCfile)
            self.bottom_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["bottom_pic"]).convert_alpha(),
                mainwindow_size
            )
            self.bottom_temp = self.bottom_pic.copy()


class RSingle():
    def __init__(self,loadfile):
        with open(loadfile, 'r') as RSfile:
            data = json.load(RSfile)
            self.bg_pic = pygame.transform.smoothscale(
                pygame.image.load(data[0]["bg_pic"]).convert_alpha(),
                data[0]["bg_size"]
            )


class RCharacter():
    def __init__(self, loadfile):
        with open(loadfile, 'r') as RCfile:
            data = json.load(RCfile)
            self.pic_static = []
            self.pic_move = []
            self.attack = []
            self.attacked = []
            self.size = data[0]["size"]
