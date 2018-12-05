# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 16:13:26 2018

@author: Wending_Tang & Kaifeng_Deng
"""

from enum import Enum
from weapon.py import Weapon
from define.py import mainwindow_size
from math import pow
from define import *

class Player_State(Enum):
    station=0
    attacking_normal=1
    moving=2
    attacking_super=3
    attacked=4
    
blow_distance=(1,1)
boundary=(0,0,1920,1080)
PERIOD_MOVE=2
PERIOD_ATTACK=2
PERIOD_ATTACKED=10000

class Player:
    
    def __init__(self, position=(0,0),velocity=(10,10),
                 blood=100,attack=1,defence=1,magic=1,distance=10,
                 state=Player_State.station,signal=NULL):
        self.position=position
        self.velocity=velocity
        self.blood=blood
        self.attack=attack
        self.defence=defence
        self.magic=magic
        self.distance=distance
        self.state=state
        self.signal=NULL
        self.count=0
        
    def move(self, horizontal, vertical):
##        if self.state==Player_State.station:
##            self.state=Player_State.moving
        if self.state==Player_State.moving:
            self.position=self.position+(velocity[0]*horizontal,velocity[1]*vertical)
        if self.position[0]<0:
            self.position[0]=0
        elif self.position[0]>mainwindow_size[0]:
            self.position[0]=mainwindow_size[0]
        if self.position[1]<0:
            self.position[1]=0
        elif self.position[1]>mainwindow_size[1]:
            self.position[1]=mainwindow_size[1]
                
    def being_attacked(self, damage, direction):
##        self.state=Player_State.attacked
##        self.position=self.position+((-1)*direction[0]*blow_distance[0],(-1)*direction[1]*blow_distance[1])
##        if self.position[0]<0:
##            self.position[0]=0
##        elif self.position[0]>mainwindow_size[0]:
##            self.position[0]=mainwindow_size[0]
##        if self.position[1]<0:
##            self.position[1]=0
##        elif self.position[1]>mainwindow_size[1]:
##            self.position[1]=mainwindow_size[1]
##        self.blood-=round(damage*(pow(2,(-1)*self.defence)))
##        if self.blood<=0:
##            self.death()
        
    def attack_release(self):
        self.state=Player_State.station
        
    def attack_normal(self):
##        if self.state==Player_State.moving or self.state==Player_State.station:
##            self.state=Player_State.attacking_normal
        myWeapon=Weapon()
        skill_list.append(myWeapon)
    
    def death(self):
        #此处跳到过场动画

    def update(self):
        if self.state==Player_State.station:
            self.show_pic()
            if self.signal==MOVEUP:
                self.move(0,1)
                self.count=0
                self.state=Player_State.moving
            elif self.signal==MOVEDOWN:
                self.move(0,-1)
                self.count=0
                self.state=Player_State.moving
            elif self.signal==MOVELEFT:
                self.move(-1,0)
                self.count=0
                self.state=Player_State.moving
            elif self.signal==MOVERIGHT:
                self.move(1,0)
                self.count=0
                self.state=Player_State.moving
            elif self.signal==MOVEUPRIGHT:
                self.move(1,1)
                self.count=0
                self.state=Player_State.moving
            elif self.signal==MOVEUPLEFT:
                self.move(-1,1)
                self.count=0
                self.state=Player_State.moving
            elif self.signal==MOVEDOWNRIGHT:
                self.move(1,-1)
                self.count=0
                self.state=Player_State.moving
            elif self.signal==MOVEDOWNLEFT:
                self.move(-1,-1)
                self.count=0
                self.state=Player_State.moving
            elif self.signal==Skill1:
                self.attack_normal()
                self.count=0
                self.state=Player_State.attacking_normal
            elif self.signal=Skill2:
                self.attack_normal()
                self.count=0
                self.state=Player_State.attacking_normal
            elif self.signal==Skill3:
                self.attack_normal()
                self.count=0
                self.state=Player_State.attacking_normal
            elif self.signal==ATTACKED:
                self.count=0
                self.state=Player_State.attacked
        elif self.state==Player_State.moving:
            self.count=(self.count+1) mod PERIOD_MOVE
            self.show_pic()
            if self.signal==MOVEUP:
                self.move(0,1)
                self.state=Player_State.moving
            elif self.signal==MOVEDOWN:
                self.move(0,-1)
                self.state=Player_State.moving
            elif self.signal==MOVELEFT:
                self.move(-1,0)
                self.state=Player_State.moving
            elif self.signal==MOVERIGHT:
                self.move(1,0)
                self.state=Player_State.moving
            elif self.signal==MOVEUPRIGHT:
                self.move(1,1)
                self.state=Player_State.moving
            elif self.signal==MOVEUPLEFT:
                self.move(-1,1)
                self.state=Player_State.moving
            elif self.signal==MOVEDOWNRIGHT:
                self.move(1,-1)
                self.state=Player_State.moving
            elif self.signal==MOVEDOWNLEFT:
                self.move(-1,-1)
                self.state=Player_State.moving
            elif self.signal==Skill1:
                self.attack_normal()
                self.count=0
                self.state=Player_State.attacking_normal
            elif self.signal=Skill2:
                self.attack_normal()
                self.count=0
                self.state=Player_State.attacking_normal
            elif self.signal==Skill3:
                self.attack_normal()
                self.count=0
                self.state=Player_State.attacking_normal                
            elif self.signal==ATTACKED:
                self.count=0
                self.state=Player_State.attacked
        elif self.state==Player_State.attacking_normal:
            self.count=(self.count+1) mod PERIOD_ATTACK
            self.show_pic()
            if self.signal==ATTACKED:
                self.count=0
                self.state=Player_State.attacked
        elif self.state==Player_State.attacking_super:
            self.count=(self.count+1) mod PERIOD_ATTACK
            self.show_pic()
            if self.signal==ATTACKED:
                self.count=0
                self.state=Player_State.attacked
        elif self.state==Player_State.attacked:
            self.count=self.count+1
            self.show_pic()
            if self.count==PERIOD_ATTACKED:
                self.state=Player_State.station
