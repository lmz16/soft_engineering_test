#
#   创建json文件
#

from define import *

import extern

import pygame
import json

import main
import start

import Game
import Player
import Item

from pygame.locals import *
from sys import exit

background='lm.jpg'
backgroundsize=(3968,2240)
playersize=(58,58)
playerpic='lbk.jpeg'
enemysize=(64,46)
enemypic='paji.png'
enemy1site=[500,2000]
enemy2site=[800,2000]
enemylist=[enemy1site,enemy2site]
info=[background,backgroundsize,playersize,playerpic,enemysize,enemypic,enemylist]
with open('gametest','w') as checkpointinfo:
    temp=json.dump(info,checkpointinfo)
    print (temp)
