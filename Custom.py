import threading
import pygame
from pygame.locals import *
import extern
from define import *
import json
import time
import Resource
import os
import shutil

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
        self.buttonscale=[[160,290,120,150],[103,894,44,838],[310,437,120,150],[474,600,120,150],[160,290,351,384],[308,437,351,384]]
        self.rolllength=0
        self.fontObj = pygame.font.Font('DejaVuSans.ttf', 20)
        self.actionkind=-1
        self.actioncomplete=[False,False,False,False]
        self.choosestate=0
        self.charactersize=[200,350]
        self.actionpic=[]
        self.actionblitcount=0
        self.actionpath=[[],[],[],[]]
        extern.custom_resource=Resource.RCustom('Resource/json/custom')

    def customshow1(self):
        extern.interface_resource.screen.blit(extern.interface_resource.custom_choose_bk1,(-1,-1))
        [x,y]=pygame.mouse.get_pos()
        x-=extern.interface_resource.cursor.get_width()/2
        y-=extern.interface_resource.cursor.get_width()/2
        extern.interface_resource.screen.blit(extern.interface_resource.cursor,(x,y))

    def customshow2(self):
        extern.interface_resource.screen.blit(extern.interface_resource.custom_choose_bk2,(-1,-1))
        [x,y]=pygame.mouse.get_pos()
        extern.interface_resource.screen.blit(extern.interface_resource.custom_frame,(105,34))
        temp=extern.interface_resource.custom_pic_choose_bk.copy()
        temp.blit(
            extern.interface_resource.custom_pic_choose_bk,
            (0,(self.rolllength+custom_pic_choose_size[1])%custom_pic_choose_size[1]-custom_pic_choose_size[1])
        )
        temp.blit(
            extern.interface_resource.custom_pic_choose_bk,
            (0,(self.rolllength+custom_pic_choose_size[1])%custom_pic_choose_size[1]-3)
            )
        for tx,pic in enumerate(extern.custom_resource.pic):
            rc=[int(tx/5),tx%5]
            if (rc[0]<6.5+self.rolllength/custom_thumbnail_size[1])&(rc[0]+0.5>self.rolllength/custom_thumbnail_size[1]):
                temp.blit(pic,(rc[1]*int(custom_pic_choose_size[0]/5)+20,(self.rolllength+10+rc[0]*(custom_thumbnail_size[1]+90))))
        extern.interface_resource.screen.blit(temp,(120,49))
        x-=extern.interface_resource.cursor.get_width()/2
        y-=extern.interface_resource.cursor.get_width()/2
        extern.interface_resource.screen.blit(extern.interface_resource.cursor,(x,y))
        


    def click_respond1(self,event):
        [x,y]=pygame.mouse.get_pos()
        if(event.type==MOUSEBUTTONDOWN):
            if(event.button==1):
                if ((x<self.buttonscale[0][1])&(x>self.buttonscale[0][0])&(y<self.buttonscale[0][3])&(y>self.buttonscale[0][2])):
                    self.state2init(0)
                elif ((x<self.buttonscale[2][1])&(x>self.buttonscale[2][0])&(y<self.buttonscale[2][3])&(y>self.buttonscale[2][2])):
                    self.state2init(1)
                elif ((x<self.buttonscale[3][1])&(x>self.buttonscale[3][0])&(y<self.buttonscale[3][3])&(y>self.buttonscale[3][2])):    
                    self.state2init(2)
                elif ((x<self.buttonscale[4][1])&(x>self.buttonscale[4][0])&(y<self.buttonscale[4][3])&(y>self.buttonscale[4][2])):    
                    self.state2init(3)
                elif ((x<self.buttonscale[5][1])&(x>self.buttonscale[5][0])&(y<self.buttonscale[5][3])&(y>self.buttonscale[5][2])):
                    self.temptime=extern.last_fresh_time
                    extern.game_state=GAMEINIT
                    if len(self.actionpic)>0:
                        for p in self.actionpic:
                            del p
                    self.actionpic=[]
                    if False not in self.actionpath:
                        self.writejson()
        x-=extern.interface_resource.cursor.get_width()/2
        y-=extern.interface_resource.cursor.get_width()/2
        textSurfaceObj = self.fontObj.render('('+str(x)+','+str(y)+') '+str(self.state), True,(0,0,0),(255,255,255))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (1300,100)
        extern.interface_resource.screen.blit(textSurfaceObj, textRectObj)

    def mouse_respond1(self,event):
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
                    tx=x-120
                    ty=(self.rolllength+10+y-49)
                    if (ty%250)<160:
                        if ((tx%140)>20)&((tx%140)<120):
                            if (int(tx/140)+int(ty/250)*5)<len(extern.custom_resource.pic):
                                self.actionpic.append(
                                    pygame.transform.smoothscale(
                                        pygame.image.load('Resource/custom/'+extern.custom_resource.picpath[int(tx/140)+int(ty/250)*5]
                                        ).convert_alpha(),
                                    self.charactersize))
                                self.actionpath[self.actionkind].append('Resource/custom/'+extern.custom_resource.picpath[int(tx/140)+int(ty/250)*5])
                                self.choosestate=self.choosestate+1
                                self.temptime=extern.last_fresh_time
                                if self.choosestate==3:
                                    self.choosestate=0
                                    self.actioncomplete[self.actionkind]=True
                                    self.state=1

        x-=extern.interface_resource.cursor.get_width()/2
        y-=extern.interface_resource.cursor.get_width()/2
        textSurfaceObj = self.fontObj.render('('+str(x)+','+str(y)+') '+str(self.rolllength), True,(0,0,0),(255,255,255))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (1300,100)
        extern.interface_resource.screen.blit(textSurfaceObj, textRectObj)

    def state2init(self,ak):
        self.state=2
        self.actionkind=ak
        self.temptime=extern.last_fresh_time
        self.actioncomplete[ak]=False
        if len(self.actionpic)>0:
            for p in self.actionpic:
                del p
        self.actionpic=[]
        self.actionpath[self.actionkind]=[]

    def actionblit(self):
        if self.actionkind>-1:
            if self.actioncomplete[self.actionkind]:
                self.actionblitcount=self.actionblitcount+1
                if self.actionblitcount==15:
                    self.actionblitcount=0
                if not extern.game_state==GAMEINIT:
                    extern.interface_resource.screen.blit(self.actionpic[int(self.actionblitcount/5)],(1000,100))

    def writejson(self):
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
            self.customshow1()
            if (extern.last_fresh_time-self.temptime)>0.5:
                self.click_respond1(event)
            self.actionblit()
        elif self.state==2:
            self.customshow2()
            if (extern.last_fresh_time-self.temptime)>0.5:
                self.mouse_respond1(event)
