#
#   外部逻辑
#

from Define import *
import Extern as Et
import Game
import time
import json

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
    }
    return pinfo


def sinfoInit():
    sinfo = {
        "site":[0,0],
        "size": [0, 0],
        "visable":True,
        "kind":0
    }
    return sinfo

def gameInit():
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
    sdata = [{
        "p":Et.Pr_info,
        "s":Et.Sk_info,
        "state":Et.game_state,
    }]
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
    ]
    for s in range(0,len(Et.R_skill)):
        Et.R_skill[s] = RSkillInit()
        with open (skill_file[s],'r') as f:
            temp = json.load(f)
            Et.R_skill[s]["damage"] = temp[0]["damage"]
            Et.R_skill[s]["size"] = temp[0]["realsize"]
            Et.R_skill[s]["duration"] = temp[0]["life"]
            Et.R_skill[s]["velocity"] = temp[0]["v"]