#
#   在线游戏的内部逻辑文件
#

import Extern as Et
import Mainfunc as Mf
import Player as Pl
from Define import *
import json

character_file = [
    "Resource/json/character1",
    "Resource/json/character2",
    "Resource/json/character3",
]

class Online():
    def __init__(self):
        self.player1 = []
        self.player2 = []
        self.ctr = []
        self.skill_list = []    #技能列表
        self.obstacle_list = [] #障碍物列表
        self.size = [1000,1000]
        self.loadGame()

#   玩家加入函数
    def playerJoin(self):
        Et.Pr_info.append(Mf.pinfoInit())
        self.ctr.append(ctrInit())
        tempplayer = Pl.Player(Et.Pr_info[len(Et.Pr_info)-1])
        tempplayer.id = len(Et.Pr_info) - 1
        tempplayer.game = self
        tempplayer.info["ip"] = Et.num_ip[tempplayer.id]
        self.loadPlayer(tempplayer,Et.data["player_kind"])
        if len(self.player1)>len(self.player2):
            self.player2.append(tempplayer)
            tempplayer.camp = 1
            tempplayer.info["camp"] = 1
            tempplayer.info["site"] = [self.size[0]-200,300+50*(len(self.player2)-1)]
            tempplayer.info["pic_direction"] = LEFT
        else:
            self.player1.append(tempplayer)
            tempplayer.camp = 0
            tempplayer.info["camp"] = 0
            tempplayer.info["site"] = [200,300+50*(len(self.player1)-1)]

#   信号发送
    def controlSignal(self):
        for i in range(0,len(self.player1)):
            self.player1[i].signal = self.playerSignal(
                self.ctr[self.player1[i].id])
        for i in range(0,len(self.player2)):
            self.player2[i].signal = self.playerSignal(
                self.ctr[self.player2[i].id])

#   对每一个人物发送信号
    def playerSignal(self,ctr):
        signal = None
        move_switch = [None, 3, 2, None, 1, 7, 6, None, 0, 5, 4, None, None, None, None, None]
        move_state = ctr["up"] << 3 | ctr["down"] << 2 | ctr["left"] << 1 | \
                     ctr["right"]
        signal = move_switch[move_state]
        if ctr["atk1"]:
            signal = SKILL1
        elif ctr["atk2"]:
            signal = SKILL2
        elif ctr["atk3"]:
            signal = SKILL3
        return signal

#   人物配置读取
    def loadPlayer(self,player,kind):
        with open (character_file[kind],'r') as f:
            jdata = json.load(f)[0]
            player.info["size"] = jdata["realsize"]
            player.info["max_life"] = jdata["life_value"]
            player.info["life"] = jdata["life_value"]
            player.velocity = jdata["v"]
            player.skill_type = jdata["skill"]
            player.info["kind"] = kind


    def loadGame(self):
        with open("Resource/json/game1") as f:
            jdata = json.load(f)[0]
            self.size = jdata["bg_size"]
            for o in jdata["obstacle"]:
                temp = Mf.oinfoInit()
                temp["site"] = o["site"]
                temp["size"] = o["size"]
                temp["kind"] = o["kind"]
                Et.Ob_info.append(temp)
                self.obstacle_list.append(Ob(temp))

    def update(self):
        self.controlSignal()
        for p in self.player1:
            if p.info["life"]<0:
                p.info["site"][1] = -100000
        for p in self.player2:
            if p.info["life"]<0:
                p.info["site"][1] = -100000        
        for s in self.skill_list:
            s.update()
            s.influence()
            self.delSkill(s)
        self.moveJudge()
        for p in self.player1:
            p.update()
        for p in self.player2:
            p.update()
        self.loseJudge()
        
    def moveJudge(self):
        for p in self.player1:
            p.movable = [True]*4
        for p in self.player2:
            p.movable = [True]*4
        for ob in self.obstacle_list:
            for p in self.player1:
                self.__collisionJudge(ob.info,p)
            for p in self.player2:
                self.__collisionJudge(ob.info,p)

    def __collisionJudge(self, obstacleInfo, obj):
        dxMin = (obj.info["size"][0] + obstacleInfo["size"][0]) / 2
        dyMin = (obj.info["size"][1] + obstacleInfo["size"][1]) / 2
        if ((abs(obj.info["site"][0] - obstacleInfo["site"][0]) < (dxMin + COLLISIONTHRESHOLD)) &
                (abs(obj.info["site"][1] - obstacleInfo["site"][1]) < (dyMin + COLLISIONTHRESHOLD))):
            obj.movable[3] &= ~(obj.info["site"][0] < obstacleInfo["site"][0] - dxMin)
            obj.movable[2] &= ~(obj.info["site"][0] > obstacleInfo["site"][0] + dxMin)
            obj.movable[1] &= ~(obj.info["site"][1] < obstacleInfo["site"][1] - dyMin)
            obj.movable[0] &= ~(obj.info["site"][1] > obstacleInfo["site"][1] + dyMin)

    def loseJudge(self):
        flag0 = 1
        flag1 = 1
        for p in self.player1:
            if p.info["life"] > 0:
                flag0 = 0
                break
        for p in self.player2:
            if p.info["life"] > 0:
                flag1 = 0
                break
        if flag0:
            Et.game_state = GAMEWIN1
        if flag1:
            Et.game_state = GAMEWIN0
        Et.count = len(Et.Pr_info)



    def delSkill(self,skill):
        if skill.delflag:
            Et.Sk_info.remove(skill.info)
            if skill in skill.caster.skill_list[0]:
                skill.caster.skill_list[0].remove(skill)
            if skill in skill.caster.skill_list[1]:
                skill.caster.skill_list[1].remove(skill)
            if skill in skill.caster.skill_list[2]:
                skill.caster.skill_list[2].remove(skill)
            self.skill_list.remove(skill)
            del skill



def ctrInit():
    ctr = {
        "up":False,
        "down":False,
        "left":False,
        "right":False,
        "atk1":False,
        "atk2": False,
        "atk3": False,
    }
    return ctr


class Ob():
    def __init__(self,info):
        self.info = info