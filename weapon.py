# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:29:15 2018

@author: Wending_Tang & Kaifeng_Deng
"""
from define.py import mainwindow_size
from math import pow


class Weapon:
    def __init__(self,damage,velocity,start_position,reach):
        self.damage=damage
        self.velocity=velocity
        self.start_position=start_position
        self.position=self.start_position
        self.reach=reach
        
    def move(self):
        self.position=self.position+(velocity[0]*horizontal,velocity[1]*vertical)
        if self.position[0]<0 or self.position[0]>mainwindow_size[0] or self.position[1]<0 or self.position[1]>mainwindow_size[1]:
            __del__(self)
        if pow((self.position[0]-self.start_position[0]),2)+pow((self.position[1]-self.start_position[1]),2)>=pow(reach,2):
            __del__(self)
            
    