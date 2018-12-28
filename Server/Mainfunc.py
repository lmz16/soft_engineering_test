#
#   外部逻辑
#

from Define import *
import Extern as Et
import Game
import time
import json
import sys

def pinfoInit():
    pinfo = {
        "site":[0,0],
        "max_life":0,
        "life":0,
        "state":PLAYERSTATIC,
        "count":0,
        "pic_direction":RIGHT,
        "visable":True,
        "size":[30,30],
        "ip":0,
        "kind":0,
        "camp":0,
    }
    return pinfo


def sinfoInit():
    sinfo = {
        "site":[0,0],
        "size": [0, 0],
        "visable":True,
        "kind":0,
        "draw_line":None,
        "extra_param1":0,
        "extra_param2":0,
    }
    return sinfo

def oinfoInit():
    oinfo = {
        "site":[0,0],
        "kind":0,
        "size":[0,0],
    }
    return oinfo

def gameInit():
    Et.online_game = None
    Et.online_game = Game.Online()
    skillAllInit()

#   游戏的有限状态机
def gameFSM():
    temptime = time.time()
    if temptime > Et.fresh_time - 1/fps:
        Et.fresh_time = temptime    #刷新时间
        if Et.game_state == GAMEWAIT:
            gameInit()  #初始化游戏对象
            Et.game_state = GAMEJOIN
        elif Et.game_state == GAMEJOIN: #游戏玩家进入时间
            if temptime < Et.init_time + 4:
                joinRespond()
            else:
                Et.game_state = GAMESTART
        elif Et.game_state == GAMESTART:    #游戏运行
            messageUnpack()
            Et.online_game.update()
        elif Et.game_state in [GAMEWIN0,GAMEWIN1]:
            Et.Pr_info = []
            Et.Sk_info = []
            Et.Ob_info = []
            Et.num_ip = []
            Et.data = None
            if Et.count == 0:
                Et.game_state = GAMEWAIT
                #Et.count = 0
            else:
                Et.count -= 1

#   用于在游戏里添加玩家
def joinRespond():
    if Et.data["ip"] not in Et.num_ip:
        Et.num_ip.append(Et.data["ip"])
        Et.online_game.playerJoin()

#   解包数据,将信息传给游戏逻辑
def messageUnpack():
    if Et.data["ip"] in Et.num_ip:
        num = Et.num_ip.index(Et.data["ip"])
        Et.online_game.ctr[num] = {
            "up": Et.data["up"],
            "down": Et.data["down"],
            "left": Et.data["left"],
            "right": Et.data["right"],
            "atk1": Et.data["atk1"],
            "atk2": Et.data["atk2"],
            "atk3": Et.data["atk3"],
        }

def sendBack():
    tempp = []
    for p in Et.Pr_info:
        tempp.append([
            p["site"],
            p["max_life"],
            p["life"],
            p["state"],
            p["count"],
            p["pic_direction"],
            p["ip"],
            p["kind"],
            p["camp"],
        ])
    temps = []
    for s in Et.Sk_info:
        temps.append([
            s["site"],
            s["kind"],
            s["draw_line"],
        ])
    tempo = []
    for o in Et.Ob_info:
        tempo.append([
            o["site"],
            o["kind"],
        ])
    sdata = [Et.game_state,tempp,temps,tempo]
    print(Et.game_state)
    return sdata


#   技能配置信息初始化
def RSkillInit():
    rskill = {
        "damage":0,
        "size":[0,0],
        "duration":0,
        "velocity":0,
    }
    return rskill


def skillAllInit():
    skill_file = [
        "Resource/json/sk0",
        "Resource/json/sk1",
        "Resource/json/sk2",
        "Resource/json/sk3",
        "Resource/json/sk4",
        "Resource/json/sk5",
        "Resource/json/sk6",
        "Resource/json/sk7",
        "Resource/json/sk8",
        "Resource/json/sk9",
        "Resource/json/sk10",
        "Resource/json/sk11",
        "Resource/json/sk12",
        "Resource/json/sk13",
    ]
    for s in range(0,len(Et.R_skill)):
        Et.R_skill[s] = RSkillInit()
        with open (skill_file[s],'r') as f:
            temp = json.load(f)
            Et.R_skill[s]["damage"] = temp[0]["damage"]
            Et.R_skill[s]["size"] = temp[0]["realsize"]
            Et.R_skill[s]["duration"] = temp[0]["life"]
            Et.R_skill[s]["velocity"] = temp[0]["v"]
            Et.R_skill[s]["extra_param1"] = temp[0]["extra_param1"]
            Et.R_skill[s]["extra_param2"] = temp[0]["extra_param2"]
