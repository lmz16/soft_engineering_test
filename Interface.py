#
#   界面显示模块
#

import pygame
from pygame.locals import *

from Define import *
import Extern as Et
import Input as Ip
import Resource as Rs
import InterfaceTest as Itest

test_case = Itest.TInterface()

button_site = {
    "single":(480,400),
    "setting":(480,440),
    "help":(480,480),
    "online":(480,520),
    "custom":(480,560),
}
text_site = {
    "help":(480,300),
    "choose":(630,50),
    "quit":(480,530),
    "step":30,
    "num":12,
}
choose_site = {
    "start":(480,300),
    "b":(300,150),
    "p":(300,450),
    "step1":400,
    "step2":200,
    "range":((100,0),(760,600)),
}
game_file = [
    "Resource/json/game_choose",
    ["Resource/json/game1",]
]

character_file = [
    "Resource/json/character1",
]

enemy_file = [
    "Resource/json/enemy1",
]

obstacle_file = [
    "Resource/json/ob1",
]

skill_file = [
    "Resource/json/sk1",
]

def update(event):
    if Et.game_state == GAMEINIT:
        Et.R_if.screen.blit(Et.R_if.main_bk_pic,(0,0))
        mouseResponseGameInit(event)
        buttonShow()
        cursorShow()
    elif Et.game_state == GAMESETTING:
        Et.R_if.screen.blit(Et.R_if.main_bk_pic,(0,0))
        mouseResponseGameSetting(event)
        settingShow()
        cursorShow()
    elif Et.game_state == GAMEHELP:
        Et.R_if.screen.blit(Et.R_if.main_bk_pic,(0,0))
        mouseResponseGameHelp(event)
        helpShow()
        cursorShow()    
    elif Et.game_state == GAMEINIT1:
        cursorShow()
        Et.R_gc = Rs.RChoose(game_file[0])
        Et.game_state = GAMESINGLECHOOSE
    elif Et.game_state == GAMESINGLECHOOSE:
        Et.R_if.screen.blit(Et.R_gc.bottom_pic,(0,0))
        mouseResponseGameSingleChoose(event)
        singleChooseShow()
        cursorShow()
    elif Et.game_state == GAMELOADSUB:
        Et.R_pl = Rs.RCharacter(character_file[Et.player_choice])
        Et.R_em = Rs.REnemy(enemy_file[Et.game_choice])
        Et.R_ob = Rs.RObstacle(obstacle_file[Et.game_choice])
        Et.R_sk[0] = Rs.RSkill(skill_file[0])
        Et.R_sg = Rs.RSingle(game_file[1][Et.game_choice])
        Et.game_state = GAMELOAD
    elif Et.game_state == GAMELOAD:
        Et.game_state = GAMESTART
    elif Et.game_state == GAMESTART:
        Et.I_ctr.update()
        gameBlit()
        #test_case.test()
    elif Et.game_state == GAMEONLINEINIT1:
        Et.R_pl = Rs.RCharacter(character_file[Et.player_choice])
        Et.R_sg = Rs.RSingle(game_file[1][Et.game_choice])
        Et.game_state = GAMEONLINEINIT2
    elif Et.game_state == GAMEONLINEINIT2:
        Et.game_state = GAMEONLINE
    elif Et.game_state == GAMEONLINE:
        Et.I_ctr.update()
        onlineBlit()

def cursorShow():
    [x,y]=pygame.mouse.get_pos()
    centerBlit(Et.R_if.screen,Et.R_if.cursor_pic,[x,y])

def mouseResponseGameInit(event):
    if Ip.regionMonitor(event,button_site["single"],start_button_size):
        Et.game_state = GAMEINIT1
    if Ip.regionMonitor(event,button_site["setting"],start_button_size):
        Et.game_state = GAMESETTING
    if Ip.regionMonitor(event,button_site["help"],start_button_size):
        Et.game_state = GAMEHELP
    if Ip.regionMonitor(event,button_site["online"],start_button_size):
        Et.game_state = GAMEONLINEINIT1

def mouseResponseGameHelp(event):
    if Ip.regionMonitor(event,text_site["quit"],start_button_size):
        Et.game_state = GAMEINIT

def mouseResponseGameSetting(event):
    if Ip.regionMonitor(event,text_site["quit"],start_button_size):
        Et.game_state = GAMEINIT

def mouseResponseGameSingleChoose(event):
    if Ip.regionMonitor(event,choose_site["start"],start_button_size):
        Et.game_state = GAMELOADSUB
    if Ip.regionMonitor(event,(0,choose_site["b"][1]),start_button_size):
        Et.single_play_move1=Et.single_play_move1+10.0
    if Ip.regionMonitor(event,(mainwindow_size[0],choose_site["b"][1]),start_button_size):
        Et.single_play_move1=Et.single_play_move1-10.0    
    if Ip.regionMonitor(event,(0,choose_site["p"][1]),start_button_size):
        Et.single_play_move2=Et.single_play_move2+10.0
    if Ip.regionMonitor(event,(mainwindow_size[0],choose_site["p"][1]),start_button_size):
        Et.single_play_move2=Et.single_play_move2-10.0
    for i in range(len(Et.R_gc.single_choose_b)):
        if Ip.regionMonitor(event,(choose_site["b"][0]+i*choose_site["step1"]-Et.single_play_move1,choose_site["b"][1]),single_choose_b_size):
            Et.game_choice=i
    for i in range(len(Et.R_gc.single_choose_p)):
        if Ip.regionMonitor(event,(choose_site["p"][0]+i*choose_site["step2"]-Et.single_play_move2,choose_site["p"][1]),single_choose_p_size):
            Et.player_choice=i


def buttonShow():
    centerBlit(Et.R_if.screen,Et.R_if.start_single_pic,button_site["single"])
    centerBlit(Et.R_if.screen,Et.R_if.start_setting_pic,button_site["setting"])
    centerBlit(Et.R_if.screen,Et.R_if.start_help_pic,button_site["help"])
    centerBlit(Et.R_if.screen,Et.R_if.start_online_pic,button_site["online"])
    centerBlit(Et.R_if.screen,Et.R_if.start_custom_pic,button_site["custom"])

def helpShow():
    centerBlit(Et.R_if.screen,Et.R_if.help_text_pic,text_site["help"])

def settingShow():
    centerBlit(Et.R_if.screen,Et.R_if.setting_text_pic,text_site["help"])
    for i in range(0,text_site["num"]):
        centerBlit(Et.R_if.screen,Et.R_if.setting_choose_pic,(text_site["choose"][0],text_site["choose"][1]+i*text_site["step"]))

def singleChooseShow():
    Et.R_if.screen.blit(Et.R_gc.single_choose_frame,(0,0))
    centerBlit(Et.R_if.screen,Et.R_gc.single_choose_play,choose_site["start"])
    Et.R_if.screen.set_clip(choose_site["range"])
    for i in range(len(Et.R_gc.single_choose_b)):
        centerBlit(Et.R_if.screen,Et.R_gc.single_choose_b[i],(choose_site["b"][0]+i*choose_site["step1"]-Et.single_play_move1,choose_site["b"][1]))
    for i in range(len(Et.R_gc.single_choose_p)):
        centerBlit(Et.R_if.screen,Et.R_gc.single_choose_p[i],(choose_site["p"][0]+i*choose_site["step2"]-Et.single_play_move2,choose_site["p"][1]))
    centerBlit(Et.R_if.screen,Et.R_gc.single_choose_bc,(choose_site["b"][0]+Et.game_choice*choose_site["step1"]-Et.single_play_move1,choose_site["b"][1]))
    centerBlit(Et.R_if.screen,Et.R_gc.single_choose_pc,(choose_site["p"][0]+Et.player_choice*choose_site["step2"]-Et.single_play_move2,choose_site["p"][1]))
    Et.R_if.screen.set_clip((0,0),mainwindow_size)

def centerBlit(surface,pic,center):
    dx = int(pic.get_width()/2)
    dy = int(pic.get_height()/2)
    surface.blit(pic,[center[0] - dx,center[1] - dy])

def gameBlit():
    Et.R_sg.bg_pic_temp = Et.R_sg.bg_pic.copy()
    for enemy in Et.Em_info:
        enemyBlit(enemy)
    for ob in Et.Os_info:
        obstacleBlit(ob)
    for sk in Et.Sk_info:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_sk[0].pic, sk.site)
    playerBlit(Et.Pr_info[0])
    Et.R_if.screen.blit(Et.R_sg.bg_pic_temp, blitPoint())

def onlineBlit():
    Et.R_sg.bg_pic_temp = Et.R_sg.bg_pic.copy()
    for p in Et.Pr_info:
        playerBlit(p)
    Et.R_if.screen.blit(Et.R_sg.bg_pic_temp, (0, 0))

def playerBlit(pinfo):
    if pinfo.state == PLAYERSTATIC:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_pl.pic_static[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)
    elif pinfo.state == PLAYERMOVE:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_pl.pic_move[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)
    elif pinfo.state in [PLAYERATTACK,PLAYERSKILL1,PLAYERSKILL2,PLAYERSKILL3]:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_pl.pic_attack[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)
    elif pinfo.state == PLAYERATTACKED:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_pl.pic_attacked[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)

def enemyBlit(einfo):
    if einfo.state == ENEMYSTATIC:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_em.pic_static[int(einfo.count / 4)][einfo.pic_direction], einfo.site)
    elif einfo.state in [ENEMYMOVE,ENEMYPATROL]:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_em.pic_move[int(einfo.count / 4)][einfo.pic_direction], einfo.site)
    elif einfo.state in [ENEMYATTACK]:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_em.pic_attack[int(einfo.count / 4)][einfo.pic_direction], einfo.site)
    elif einfo.state == ENEMYATTACKED:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_em.pic_attacked[int(einfo.count / 4)][einfo.pic_direction], einfo.site)

def obstacleBlit(oinfo):
    if not oinfo.transparent:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_ob.pic, oinfo.site)

def blitPoint():
    x,y = 0,0
    if Et.Pr_info[0].site[0] <= mainwindow_size[0]/2:
        x = 0
    elif Et.Pr_info[0].site[0] >= Et.R_sg.size[0] - mainwindow_size[0]/2:
        x = mainwindow_size[0] - Et.R_sg.size[0]
    else:
        x = mainwindow_size[0]/2 - Et.Pr_info[0].site[0]
    return [x,y]

