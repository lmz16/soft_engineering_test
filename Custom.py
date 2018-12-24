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
        self.state=1
        self.pic_static=None
        self.pic_move1=None
        self.pic_move2=None
        self.pic_attack1=None
        self.pic_attack2=None
        self.pic_attacked=None
        self.velocity=0
        self.skill_1=None
        self.skill_2=None
        self.skill_3=None
        self.finished=False
        self.buttonscale=[[95,185,68,98],[69,596,29,559],[203,295,68,98],[311,403,68,98],[95,185,231,258],[203,295,231,258]]
        self.button_size=[90,30]
        self.button_site={
            "static":(140,83),
            "attack":(249,83),
            "move":(357,83),
            "skill":(140,245),
            "ok":(249,245),
        }
        self.rolllength=0
        self.fontObj = pygame.font.Font('DejaVuSans.ttf', 20)
        self.actionkind=-1
        self.actioncomplete=[False,False,False,False]
        self.choosestate=0
        self.charactersize=[167,233]
        self.actionpic=[]
        self.actionblitcount=0
        self.actionpath=[[],[],[],[]]
        Et.custommode=Rs.RCustom('Resource/json/custom')

    def customShow1(self):
        Et.R_if.screen.blit(Et.R_if.custom_choose_pic,(-1,-1))
        [x,y]=pygame.mouse.get_pos()
        centerBlit(Et.R_if.screen,Et.R_if.cursor_pic,[x,y])

    def customShow2(self):
        Et.R_if.screen.blit(Et.R_if.custom_choose_bk_pic,(-1,-1))
        [x,y]=pygame.mouse.get_pos()
        Et.R_if.screen.blit(Et.R_if.custom_frame_pic,(70,23))
        temp=Et.R_if.pic_choose_bk_pic.copy()
        temp.blit(
            Et.R_if.pic_choose_bk_pic,
            (0,(self.rolllength+custom_pic_choose_size[1])%custom_pic_choose_size[1]-custom_pic_choose_size[1])
        )
        temp.blit(
            Et.R_if.pic_choose_bk_pic,
            (0,(self.rolllength+custom_pic_choose_size[1])%custom_pic_choose_size[1]-3)
            )
        for tx,pic in enumerate(Et.custommode.pic):
            rc=[int(tx/5),tx%5]
            if (rc[0]<6.5+self.rolllength/custom_thumbnail_size[1])&(rc[0]+0.5>self.rolllength/custom_thumbnail_size[1]):
                temp.blit(pic,(rc[1]*int(custom_pic_choose_size[0]/5)+17,(self.rolllength+10+rc[0]*(custom_thumbnail_size[1]+60))))
        Et.R_if.screen.blit(temp,(80,33))
        centerBlit(Et.R_if.screen,Et.R_if.cursor_pic,[x,y])

    def clickRespond1(self,event):
        if Ip.regionMonitor(event,self.button_site["static"],self.button_size):
            self.state2init(0)
        if Ip.regionMonitor(event,self.button_site["attack"],self.button_size):
            self.state2init(1)
        if Ip.regionMonitor(event,self.button_site["move"],self.button_size):
            self.state2init(2)
        if Ip.regionMonitor(event,self.button_site["skill"],self.button_size):
            self.state2init(3)
        if Ip.regionMonitor(event,self.button_site["ok"],self.button_size):
            self.temptime=Et.fresh_time
            Et.game_state=GAMEINIT
            if len(self.actionpic)>0:
                for p in self.actionpic:
                    del p
            self.actionpic=[]
            if False not in self.actionpath:
                self.writeJson()
        x-=Et.R_if.cursor_pic.get_width()/2
        y-=Et.R_if.cursor_pic.get_width()/2
        textSurfaceObj = self.fontObj.render('('+str(x)+','+str(y)+') '+str(self.state), True,(0,0,0),(255,255,255))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (867,67)
        Et.R_if.screen.blit(textSurfaceObj, textRectObj)

    def mouseRespond1(self,event):
        [x,y]=pygame.mouse.get_pos()
        if(event.type == MOUSEBUTTONUP):
            if ((x<self.buttonscale[1][1])&(x>self.buttonscale[1][0])&(y<self.buttonscale[1][3])&(y>self.buttonscale[1][2])):
                if(event.button==4):
                    if self.rolllength<-11:
                        self.rolllength=self.rolllength+10
                elif(event.button==5):
                        self.rolllength=self.rolllength-10
        
        if (event.type == MOUSEBUTTONDOWN):
            if ((x<self.buttonscale[1][1])&(x>self.buttonscale[1][0])&(y<self.buttonscale[1][3])&(y>self.buttonscale[1][2])):
                if (event.button==1):
                    tx=x-85
                    ty=(self.rolllength+10+y-60)
                    if (ty%160)<107:
                        if ((tx%100)>17)&((tx%100)<80):
                            if (int(tx/100)+int(ty/160)*5)<len(Et.custommode.pic):
                                self.actionpic.append(
                                    pygame.transform.smoothscale(
                                        pygame.image.load('Resource/custom/'+Et.custommode.picpath[int(tx/100)+int(ty/160)*5]
                                        ).convert_alpha(),
                                    self.charactersize))
                                self.actionpath[self.actionkind].append('Resource/custom/'+Et.custommode.picpath[int(tx/100)+int(ty/160)*5])
                                self.choosestate=self.choosestate+1
                                self.temptime=Et.fresh_time
                                if self.choosestate==3:
                                    self.choosestate=0
                                    self.actioncomplete[self.actionkind]=True
                                    self.state=1

        x-=Et.R_if.cursor_pic.get_width()/2
        y-=Et.R_if.cursor_pic.get_width()/2
        textSurfaceObj = self.fontObj.render('('+str(x)+','+str(y)+') '+str(self.rolllength), True,(0,0,0),(255,255,255))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (867,67)
        Et.R_if.screen.blit(textSurfaceObj, textRectObj)

    def state2init(self,ak):
        self.actionkind=ak
        self.temptime=Et.fresh_time
        self.actioncomplete[ak]=False
        if len(self.actionpic)>0:
            for p in self.actionpic:
                del p
        self.actionpic=[]
        self.actionpath[self.actionkind]=[]

    def actionBlit(self):
        if self.actionkind>-1:
            if self.actioncomplete[self.actionkind]:
                self.actionblitcount=self.actionblitcount+1
                if self.actionblitcount==15:
                    self.actionblitcount=0
                if not Et.game_state==GAMEINIT:
                    Et.R_if.screen.blit(self.actionpic[int(self.actionblitcount/5)],(650,67))

    def writeJson(self):
        dirname='Resource/character/'+time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        os.mkdir(dirname)
        filename=[*self.actionpath[0],*self.actionpath[1],*self.actionpath[2],*self.actionpath[3]]
        filename=list({}.fromkeys(filename).keys()) 
        for x in filename:
            shutil.copyfile(x,dirname+'/'+x.split('/')[-1])
        with open ('Resource/json/'+time.strftime('%Y%m%d%H%M',time.localtime(time.time())),'w') as mc:
            info = [
                [dirname+'/'+self.actionpath[0][0].split('/')[-1],
                dirname+'/'+self.actionpath[1][0].split('/')[-1],
                dirname+'/'+self.actionpath[1][1].split('/')[-1],
                dirname+'/'+self.actionpath[2][0].split('/')[-1],
                dirname+'/'+self.actionpath[2][1].split('/')[-1],
                dirname+'/'+self.actionpath[3][0].split('/')[-1]],
                (75,123),
                [(200,200)],
                (10,10),
                [2,3,4]
            ]
            json.dump(info,mc)

    def update(self,event):
        if self.state==1:
            self.customShow1()
            if (Et.fresh_time-self.temptime)>0.5:
                self.clickRespond1(event)
            self.actionBlit()
        elif self.state==2:
            self.customShow2()
            if (Et.fresh_time-self.temptime)>0.5:
                self.mouseRespond1(event)
def centerBlit(surface,pic,center):
    dx = int(pic.get_width()/2)
    dy = int(pic.get_height()/2)
    surface.blit(pic,[center[0] - dx,center[1] - dy])


class CustomG():
    def __init__(self):
        self.back = pygame.transform.smoothscale(
                pygame.image.load("Resource/interface/customgbk.png").convert_alpha(),
                (960,600)
            )
        self.pic = pygame.transform.smoothscale(
                pygame.image.load("Resource/singleplayergame/game1/background3.jpg").convert_alpha(),
                (712,400)
            )
        self.button = pygame.transform.smoothscale(
                pygame.image.load("Resource/interface/custombutton.png").convert_alpha(),
                (100,30)
            )
        self.enemy_pic = [
            pygame.transform.smoothscale(
                pygame.image.load("Resource/enemy/enemy1/enemy1_static.jpeg").convert_alpha(),
                (30, 30)
            )
        ]
        self.ob_pic = [
            pygame.transform.smoothscale(
                pygame.image.load("Resource/item/ob1.png").convert_alpha(),
                (30, 30)
            )
        ]
        self.enemy_list = []
        self.obstacle_list = []
        self.choose = 0

    def writeJson(self):
        tempenemy = []
        tempobstacle = []
        for e in self.enemy_list:
            tempenemy.append({
                "site":[int(1.5*e[0]-15),int(1.5*e[1]-15)],
                "kind": 0
            })
        for o in self.obstacle_list:
            tempobstacle.append({
                "site": [int(1.5 * o[0] - 15), int(1.5 * o[1] - 15)],
                "size": [100, 100],
                "kind": 0,
            })
        with open ("Resource/json/game2",'w') as f:
            data = [{
                "p1_site": [200, 400],
                "bg_pic": "Resource/singleplayergame/game1/background3.jpg",
                "bg_size": [1067, 600],
                "enemy": tempenemy,
                "obstacle": tempobstacle,
            }]
            json.dump(data,f)

