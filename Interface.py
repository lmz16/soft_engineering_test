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
import json
import Custom

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
single_site = {
    "portrait":(435,535),
    "hp":(480,580),
    "skill":(480,535),
    "smallmap":(860,550),
    "smallplayer":(770,510),
    "step":30,
}
custom_choose_site = {
    "back":(150,100),
    "c1":(250,350),
    "c2":(650,350),
    "backsize":(200,100),
    "csize":(400,300),
}
custom_c_site = {
    "static":(140,83),
    "attack":(249,83),
    "move":(357,83),
    "skill":(140,245),
    "ok":(249,245),
    "buttom_size":(90,30),
}
game_file = [
    "Resource/json/game_choose",
    ["Resource/json/game1","Resource/json/game2"]
]

enemy_file = [
    "Resource/json/enemy1",
    "Resource/json/enemy1",
]

obstacle_file = [
    "Resource/json/ob1",
    "Resource/json/ob1",
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
        Et.R_pl = Rs.RCharacter(Et.R_gc.character_file[Et.player_choice])
        Et.R_em = Rs.REnemy(enemy_file[Et.game_choice])
        Et.R_ob = Rs.RObstacle(obstacle_file[Et.game_choice])
        for i in range(0,SKILLMAXINDEX):
            Et.R_sk[i] = Rs.RSkill(skill_file[i])
        Et.R_sg = Rs.RSingle(game_file[1][Et.game_choice])
        Et.game_state = GAMELOAD
    elif Et.game_state == GAMELOAD:
        Et.game_state = GAMESTART
    elif Et.game_state == GAMESTART:
        Et.I_ctr.update()
        gameBlit()
        if Et.over_count == 50:
            Et.over_count = 0
            Et.game_state = GAMESINGLECHOOSE
            mydel()
        #test_case.test()
    elif Et.game_state == GAMEONLINEINIT1:
        Et.R_gc = Rs.RChoose(game_file[0])
        Et.R_pl = Rs.RCharacter(Et.R_gc.character_file[Et.player_choice])
        Et.R_sg = Rs.RSingle(game_file[1][Et.game_choice])
        Et.R_og = Rs.ROnline()
        for i in range(0,SKILLMAXINDEX):
            Et.R_sk[i] = Rs.RSkill(skill_file[i])
        Et.game_state = GAMEONLINEINIT2
        Et.Pr_info = []
    elif Et.game_state == GAMEONLINEINIT2:
        Et.game_state = GAMEONLINE
    elif Et.game_state == GAMEONLINE:
        Et.I_ctr.update()
        onlineBlit()
    elif Et.game_state == GAMECUSTOMCHOOSE:
        Et.R_if.screen.blit(Et.R_if.main_bk_pic, (0, 0))
        Et.R_if.screen.blit(Et.R_if.custom_choose_choose_pic, (0, 0))
        mouseResponseGameCustomChoose(event)
        cursorShow()
        if Et.R_cu:
            del Et.R_cu
        #   Et.R_cu=Custom.CustomC()

        # elif(Et.game_state==GAMECUSTOMC):
        #     Et.R_cu=Custom.CustomC()
        #     customCShow1()
        #     if (Et.fresh_time-Et.R_cu.temptime)>0.5:
        #         mouseResponseGameCustomC(event)
        #     customCActionshow()
        # elif(Et.game_state==GAMECUSTOMC2):
        #     self.customShow2()
        #     if (Et.fresh_time-self.temptime)>0.5:
        #         self.mouseRespond1(event)
    elif Et.game_state == GAMECUSTOMG:
        if Et.C_G:
            del Et.C_G
        Et.C_G = Custom.CustomG()
        Et.game_state = GAMECUSTOMG2
    elif Et.game_state == GAMECUSTOMG2:
        customGShow1()
        mouseResponseCustomG(event)
        cursorShow()
        if Et.C_G.choose == 7:
            Et.game_state = GAMEINIT
            Et.C_G.writeJson()

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
    if Ip.regionMonitor(event, button_site["custom"], start_button_size):
        Et.game_state = GAMECUSTOMCHOOSE

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

def mouseResponseGameCustomChoose(event):
    if Ip.regionMonitor(event, custom_choose_site["back"], custom_choose_site["backsize"]):
        Et.game_state = GAMEINIT
    if Ip.regionMonitor(event, custom_choose_site["c1"], custom_choose_site["csize"]):
        Et.game_state = GAMECUSTOMC
    if Ip.regionMonitor(event, custom_choose_site["c2"], custom_choose_site["csize"]):
        Et.game_state = GAMECUSTOMG

def mouseResponseGameCustomC(event):
    if Ip.regionMonitor(event,custom_c_site["static"],custom_c_site["buttom_size"]):
        Et.game_state=GAMECUSTOMC2
        Et.R_cu.state2init(0)
    if Ip.regionMonitor(event,custom_c_site["attack"],custom_c_site["buttom_size"]):
        Et.game_state=GAMECUSTOMC2
        Et.R_cu.state2init(1)
    if Ip.regionMonitor(event,custom_c_site["move"],custom_c_site["buttom_size"]):
        Et.game_state=GAMECUSTOMC2
        Et.R_cu.state2init(2)
    if Ip.regionMonitor(event,custom_c_site["skill"],custom_c_site["buttom_size"]):
        Et.game_state=GAMECUSTOMC2
        Et.R_cu.state2init(3)
    if Ip.regionMonitor(event,custom_c_site["ok"],custom_c_site["buttom_size"]):
        Et.R_cu.temptime=Et.fresh_time
        Et.game_state=GAMEINIT
        if len(Et.R_cu.actionpic)>0:
            for p in Et.R_cu.actionpic:
                del p
        Et.R_cu.actionpic=[]
        if False not in Et.R_cu.actionpath:
            Et.R_cu.writeJson()


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

def customCShow1():
    Et.R_if.screen.blit(Et.R_if.custom_choose_pic,(-1,-1))
    [x,y]=pygame.mouse.get_pos()
    centerBlit(Et.R_if.screen,Et.R_if.cursor_pic,[x,y])

def customCActionshow():
        if Et.R_cu.actionkind>-1:
            if Et.R_cu.actioncomplete[Et.R_cu.actionkind]:
                Et.R_cu.actionblitcount=Et.R_cu.actionblitcount+1
                if Et.R_cu.actionblitcount==15:
                    Et.R_cu.actionblitcount=0
                if not Et.game_state==GAMEINIT:
                    Et.R_if.screen.blit(Et.R_cu.actionpic[int(Et.R_cu.actionblitcount/5)],(650,67))

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
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_sk[sk.kind].pic, sk.site)
        if sk.draw_line != None:
            pygame.draw.line(Et.R_sg.bg_pic_temp, (0,0,0), sk.draw_line[0], sk.draw_line[1], 5)
    playerBlit(Et.Pr_info[0])
    Et.R_if.screen.blit(Et.R_sg.bg_pic_temp, blitPoint())
    Et.R_if.screen.blit(Et.R_if.single_frame_pic, (0, 0))
    centerBlit(Et.R_if.screen, Et.R_gc.single_portrait[Et.player_choice], single_site["portrait"])
    centerBlit(Et.R_if.screen, Et.R_if.single_hp_pic, (
    single_site["hp"][0] + ((Et.Pr_info[0].life_value - Et.R_pl.max_life) * single_game_hp_size[0] / Et.R_pl.max_life),
    single_site["hp"][1]))
    for i in range(0, 3):
        centerBlit(Et.R_if.screen, Et.R_sk[Et.R_pl.skill[i]].single_game_skill,
            (single_site["skill"][0] + i * single_site["step"], single_site["skill"][1]))
    centerBlit(Et.R_if.screen, Et.R_sg.small_map_pic, single_site["smallmap"])
    centerBlit(Et.R_if.screen, Et.R_if.single_game_smallplayer_pic, (
    single_site["smallplayer"][0] + Et.Pr_info[0].site[0] / Et.R_sg.size[0] * single_game_map_size[0],
    single_site["smallplayer"][1] + Et.Pr_info[0].site[1] / Et.R_sg.size[1] * single_game_map_size[1]))
    if Et.S_game.over == 1:
        centerBlit(Et.R_if.screen, Et.R_if.vic_pic, [mainwindow_size[0]/2,mainwindow_size[1]/2])
        Et.over_count += 1
    elif Et.S_game.over == 2:
        centerBlit(Et.R_if.screen, Et.R_if.lose_pic, [mainwindow_size[0] / 2, mainwindow_size[1] / 2])
        Et.over_count += 1

def onlineBlit():
    Et.R_sg.bg_pic_temp = Et.R_sg.bg_pic.copy()
    for p in Et.Pr_info:
        onlinePlayerBlit(p)
    for sk in Et.Sk_info:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_sk[sk.kind].pic, sk.site)
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
    if oinfo.kind != 0:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_ob.pic[oinfo.kind-1], oinfo.site)

def blitPoint():
    x,y = 0,0
    if Et.Pr_info[0].site[0] <= mainwindow_size[0]/2:
        x = 0
    elif Et.Pr_info[0].site[0] >= Et.R_sg.size[0] - mainwindow_size[0]/2:
        x = mainwindow_size[0] - Et.R_sg.size[0]
    else:
        x = mainwindow_size[0]/2 - Et.Pr_info[0].site[0]
    return [x,y]


def customGShow1():
    Et.R_if.screen.blit(Et.C_G.back, (-1,-1))
    Et.R_if.screen.blit(Et.C_G.pic, (30,100))
    for i in range(0,8):
        Et.R_if.screen.blit(Et.C_G.button, (800, 110+50*i))
    for site in Et.C_G.enemy_list:
        Et.R_if.screen.blit(Et.C_G.enemy_pic[0], site)
    for site in Et.C_G.obstacle_list:
        Et.R_if.screen.blit(Et.C_G.ob_pic[0], site)

def mouseResponseCustomG(event):
    for i in range(0,8):
        if Ip.regionMonitor(event,[850,125+50*i],[100,30]):
            Et.C_G.choose = i
    if Ip.regionMonitor(event,[386,280],[700,380]):
        if Et.C_G.choose in [0,1,2]:
            Et.C_G.enemy_list.append(pygame.mouse.get_pos())
        else:
            Et.C_G.obstacle_list.append(pygame.mouse.get_pos())


def mydel():
    Et.R_sg = None
    Et.R_pl = [None]*2


def onlinePlayerBlit(pinfo):
    if pinfo.state == PLAYERSTATIC:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_og.r_player[pinfo.kind].pic_static[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)
    elif pinfo.state == PLAYERMOVE:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_og.r_player[pinfo.kind].pic_move[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)
    elif pinfo.state in [PLAYERATTACK,PLAYERSKILL1,PLAYERSKILL2,PLAYERSKILL3]:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_og.r_player[pinfo.kind].pic_attack[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)
    elif pinfo.state == PLAYERATTACKED:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_og.r_player[pinfo.kind].pic_attacked[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)