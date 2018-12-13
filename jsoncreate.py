#
#   创建json文件
#

import json
from sys import exit

singleplayer_player_pic_static='Resource/character/tmg/static.png'
singleplayer_player_pic_move1='Resource/character/tmg/static.png'
singleplayer_player_pic_move2='Resource/character/tmg/move1.png'
singleplayer_player_pic_attack1='Resource/character/tmg/attack0.png'
singleplayer_player_pic_attack2='Resource/character/tmg/attack1.png'
singleplayer_player_pic_attacked='Resource/character/tmg/move1.png'
singleplayer_player_velocity=(10,10)
singleplayer_player_max_life=1000
singleplayer_player_max_mana=1000

singleplayer_background_pic='Resource/singleplayergame/game1/background1.jpg'

singleplayer_enemy_pic_static='Resource/enemy/enemy1/enemy1_static.jpeg'
singleplayer_enemy_pic_move1='Resource/enemy/enemy1/enemy1_static.jpeg'
singleplayer_enemy_pic_move2='Resource/enemy/enemy1/enemy1_static.jpeg'
singleplayer_enemy_pic_attack1='Resource/enemy/enemy1/enemy1_static.jpeg'
singleplayer_enemy_pic_attack2='Resource/enemy/enemy1/enemy1_static.jpeg'
singleplayer_enemy_pic_attacked='Resource/enemy/enemy1/enemy1_static.jpeg'

fire_ball_pic='Resource/item/fire_ball.png'
fire_ball_pic_size=(61,56)
fire_ball_duration=5
fire_ball_velocity=20
fire_ball_damage=300
skill1_cd=2

info=[
    [singleplayer_player_pic_static,
    singleplayer_player_pic_move1,
    singleplayer_player_pic_move2,
    singleplayer_player_pic_attack1,
    singleplayer_player_pic_attack2,
    singleplayer_player_pic_attacked],
    (174,174),
    [(200,200)],
    singleplayer_player_velocity,
    skill1_cd,
#12月8日晚谢福生改动
    singleplayer_player_max_life,
    singleplayer_player_max_mana,
    fire_ball_pic
#12月8日晚谢福生改动
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
#12月13日谢福生改动
setting_text_filename='Resource/interface/setting_text.png'
setting_choose_filename='Resource/interface/setting_choose.png'
#12月13日谢福生改动
single_choose_background_filename='Resource/interface/single_choose_background.jpg'
single_choose_background2_filename='Resource/interface/single_choose_background.png'
single_choose_b1_filename='Resource/interface/single_choose_b1.png'
single_choose_b2_filename='Resource/interface/single_choose_b2.png'
single_choose_b3_filename='Resource/interface/single_choose_b3.png'
single_choose_p1_filename='Resource/interface/single_choose_p1.png'
single_choose_p2_filename='Resource/interface/single_choose_p2.png'
single_choose_p3_filename='Resource/interface/single_choose_p3.png'
single_choose_play_filename='Resource/interface/single_choose_play.png'
single_choose_choose_filename='Resource/interface/single_choose_choose.png'

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
    single_choose_background2_filename,
    #12月13日谢福生改动
    setting_text_filename,
    setting_choose_filename
    #12月13日谢福生改动
]

with open('Resource/json/interface','w') as interface:
    temp=json.dump(info,interface)

#12月8日晚谢福生改动
single_game_hpmp_filename='Resource/interface/single_game_hpmp.png'
single_game_hp_filename='Resource/interface/single_game_hp.png'
single_game_mp_filename='Resource/interface/single_game_mp.png'
gameinterface_filename='Resource/interface/gameinterface.png'
single_game_smallplayer_filename='Resource/interface/single_game_smallplayer.png'
#12月8日晚谢福生改动

info = [
    singleplayer_background_pic,
    (2160,900),
    [[700,250],[1000,250]],
    #12月8日晚谢福生改动
    single_game_hpmp_filename,
    single_game_hp_filename,
    single_game_mp_filename,
    gameinterface_filename,
    single_game_smallplayer_filename
    #12月8日晚谢福生改动
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
    [120,138],
    [1000,1000],
    3
]

with open('Resource/json/enemy1','w') as enemy:
    temp=json.dump(info,enemy)

info = [
    [fire_ball_pic],
    fire_ball_pic_size,
    fire_ball_duration,
    fire_ball_velocity,
    fire_ball_damage
]

with open('Resource/json/skill1','w') as skill:
    temp=json.dump(info,skill)
