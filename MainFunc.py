#
#	Main文件的函数实现
#

import pygame
from pygame.locals import *
import os
import time
import json
import socket

import Extern as Et
import Resource as Rs
import Input as Ip
import Game as Gm
import Player as Pl
import Skill
import Item
import threading
from Define import *
import random

HOST, PORT = "localhost", 20000

#   游戏程序初始化函数
def init():
    pygame.init()	#pygame初始化
    pygame.mouse.set_visible(False)	#隐藏鼠标
    Et.game_state = GAMEINIT #初始化游戏状态
    Et.R_if = Rs.RInterface("Resource/json/interface") #加载界面资源
    Et.I_ctr = Ip.Control()     #初始化键盘控制
    netInit()

def netInit():
    Et.t_net = threading.Thread(target = host,args = ())
    Et.fake_ip = random.randint(0,100)


#   游戏退出函数
def gameQuit(event):
    if event.type==QUIT:
        pygame.quit()
        os._exit(0)

#   时间更新函数
def timeUpdate():
    temptime = time.time()
    if (temptime - Et.fresh_time) > 1/fps:
        Et.fresh_time = temptime
        return True
    else:
        return False 

def gameStateManager():
    if Et.game_state == GAMELOAD:
        Et.S_game = None
        Et.S_game = Gm.SingleGame()
    elif Et.game_state == GAMESTART:
        Et.S_game.update()
        #pass
    elif Et.game_state == GAMEONLINEINIT2:
        onlineInit()
        Et.t_net.setDaemon(True)
        Et.t_net.start()
    elif Et.game_state == GAMEONLINE:
        pass


def onlineInit():
    pass


def host():
    temptime = 0
    while True:
        if (Et.fresh_time - temptime)>1/fps:
            temptime = time.time()
            client(pack())
            if Et.online_over:
                break


def client(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    try:
        sock.sendall(message.encode("utf-8"))
        response = sock.recv(1024)
        jresp = json.loads(response.decode('utf-8'))
        Et.Pr_info = []
        for p in jresp[1]:
            temp = Pl.PlayerInfo()
            temp.site = p[0]
            temp.state = p[3]
            temp.life_value = p[2]
            temp.max_life = p[1]
            temp.count = p[4]
            temp.pic_direction = p[5]
            temp.kind = p[7]
            if p[6] == Et.fake_ip:
                Et.online_player_site = p[0]
                Et.online_camp = p[8]
            Et.Pr_info.append(temp)
        Et.Sk_info = []
        for s in jresp[2]:
            temp = Skill.SkillInfo()
            temp.draw_line = s[2]
            temp.kind = s[1]
            temp.site = s[0]
            Et.Sk_info.append(temp)
        Et.Os_info = []
        for o in jresp[3]:
            temp = Item.ObstacleInfo()
            temp.kind = o[1]
            temp.site = o[0]
            Et.Os_info.append(temp)
        if jresp[0] == 3:
            if Et.online_camp == 0:
                Et.online_over = 2
            else :
                Et.online_over = 1
        elif jresp[0] == 4:
            if Et.online_camp == 1:
                Et.online_over = 2
            else :
                Et.online_over = 1


    finally:
        sock.close()

def pack():
    msg = [Et.I_ctr.p1_key]
    msg[0]["player_kind"] = Et.player_choice
    msg[0]["ip"] = Et.fake_ip
    jmsg = json.dumps(msg)
    return jmsg
