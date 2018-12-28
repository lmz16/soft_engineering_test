import threading
import pygame
from pygame.locals import *
import Extern as Et
from Define import *
import json
import time
import Resource as Rs
import os
import shutil
import Input as Ip

class CustomC():
    def __init__(self):
        self.temptime=0
        self.velocity=0
        self.customskill=[]
        self.finished=False
        self.buttonscale=[[95,185,68,98],[69,596,29,559],[203,295,68,98],[311,403,68,98],[95,185,231,258],[203,295,231,258]]
        self.rolllength=0
        self.actionkind=-1
        self.actioncomplete=[False,False,False,False,False]
        self.choosestate=0
        self.charactersize=[200,280]
        self.actionpic=[]
        self.actionblitcount=0
        self.actionpath=[[],[],[],[],[]]
        Et.custommode=Rs.RCustom('Resource/json/custom')
        #谢福生12月26日修改
        self.characterType=0
        #谢福生12月26日修改

    def state2init(self):
        self.actioncomplete[self.actionkind]=False
        if len(self.actionpic)>0:
            for p in self.actionpic:
                del p
        self.actionpic=[]
        self.actionpath[self.actionkind]=[]
 #谢福生12月26日修改
    def writeJson(self):
        flag=0
        for i in range(5):
            if self.actioncomplete[i]==False:
                flag=1
        if(flag==0):
            dirname='Resource/character/'+time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
            os.mkdir(dirname)
            filename=[*self.actionpath[0],*self.actionpath[1],*self.actionpath[2],*self.actionpath[3]]
            filename=list({}.fromkeys(filename).keys()) 
            for x in filename:
                shutil.copyfile(x,dirname+'/'+x.split('/')[-1])
            with open ('Resource/json/'+time.strftime('%Y%m%d%H%M',time.localtime(time.time())),'w') as mc:
                if self.characterType==0:
                    info = [{
                            "size":[48,80],
                            "realsize":[48,80],
                            "life_value":2000,
                            "static":[
                                dirname+'/'+self.actionpath[0][0].split('/')[-1],
                                dirname+'/'+self.actionpath[0][1].split('/')[-1],
                                dirname+'/'+self.actionpath[0][2].split('/')[-1],
                            ],
                            "move":[
                                dirname+'/'+self.actionpath[2][0].split('/')[-1],
                                dirname+'/'+self.actionpath[2][1].split('/')[-1],
                                dirname+'/'+self.actionpath[2][2].split('/')[-1],
                                ],
                            "attack":[
                                dirname+'/'+self.actionpath[1][0].split('/')[-1],
                                dirname+'/'+self.actionpath[1][1].split('/')[-1],
                                dirname+'/'+self.actionpath[1][2].split('/')[-1],
                            ],
                            "attacked":[
                                dirname+'/'+self.actionpath[3][0].split('/')[-1],
                                dirname+'/'+self.actionpath[3][1].split('/')[-1],
                                dirname+'/'+self.actionpath[3][2].split('/')[-1],
                            ],
                            "v":[5,5],
                            "skill":[self.customskill[0],self.customskill[1],self.customskill[2]],
                            "skillCD":[1,2,3],
                        }]
                elif self.characterType==1:
                    info = [{
                            "size":[48,80],
                            "realsize":[48,80],
                            "life_value":1000,
                            "static":[
                                dirname+'/'+self.actionpath[0][0].split('/')[-1],
                                dirname+'/'+self.actionpath[0][1].split('/')[-1],
                                dirname+'/'+self.actionpath[0][2].split('/')[-1],
                            ],
                            "move":[
                                dirname+'/'+self.actionpath[2][0].split('/')[-1],
                                dirname+'/'+self.actionpath[2][1].split('/')[-1],
                                dirname+'/'+self.actionpath[2][2].split('/')[-1],
                                ],
                            "attack":[
                                dirname+'/'+self.actionpath[1][0].split('/')[-1],
                                dirname+'/'+self.actionpath[1][1].split('/')[-1],
                                dirname+'/'+self.actionpath[1][2].split('/')[-1],
                            ],
                            "attacked":[
                                dirname+'/'+self.actionpath[3][0].split('/')[-1],
                                dirname+'/'+self.actionpath[3][1].split('/')[-1],
                                dirname+'/'+self.actionpath[3][2].split('/')[-1],
                            ],
                            "v":[10,10],
                            "skill":[self.customskill[0],self.customskill[1],self.customskill[2]],
                            "skillCD":[1,2,3],
                        }]
 #谢福生12月26日修改
                elif self.characterType==2:
                    info = [{
                            "size":[48,80],
                            "realsize":[48,80],
                            "life_value":1000,
                            "static":[
                                dirname+'/'+self.actionpath[0][0].split('/')[-1],
                                dirname+'/'+self.actionpath[0][1].split('/')[-1],
                                dirname+'/'+self.actionpath[0][2].split('/')[-1],
                            ],
                            "move":[
                                dirname+'/'+self.actionpath[2][0].split('/')[-1],
                                dirname+'/'+self.actionpath[2][1].split('/')[-1],
                                dirname+'/'+self.actionpath[2][2].split('/')[-1],
                                ],
                            "attack":[
                                dirname+'/'+self.actionpath[1][0].split('/')[-1],
                                dirname+'/'+self.actionpath[1][1].split('/')[-1],
                                dirname+'/'+self.actionpath[1][2].split('/')[-1],
                            ],
                            "attacked":[
                                dirname+'/'+self.actionpath[3][0].split('/')[-1],
                                dirname+'/'+self.actionpath[3][1].split('/')[-1],
                                dirname+'/'+self.actionpath[3][2].split('/')[-1],
                            ],
                            "v":[5,5],
                            "skill":[self.customskill[0],self.customskill[1],self.customskill[2]],
                            "skillCD":[0.5,1,1.5],
                        }]
                json.dump(info,mc)
            with open ('Resource/json/player_choose','r') as gcfile:
                single_choose_p=[]
                character_file=[]
                data=json.load(gcfile)
                num=data[0]["pointer"]+1
                for i in range(0,len(data[0]["data"])):
                    single_choose_p.append(data[0]["data"][i]["pic"])
                    character_file.append(data[0]["data"][i]["config_file"])
            with open ('Resource/json/player_choose','w') as gcfile2:
                data = []
                for i in range(0,len(character_file)):
                    data.append({"config_file":character_file[i],"pic":single_choose_p[i]})
                data.append({"config_file": 'Resource/json/'+time.strftime('%Y%m%d%H%M',time.localtime(time.time())),"pic": dirname+'/'+self.actionpath[0][0].split('/')[-1]})
                info2 = [{
                    "pointer": num,
                    "data":data,
                    }]
                json.dump(info2,gcfile2)

class CustomG():
    def __init__(self):
        self.back = pygame.transform.smoothscale(
                pygame.image.load("Resource/interface/customgbk.png").convert_alpha(),
                (960,600)
            )
        self.pic = pygame.transform.smoothscale(
                pygame.image.load("Resource/singleplayergame/game1/background3.jpg").convert_alpha(),
                custom_G_face_size
            )
        self.enemy_pic = [
            pygame.transform.smoothscale(
                pygame.image.load("Resource/enemy/enemy1/enemy1_static.jpeg").convert_alpha(),
                (30, 30)
            ),
            pygame.transform.smoothscale(
                pygame.image.load("Resource/enemy/enemy2/enemy2_static.png").convert_alpha(),
                (30, 30)
            ),
            pygame.transform.smoothscale(
                pygame.image.load("Resource/enemy/enemy3/enemy3_static.png").convert_alpha(),
                (30, 30)
            ),
        ]
        self.ob_pic = [
            pygame.transform.smoothscale(
                pygame.image.load("Resource/item/ob1.png").convert_alpha(),
                (30, 30)
            ),
            pygame.transform.smoothscale(
                pygame.image.load("Resource/item/ob2.jpg").convert_alpha(),
                (30, 30)
            ),
            pygame.transform.smoothscale(
                pygame.image.load("Resource/item/ob3.jpg").convert_alpha(),
                (30, 30)
            ),
            pygame.transform.smoothscale(
                pygame.image.load("Resource/item/ob4.jpg").convert_alpha(),
                (30, 30)
            ),
        ]
        self.enemy_list = []
        self.obstacle_list = []
        self.choose = 0

    def writeJson(self):
        tempenemy = []
        tempobstacle = [{"site":[0,0],"size":[10000,600],"kind":0}]
        for e in self.enemy_list:
            tempenemy.append({
                "site":[int(96/59*(e[0]-80)),int(60/29*(e[1]-120))],
                "kind": e[2],
            })
        for o in self.obstacle_list:
            tempobstacle.append({
                "site": [int(96/59 * (o[0] - 80)), int(60/29 * (o[1] - 120))],
                "size": [100, 100],
                "kind": o[2],
            })
        with open ("Resource/json/game3",'w') as f:
            data = [{
                "p1_site": [200, 400],
                "bg_pic": "Resource/singleplayergame/game1/background3.jpg",
                "bg_size": [1067, 600],
                "enemy": tempenemy,
                "obstacle": tempobstacle,
            }]
            json.dump(data,f)

