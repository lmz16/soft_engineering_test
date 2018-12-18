#
#   输入处理函数
#

import pygame
from pygame.locals import *

p1_key_index = [
    K_w, K_s, K_a, K_d, K_j, K_k, K_l, K_ESCAPE
]
p1_key_name = [
    "up","down","left","right","atk1","atk2","atk3","esc"
]

#   监听界面区域的鼠标点击
def regionMonitor(event,xy1,xy2):
    x1,x2 = [xy1[0]-xy2[0]/2,xy1[0]+xy2[0]/2]
    y1,y2 = [xy1[1]-xy2[1]/2,xy1[1]+xy2[1]/2]
    if event.type==MOUSEBUTTONDOWN:
        if event.button==1:
            if ((event.pos[0]<x2)&(event.pos[0]>x1)&
                (event.pos[1]<y2)&(event.pos[1]>y1)):
                return True
    return False

#   外界输入接口
class Control():
    def __init__(self):
        self.reset()


    def update(self):
        self.reset()
        key_pressed = pygame.key.get_pressed()
        for i in range(0,len(p1_key_name)):
            if key_pressed[p1_key_index[i]] != 0:
                self.p1_key[p1_key_name[i]] = True


    def reset(self):
        self.p1_key = {
            #上下左右
            "up":None,
            "down":None,
            "left":None,
            "right":None,
            #攻击
            "atk1":None,
            "atk2":None,
            "atk3":None,
            #退出
            "esc":None
        }
        self.p2_key = {
            #上下左右
            "up":None,
            "down":None,
            "left":None,
            "right":None,
            #攻击
            "atk1":None,
            "atk2":None,
            "atk3":None,
            #退出
            "esc":None
        }
