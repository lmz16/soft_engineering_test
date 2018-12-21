#
#   创建json文件
#

import json
from sys import exit
import os

singleplayer_player_pic_static='Resource/character/tmg/static.png'
singleplayer_player_pic_move1='Resource/character/tmg/static.png'
singleplayer_player_pic_move2='Resource/character/tmg/move1.png'
singleplayer_player_pic_attack1='Resource/character/tmg/attack0.png'
singleplayer_player_pic_attack2='Resource/character/tmg/attack1.png'
singleplayer_player_pic_attacked='Resource/character/tmg/move1.png'
singleplayer_player_velocity=(10,10)

singleplayer_background_pic='Resource/singleplayergame/game1/background1.png'

singleplayer_enemy_pic_static='Resource/enemy/enemy1/enemy1_static.jpeg'
singleplayer_enemy_pic_move1='Resource/enemy/enemy1/enemy1_static.jpeg'
singleplayer_enemy_pic_move2='Resource/enemy/enemy1/enemy1_static.jpeg'
singleplayer_enemy_pic_attack1='Resource/enemy/enemy1/enemy1_static.jpeg'
singleplayer_enemy_pic_attack2='Resource/enemy/enemy1/enemy1_static.jpeg'
singleplayer_enemy_pic_attacked='Resource/enemy/enemy1/enemy1_static.jpeg'

fire_ball_pic='Resource/item/fire_ball.png'
fire_ball_pic_size=[30,28]
fire_ball_duration=5
fire_ball_velocity=20
fire_ball_damage=300
skill1_cd=2
skill2_cd=3
skill3_cd=4

info=[
    [singleplayer_player_pic_static,
    singleplayer_player_pic_move1,
    singleplayer_player_pic_move2,
    singleplayer_player_pic_attack1,
    singleplayer_player_pic_attack2,
    singleplayer_player_pic_attacked],
    (87,87),
    [(200,200)],
    singleplayer_player_velocity,
    [skill1_cd,skill2_cd,skill3_cd]
]
with open('Resource/json/jpx','w') as jpx:
    temp=json.dump(info,jpx)

start_background_filename='Resource/interface/start_interface.jpg'
#   光标图片路径
cursor_filename='Resource/interface/cursor.png'
#   开始按钮图片路径 单人游戏，联机对战，设置，帮助，自定义
start_button_filename='Resource/interface/start_button_single.png'
start_button_online_filename='Resource/interface/start_button_online.png'
start_button_setting_filename='Resource/interface/start_button_setting.png'
start_button_help_filename='Resource/interface/start_button_help.png'
start_button_custom_filename='Resource/interface/start_button_custom.png'
help_text_filename='Resource/interface/help_text.png'
single_choose_background_filename='Resource/interface/single_choose_background.png'
single_choose_b1_filename='Resource/interface/single_choose_b1.png'
single_choose_b2_filename='Resource/interface/single_choose_b2.png'
single_choose_b3_filename='Resource/interface/single_choose_b3.png'
single_choose_p1_filename='Resource/interface/single_choose_p1.png'
single_choose_p2_filename='Resource/interface/single_choose_p2.png'
single_choose_p3_filename='Resource/interface/single_choose_p3.png'
single_choose_play_filename='Resource/interface/single_choose_play.png'
single_choose_choose_filename='Resource/interface/single_choose_choose.png'
custom_choose='Resource/interface/custom_choose.png'
custom_choose_bk='Resource/interface/custom_choose_bk.png'
custom_pic_choose_bk='Resource/interface/pic_choose_bk.png'
custom_frame='Resource/interface/frame.png'
info = [
    start_background_filename,
    cursor_filename,
    start_button_filename,
    start_button_online_filename,
    start_button_setting_filename,
    start_button_help_filename,
    start_button_custom_filename,
    help_text_filename,
    single_choose_background_filename,
    single_choose_b1_filename,
    single_choose_b2_filename,
    single_choose_b3_filename,
    single_choose_p1_filename,
    single_choose_p2_filename,
    single_choose_p3_filename,
    single_choose_play_filename,
    single_choose_choose_filename,
    [custom_choose,
    custom_choose_bk],
    custom_pic_choose_bk,
    custom_frame
]
with open('Resource/json/interface','w') as interface:
    temp=json.dump(info,interface)

info = [
    singleplayer_background_pic,
    (2160,600),
    [[700,250],[1000,250],[1250,100],[1250,500]]
]

with open('Resource/json/singlegame1','w') as game:
    temp=json.dump(info,game)

info = [
    [singleplayer_enemy_pic_static,
    singleplayer_enemy_pic_move1,
    singleplayer_enemy_pic_move2,
    singleplayer_enemy_pic_attack1,
    singleplayer_enemy_pic_attack2,
    singleplayer_enemy_pic_attacked],
    [60,69],
    [1000,1000,1000,1000],
    3
]

with open('Resource/json/enemy1','w') as enemy:
    temp=json.dump(info,enemy)

info = [
    [fire_ball_pic],
    fire_ball_pic_size,
    fire_ball_duration,
    fire_ball_velocity,
    fire_ball_damage,
    True,
    1
]

with open('Resource/json/skill1','w') as skill:
    temp=json.dump(info,skill)

info = [
    [fire_ball_pic],
    fire_ball_pic_size,
    fire_ball_duration,
    fire_ball_velocity,
    fire_ball_damage,
    True,
    2
]

with open('Resource/json/skill2','w') as skill:
    temp=json.dump(info,skill)

info = [
    [fire_ball_pic],
    fire_ball_pic_size,
    fire_ball_duration,
    fire_ball_velocity,
    fire_ball_damage,
    True,
    3
]

pic=[]
for x in os.listdir('Resource/custom'):
    pic.append(x)

info=[pic]

with open('Resource/json/custom','w') as skill:
    temp=json.dump(info,skill)

