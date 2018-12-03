#
#   创建json文件
#

from define import *

import extern

import pygame
import json

#import main
import start

import Game
import Player
import Item

from pygame.locals import *
from sys import exit

singleplayer_player_pic_static='tmg/static.png'
singleplayer_player_pic_move1='tmg/static.png'
singleplayer_player_pic_move2='tmg/move1.png'
singleplayer_player_pic_attack1='单人游戏人物攻击图片帧1'
singleplayer_player_pic_attack2='单人游戏人物攻击图片帧2'
singleplayer_player_pic_attacked='单人游戏人物被攻击图片帧'
singleplayer_player_velocity=(5,5)

singleplayer_background_pic='background1.jpg'

singleplayer_enemy_pic_static='enemy1_static.png'
singleplayer_enemy_pic_move1='单人游戏敌人移动图片帧1'
singleplayer_enemy_pic_move2='单人游戏敌人移动图片帧2'
singleplayer_enemy_pic_attack1='单人游戏敌人攻击图片帧1'
singleplayer_enemy_pic_attack2='单人游戏敌人攻击图片帧2'
singleplayer_enemy_pic_attacked='单人游戏敌人被攻击图片帧'
info=[singleplayer_background_pic,
    # [singleplayer_player_pic_static,
    # singleplayer_player_pic_move1,
    # singleplayer_player_pic_move2,
    # singleplayer_player_pic_attack1,
    # singleplayer_player_pic_attack2,
    # singleplayer_player_pic_attacked],
    [singleplayer_enemy_pic_static,
    singleplayer_enemy_pic_move1,
    singleplayer_enemy_pic_move2,
    singleplayer_enemy_pic_attack1,
    singleplayer_enemy_pic_attack2,
    singleplayer_enemy_pic_attacked],
    (2160,600),#(58,58),
    (195,138),
    [(700,250),[1000,250]]
]
with open('gametest','w') as checkpointinfo:
    temp=json.dump(info,checkpointinfo)
info=[
    [singleplayer_player_pic_static,
    singleplayer_player_pic_move1,
    singleplayer_player_pic_move2,
    singleplayer_player_pic_attack1,
    singleplayer_player_pic_attack2,
    singleplayer_player_pic_attacked],
    (174,174),
    [(200,200)],
    singleplayer_player_velocity
]
with open('jpx','w') as jpx:
    temp=json.dump(info,jpx)
pygame.quit()