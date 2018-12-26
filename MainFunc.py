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
        # Et.I_ctr.update()
        # for key,value in Et.I_ctr.p1_key.items():
        #         if value:
        #                 print(key)


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
        for p in jresp[0]["p"]:
            temp = Pl.PlayerInfo()
            temp.site = p["site"]
            temp.state = p["state"]
            temp.life_value = p["life"]
            temp.max_life = p["max_life"]
            temp.state = p["state"]
            temp.count = p["count"]
            temp.pic_direction = p["pic_direction"]
            temp.kind = p["kind"]
            Et.Pr_info.append(temp)
        Et.Sk_info = []
        for s in jresp[0]["s"]:
            temp = Skill.SkillInfo()
            temp.kind = s["kind"]
            temp.site = s["site"]
            Et.Sk_info.append(temp)


    finally:
        sock.close()

def pack():
    msg = [Et.I_ctr.p1_key]
    msg[0]["player_kind"] = 0
    msg[0]["ip"] = Et.fake_ip
    jmsg = json.dumps(msg)
    return jmsg