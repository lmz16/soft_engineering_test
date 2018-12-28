#
#   界面显示模块
#

import pygame
from pygame.locals import *

from Define import *
import Extern as Et
import Input as Ip
import Resource as Rs
import MainFunc as Mf
import InterfaceTest as Itest
import json
import Custom

test_case = Itest.TInterface()

button_site = {
    "single":(480,364),
    "help":(480,560),
    "online":(480,432),
    "custom":(480,495),
}
#谢福生12月26日修改
text_site = {
    "help":(480,300),
    "quit":(688,444),
    "quitsize":(45,60),
}
choose_site = {
    "start":(345,315),
    "back":(625,315),
    "b":(300,150),
    "p":(300,450),
    "roll":((80,160),(900,160),(80,480),(900,480)),
    "rollsize":(60,60),
    "step1":400,
    "step2":200,
    "range":((100,0),(760,600)),
}
online_choose_site = {
    "start":(760,525),
    "back":(880,525),
    "p":(300,300),
    "roll":((80,300),(900,300)),
    "rollsize":(60,60),
    "step2":200,
    "range":((100,0),(760,600)),
    "backsize":(100,100),
}
single_site = {
    "portrait":(420,520),
    "hp":(480,567),
    "skill":(481,510),
    "smallmap":(870,530),
    "smallplayer":(740,460),
    "state":(480,550),
    "step":45,
}
custom_choose_site = {
    "back":(880,525),
    "c1":(265,310),
    "c2":(683,315),
    "backsize":(100,100),
    "csize":(310,290),
}
custom_c_site = {
    "static":(108,475),
    "attack":(253,475),
    "move":(399,475),
    "attacked":(108,535),
    "skill":(253,535),
    "back":(855,535),
    "ok":(855,475),
    "pow":(553,475),
    "agi":(705,475),
    "int":(705,535),
    "show":(68,51),
    "choose":(480,300),
    "choose_size":(480,300),
    "action":(680,90),
}
custom_G_site = {
    "button":(805,105),
    "step":60,
    "back":(875,518),
    "button_size":(100,50),
    "back_size":(100,100),
    "face":(375,265)
}
#谢福生12月26日修改
game_file = [
    "Resource/json/game_choose",
    ["Resource/json/game1","Resource/json/game2","Resource/json/game3"]
]

enemy_file = [
    "Resource/json/enemy1",
]

obstacle_file = [
    "Resource/json/ob1",
]

def update(event):
    if Et.game_state == GAMEINIT:
        Et.R_if.screen.blit(Et.R_if.main_bk_pic,(0,0))
        mouseResponseGameInit(event)
        cursorShow()
    elif Et.game_state == GAMEHELP:
        Et.R_if.screen.blit(Et.R_if.main_bk_pic,(0,0))
        mouseResponseGameHelp(event)
        helpShow()
        cursorShow()    
    elif Et.game_state == GAMEINIT1:
        cursorShow()
        Et.R_gc = Rs.RChoose(game_file[0],"Resource/json/player_choose")
        Et.game_state = GAMESINGLECHOOSE
    elif Et.game_state == GAMESINGLECHOOSE:
        Et.R_if.screen.blit(Et.R_gc.bottom_pic,(0,0))
        mouseResponseGameSingleChoose(event)
        singleChooseShow()
        cursorShow()
    elif Et.game_state == GAMELOADSUB:
        Et.Pr_info = [None]
        Et.R_pl = Rs.RCharacter(Et.R_gc.character_file[Et.player_choice])
        Et.R_em = Rs.REnemy(enemy_file[0])
        Et.R_ob = Rs.RObstacle(obstacle_file[0])
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
        Mf.netInit()
        Et.R_gc = Rs.RChoose(game_file[0],"Resource/json/player_choose_online")
        Et.R_sg = Rs.RSingle(game_file[1][1])
        Et.R_og = Rs.ROnline()
        Et.R_ob = Rs.RObstacle(obstacle_file[Et.game_choice])
        for i in range(0,SKILLMAXINDEX):
            Et.R_sk[i] = Rs.RSkill(skill_file[i])
        Et.game_state = GAMEONLINECHOOSE
        Et.Pr_info = []
    elif Et.game_state == GAMEONLINECHOOSE:
        Et.R_if.screen.blit(Et.R_if.online_choose_bk_pic,(0,0))
        mouseResponseGameOnlineChoose(event)
        OnlineChooseShow()
        cursorShow()
    elif Et.game_state == GAMEONLINEINIT2:
        Et.game_state = GAMEONLINE
    elif Et.game_state == GAMEONLINE:
        Et.I_ctr.update()
        onlineBlit()
        if Et.over_count == 50:
            Et.over_count = 0
            Et.game_state = GAMEINIT
            Et.R_og = None
            Et.t_net = None
            Et.online_over = 0
    elif Et.game_state == GAMECUSTOMCHOOSE:
        Et.R_if.screen.blit(Et.R_if.main_bk_pic,(0,0))
        Et.R_if.screen.blit(Et.R_if.custom_choose_choose_pic,(0,0))
        if  Et.fresh_time >Et.init_time+0.5:
            mouseResponseGameCustomChoose(event)
        cursorShow() 
    elif(Et.game_state==GAMECUSTOMCLOAD):
        if Et.R_cu:
            del Et.R_cu
        Et.R_cu=Custom.CustomC()
        Et.game_state=GAMECUSTOMC
    elif(Et.game_state==GAMECUSTOMC):
        customC1Show()
        if (Et.fresh_time-Et.R_cu.temptime)>0.5:
            mouseResponseGameCustomC(event)
        customCActionshow()
    elif(Et.game_state==GAMECUSTOMC2):
        customC2Show()
        customCActionshow()
        if (Et.fresh_time-Et.R_cu.temptime)>0.5:
            mouseResponseGameCustomC2(event)
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
    if Ip.regionMonitor(event,button_site["help"],start_button_size):
        Et.game_state = GAMEHELP
    if Ip.regionMonitor(event,button_site["online"],start_button_size):
        Et.game_state = GAMEONLINEINIT1
    if Ip.regionMonitor(event, button_site["custom"], start_button_size):
        Et.game_state = GAMECUSTOMCHOOSE
        Et.init_time = Et.fresh_time

def mouseResponseGameHelp(event):
    if Ip.regionMonitor(event,text_site["quit"],text_site["quitsize"]):
        Et.game_state = GAMEINIT


def mouseResponseGameCustomChoose(event):
    if Ip.regionMonitor(event,custom_choose_site["back"],custom_choose_site["backsize"]):
        Et.game_state = GAMEINIT
    if Ip.regionMonitor(event,custom_choose_site["c1"],custom_choose_site["csize"]):
        Et.game_state = GAMECUSTOMCLOAD
    if Ip.regionMonitor(event,custom_choose_site["c2"],custom_choose_site["csize"]):
        Et.game_state = GAMECUSTOMG  

def mouseResponseGameCustomC(event):
    if Ip.regionMonitor(event,custom_c_site["static"],custom_button_size):
        Et.game_state=GAMECUSTOMC2
        Et.R_cu.actionkind=0
        Et.R_cu.temptime=Et.fresh_time
        Et.R_cu.state2init()
    if Ip.regionMonitor(event,custom_c_site["attack"],custom_button_size):
        Et.game_state=GAMECUSTOMC2
        Et.R_cu.actionkind=1
        Et.R_cu.temptime=Et.fresh_time
        Et.R_cu.state2init()
    if Ip.regionMonitor(event,custom_c_site["move"],custom_button_size):
        Et.game_state=GAMECUSTOMC2
        Et.R_cu.actionkind=2
        Et.R_cu.temptime=Et.fresh_time
        Et.R_cu.state2init()
    if Ip.regionMonitor(event,custom_c_site["attacked"],custom_button_size):
        Et.game_state=GAMECUSTOMC2
        Et.R_cu.actionkind=3
        Et.R_cu.temptime=Et.fresh_time
        Et.R_cu.state2init()
    if Ip.regionMonitor(event,custom_c_site["skill"],custom_button_size):
        Et.game_state=GAMECUSTOMC2
        Et.R_cu.actionkind=4
        Et.R_cu.temptime=Et.fresh_time
        Et.R_cu.state2init()
    if Ip.regionMonitor(event,custom_c_site["pow"],custom_button_size):
        Et.R_cu.characterType=0
    if Ip.regionMonitor(event,custom_c_site["agi"],custom_button_size):
        Et.R_cu.characterType=1
    if Ip.regionMonitor(event,custom_c_site["int"],custom_button_size):
        Et.R_cu.characterType=2
    if Ip.regionMonitor(event,custom_c_site["back"],custom_button_size):
        Et.game_state=GAMEINIT
    if Ip.regionMonitor(event,custom_c_site["ok"],custom_button_size):
        Et.R_cu.temptime=Et.fresh_time
        Et.game_state=GAMEINIT
        if len(Et.R_cu.actionpic)>0:
            for p in Et.R_cu.actionpic:
                del p
        Et.R_cu.actionpic=[]
        if False not in Et.R_cu.actionpath:
            Et.R_cu.writeJson()


def mouseResponseGameCustomC2(event):
        [x,y]=pygame.mouse.get_pos()
        if(event.type == MOUSEBUTTONUP):
            if ((x<570)&(x>70)&(y<423)&(y>23)):
                if(event.button==4):
                    if Et.R_cu.rolllength<-11:
                        Et.R_cu.rolllength=Et.R_cu.rolllength+10
                elif(event.button==5):
                        Et.R_cu.rolllength=Et.R_cu.rolllength-10
        if (event.type == MOUSEBUTTONDOWN):
            if(event.button==1):
                tx=x-85
                ty=(-Et.R_cu.rolllength+10+y-60)
                if (ty%160)<107:
                    if ((tx%100)>17)&((tx%100)<80):
                        if  Et.R_cu.actionkind==4:
                            if (int(tx/100)+int(ty/160)*5)<len(Et.custommode.custom_skill):
                                Et.R_cu.customskill.append(int(tx/100)+int(ty/160)*5)
                                Et.R_cu.choosestate=Et.R_cu.choosestate+1
                                Et.R_cu.temptime=Et.fresh_time
                                Et.R_if.custom_frame_place.append([int(tx/100),int(ty/160)])
                        else:
                            if (int(tx/100)+int(ty/160)*5)<len(Et.custommode.pic):
                                Et.R_cu.actionpic.append(
                                    pygame.transform.smoothscale(
                                        pygame.image.load('Resource/custom/'+Et.custommode.picpath[int(tx/100)+int(ty/160)*5]
                                        ).convert_alpha(),
                                    Et.R_cu.charactersize))
                                Et.R_if.custom_frame_place.append([int(tx/100),int(ty/160)])
                                Et.R_cu.actionpath[Et.R_cu.actionkind].append('Resource/custom/'+Et.custommode.picpath[int(tx/100)+int(ty/160)*5])
                                Et.R_cu.choosestate=Et.R_cu.choosestate+1
                                Et.R_cu.temptime=Et.fresh_time
                        if Et.R_cu.choosestate==3:
                            Et.R_cu.choosestate=0
                            Et.R_cu.actioncomplete[Et.R_cu.actionkind]=True
                            Et.R_if.custom_frame_place=[]
                            Et.game_state=GAMECUSTOMC

def mouseResponseGameSingleChoose(event):
    if Ip.regionMonitor(event,choose_site["start"],start_button_size):
        Et.game_state = GAMELOADSUB
    if Ip.regionMonitor(event,choose_site["back"],start_button_size):
        Et.game_state = GAMEINIT
    if Ip.regionMonitor(event,choose_site["roll"][0],choose_site["rollsize"]):
        Et.single_play_move1=Et.single_play_move1-10.0
    if Ip.regionMonitor(event,choose_site["roll"][1],choose_site["rollsize"]):
        Et.single_play_move1=Et.single_play_move1+10.0    
    if Ip.regionMonitor(event,choose_site["roll"][2],choose_site["rollsize"]):
        Et.single_play_move2=Et.single_play_move2-10.0
    if Ip.regionMonitor(event,choose_site["roll"][3],choose_site["rollsize"]):
        Et.single_play_move2=Et.single_play_move2+10.0
    for i in range(len(Et.R_gc.single_choose_b)):
        if Ip.regionMonitor(event,(choose_site["b"][0]+i*choose_site["step1"]-Et.single_play_move1,choose_site["b"][1]),single_choose_b_size):
            Et.game_choice=i
    for i in range(len(Et.R_gc.single_choose_p)):
        if Ip.regionMonitor(event,(choose_site["p"][0]+i*choose_site["step2"]-Et.single_play_move2,choose_site["p"][1]),single_choose_p_size):
            Et.player_choice=i

def mouseResponseGameOnlineChoose(event):
    if Ip.regionMonitor(event,online_choose_site["start"],online_choose_site["backsize"]):
        Et.game_state = GAMEONLINEINIT2
    if Ip.regionMonitor(event,online_choose_site["back"],online_choose_site["backsize"]):
        Et.game_state = GAMEINIT
    if Ip.regionMonitor(event,online_choose_site["roll"][0],online_choose_site["rollsize"]):
        Et.single_play_move2=Et.single_play_move2-10.0
    if Ip.regionMonitor(event,online_choose_site["roll"][1],online_choose_site["rollsize"]):
        Et.single_play_move2=Et.single_play_move2+10.0   
    for i in range(len(Et.R_gc.single_choose_p)):
        if Ip.regionMonitor(event,(online_choose_site["p"][0]+i*online_choose_site["step2"]-Et.single_play_move2,online_choose_site["p"][1]),single_choose_p_size):
            Et.player_choice=i

def mouseResponseGameCustomChoose(event):
    if Ip.regionMonitor(event, custom_choose_site["back"], custom_choose_site["backsize"]):
        Et.game_state = GAMEINIT
    if Ip.regionMonitor(event, custom_choose_site["c1"], custom_choose_site["csize"]):
        Et.game_state = GAMECUSTOMCLOAD
    if Ip.regionMonitor(event, custom_choose_site["c2"], custom_choose_site["csize"]):
        Et.game_state = GAMECUSTOMG

def helpShow():
    centerBlit(Et.R_if.screen,Et.R_if.help_text_pic,text_site["help"])

def singleChooseShow():
    Et.R_if.screen.blit(Et.R_gc.single_choose_frame,(0,0))
    Et.R_if.screen.set_clip(choose_site["range"])
    for i in range(len(Et.R_gc.single_choose_b)):
        centerBlit(Et.R_if.screen,Et.R_gc.single_choose_b[i],(choose_site["b"][0]+i*choose_site["step1"]-Et.single_play_move1,choose_site["b"][1]))
    for i in range(len(Et.R_gc.single_choose_p)):
        centerBlit(Et.R_if.screen,Et.R_gc.single_choose_p[i],(choose_site["p"][0]+i*choose_site["step2"]-Et.single_play_move2,choose_site["p"][1]))
    centerBlit(Et.R_if.screen,Et.R_gc.single_choose_bc,(choose_site["b"][0]+Et.game_choice*choose_site["step1"]-Et.single_play_move1,choose_site["b"][1]))
    centerBlit(Et.R_if.screen,Et.R_gc.single_choose_pc,(choose_site["p"][0]+Et.player_choice*choose_site["step2"]-Et.single_play_move2,choose_site["p"][1]))
    Et.R_if.screen.set_clip((0,0),mainwindow_size)

def OnlineChooseShow():
    Et.R_if.screen.set_clip(online_choose_site["range"])
    for i in range(len(Et.R_gc.single_choose_p)):
        centerBlit(Et.R_if.screen,Et.R_gc.single_choose_p[i],(online_choose_site["p"][0]+i*online_choose_site["step2"]-Et.single_play_move2,online_choose_site["p"][1]))
    centerBlit(Et.R_if.screen,Et.R_gc.single_choose_pc,(online_choose_site["p"][0]+Et.player_choice*online_choose_site["step2"]-Et.single_play_move2,online_choose_site["p"][1]))
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
                    Et.R_if.screen.blit(Et.R_cu.actionpic[int(Et.R_cu.actionblitcount/5)],custom_c_site["action"])

def customC1Show():
    Et.R_if.screen.blit(Et.R_if.custom_choose_bk_pic,(-1,-1))
    [x,y]=pygame.mouse.get_pos()
    if Et.R_cu.characterType==0:
        centerBlit(Et.R_if.screen,Et.R_if.tick_pic,custom_c_site["pow"])
    elif Et.R_cu.characterType==1:
        centerBlit(Et.R_if.screen,Et.R_if.tick_pic,custom_c_site["agi"])
    elif Et.R_cu.characterType==2:
        centerBlit(Et.R_if.screen,Et.R_if.tick_pic,custom_c_site["int"])
    centerBlit(Et.R_if.screen,Et.R_if.cursor_pic,[x,y])

def customCActionshow():
    if Et.R_cu.actionkind>-1:
        if Et.R_cu.actionkind<4:
            if Et.R_cu.actioncomplete[Et.R_cu.actionkind]:
                Et.R_cu.actionblitcount=Et.R_cu.actionblitcount+1
                if Et.R_cu.actionblitcount==15:
                    Et.R_cu.actionblitcount=0
                if not Et.game_state==GAMEINIT:
                    Et.R_if.screen.blit(Et.R_cu.actionpic[int(Et.R_cu.actionblitcount/5)],custom_c_site["action"])

def customC2Show():
    Et.R_if.screen.blit(Et.R_if.custom_choose_bk_pic,(-1,-1))
    [x,y]=pygame.mouse.get_pos()
    temp=Et.R_if.pic_choose_bk_pic.copy()
    if Et.R_cu.actionkind==4:
        for tx,custom_skill in enumerate(Et.custommode.custom_skill):
            rc=[int(tx/5),tx%5]
            if (rc[0]<6.5+Et.R_cu.rolllength/custom_thumbnail_size[1])&(rc[0]+0.5>Et.R_cu.rolllength/custom_thumbnail_size[1]):
                temp.blit(custom_skill,(rc[1]*int(custom_pic_choose_size[0]/5)+17,(Et.R_cu.rolllength+10+rc[0]*(custom_thumbnail_size[1]+60))))
    else:
        for tx,pic in enumerate(Et.custommode.pic):
            rc=[int(tx/5),tx%5]
            #if (rc[0]<6.5+Et.R_cu.rolllength/custom_thumbnail_size[1])&(rc[0]+0.5>Et.R_cu.rolllength/custom_thumbnail_size[1]):
            temp.blit(pic,(rc[1]*int(custom_pic_choose_size[0]/5)+17,(Et.R_cu.rolllength+10+rc[0]*(custom_thumbnail_size[1]+60))))

    for i in range(len(Et.R_if.custom_frame_place)):
        temp.blit(Et.R_if.custom_frame2_pic,(Et.R_if.custom_frame_place[i][0]*int(custom_pic_choose_size[0]/5)+17,(Et.R_cu.rolllength+10+Et.R_if.custom_frame_place[i][1]*(custom_thumbnail_size[1]+60))))

    Et.R_if.screen.blit(temp,custom_c_site["show"])
    centerBlit(Et.R_if.screen,Et.R_if.cursor_pic,[x,y])

def centerBlit(surface,pic,center):
    dx = int(pic.get_width()/2)
    dy = int(pic.get_height()/2)
    surface.blit(pic,[center[0] - dx,center[1] - dy])

def gameBlit():
    Et.R_sg.bg_pic_temp = Et.R_sg.bg_pic.copy()
    for ob in Et.Os_info:
        obstacleBlit(ob)
    for sk in Et.Sk_info:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_sk[sk.kind].pic, sk.site)
        if sk.draw_line != None:
            pygame.draw.line(Et.R_sg.bg_pic_temp, (0,0,0), sk.draw_line[0], sk.draw_line[1], 5)
    for enemy in Et.Em_info:
        enemyBlit(enemy)
    playerBlit(Et.Pr_info[0])
    Et.R_if.screen.blit(Et.R_sg.bg_pic_temp, blitPoint())
    
   #12月26日谢福生修改
    centerBlit(Et.R_if.screen,Et.R_if.single_hp_bk_pic,single_site["state"])
    centerBlit(Et.R_if.screen,Et.R_gc.single_portrait[Et.player_choice],single_site["portrait"])
    Et.R_if.screen.set_clip((single_site["hp"][0]-single_game_hp_size[0]/2,single_site["hp"][1]-single_game_hp_size[1]/2),(single_site["hp"][0]+single_game_hp_size[0]/2,single_site["hp"][1]+single_game_hp_size[1]/2))
    centerBlit(Et.R_if.screen,Et.R_if.single_hp_pic,(single_site["hp"][0]+((Et.Pr_info[0].life_value-Et.R_pl.max_life)*single_game_hp_size[0]/Et.R_pl.max_life),single_site["hp"][1]))
    Et.R_if.screen.set_clip((0,0),mainwindow_size)
    Et.R_if.screen.blit(Et.R_if.single_frame_pic, (0,0))
    for i in range(0,3):
        centerBlit(Et.R_if.screen,Et.R_sk[Et.R_pl.skill[i]].single_game_skill,(single_site["skill"][0]+i*single_site["step"],single_site["skill"][1]))
    centerBlit(Et.R_if.screen,Et.R_sg.small_map_pic,single_site["smallmap"])
    centerBlit(Et.R_if.screen,Et.R_if.single_game_smallplayer_pic,(single_site["smallplayer"][0]+Et.Pr_info[0].site[0]/Et.R_sg.size[0]*single_game_map_size[0],single_site["smallplayer"][1]+Et.Pr_info[0].site[1]/Et.R_sg.size[1]*single_game_map_size[1]))
    #12月26日谢福生修改
    if Et.S_game.over == 1:
        centerBlit(Et.R_if.screen, Et.R_if.vic_pic, [mainwindow_size[0]/2,mainwindow_size[1]/2])
        Et.over_count += 1
    elif Et.S_game.over == 2:
        centerBlit(Et.R_if.screen, Et.R_if.lose_pic, [mainwindow_size[0] / 2, mainwindow_size[1] / 2])
        Et.over_count += 1

def onlineBlit():
    if Et.online_over == 0:
        Et.R_sg.bg_pic_temp = Et.R_sg.bg_pic.copy()
        for ob in Et.Os_info:
            if ob.kind!=0:
                centerBlit(Et.R_sg.bg_pic_temp, Et.R_ob.pic[ob.kind-1], ob.site)
        for sk in Et.Sk_info:
            centerBlit(Et.R_sg.bg_pic_temp, Et.R_sk[sk.kind].pic, sk.site)
            if sk.draw_line != None:
                pygame.draw.line(Et.R_sg.bg_pic_temp, (0,0,0), sk.draw_line[0], sk.draw_line[1], 5)
        for p in Et.Pr_info:
            onlinePlayerBlit(p)
        x,y = 0,0
        if Et.online_player_site[0] <= mainwindow_size[0]/2:
            x = 0
        elif Et.online_player_site[0] >= Et.R_sg.size[0] - mainwindow_size[0]/2:
            x = mainwindow_size[0] - Et.R_sg.size[0]
        else:
            x = mainwindow_size[0]/2 - Et.online_player_site[0]
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_if.online_arrow_pic, (Et.online_player_site[0],Et.online_player_site[1]-80))
        Et.R_if.screen.blit(Et.R_sg.bg_pic_temp, (x, 0))
    elif Et.online_over == 2:
        centerBlit(Et.R_if.screen, Et.R_if.vic_pic, [mainwindow_size[0]/2,mainwindow_size[1]/2])
        Et.over_count += 1
    elif Et.online_over == 1:
        centerBlit(Et.R_if.screen, Et.R_if.lose_pic, [mainwindow_size[0]/2,mainwindow_size[1]/2])
        Et.over_count += 1

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
    Et.R_sg.bg_pic_temp.set_clip((einfo.site[0]-enemy_hp_size[0]/2,einfo.site[1]-enemy_hp_size[1]-einfo.size[1]/2),(einfo.site[0]+enemy_hp_size[0]/2,einfo.site[1]-einfo.size[1]/2))
    centerBlit(Et.R_sg.bg_pic_temp,Et.R_if.enemy_hp_pic,(einfo.site[0]+((einfo.life_value-einfo.max_life)*enemy_hp_size[0]/einfo.max_life),einfo.site[1]-einfo.size[1]/2-enemy_hp_size[1]/2))
    Et.R_sg.bg_pic_temp.set_clip((0,0),Et.R_sg.size)
    if einfo.state == ENEMYSTATIC:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_em.enemy[einfo.kind].pic_static[int(einfo.count / 4)][einfo.pic_direction], einfo.site)
    elif einfo.state in [ENEMYMOVE,ENEMYPATROL]:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_em.enemy[einfo.kind].pic_move[int(einfo.count / 4)][einfo.pic_direction], einfo.site)
    elif einfo.state in [ENEMYATTACK]:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_em.enemy[einfo.kind].pic_attack[int(einfo.count / 4)][einfo.pic_direction], einfo.site)
    elif einfo.state == ENEMYATTACKED:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_em.enemy[einfo.kind].pic_attacked[int(einfo.count / 4)][einfo.pic_direction], einfo.site)

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
    centerBlit(Et.R_if.screen, Et.C_G.pic,custom_G_site["face"])
    for site in Et.C_G.enemy_list:
        Et.R_if.screen.blit(Et.C_G.enemy_pic[site[2]], (site[0],site[1]))
    for site in Et.C_G.obstacle_list:
        Et.R_if.screen.blit(Et.C_G.ob_pic[site[2]-1], (site[0],site[1]))

def mouseResponseCustomG(event):
    for i in range(0,6):
        if Ip.regionMonitor(event,(custom_G_site["button"][0],custom_G_site["button"][1]+i*custom_G_site["step"]),custom_G_site["button_size"]):
            Et.C_G.choose = i
    if Ip.regionMonitor(event,custom_G_site["face"],custom_G_face_size):
        if Et.C_G.choose in [0,1,2]:
            Et.C_G.enemy_list.append((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],Et.C_G.choose))
        else:
            Et.C_G.obstacle_list.append((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],Et.C_G.choose-2))
    if Ip.regionMonitor(event,custom_G_site["back"],custom_G_site["back_size"]):
        Et.C_G.choose=7
    


def mydel():
    Et.R_sg = None
    Et.R_pl = [None]*2


def onlinePlayerBlit(pinfo):
    Et.R_sg.bg_pic_temp.set_clip((pinfo.site[0]-enemy_hp_size[0]/2,pinfo.site[1]-enemy_hp_size[1]-50),(pinfo.site[0]+enemy_hp_size[0]/2,pinfo.site[1]-50))
    centerBlit(Et.R_sg.bg_pic_temp,Et.R_if.enemy_hp_pic,(pinfo.site[0]+((pinfo.life_value-pinfo.max_life)*enemy_hp_size[0]/pinfo.max_life),pinfo.site[1]-50-enemy_hp_size[1]/2))
    Et.R_sg.bg_pic_temp.set_clip((0,0),Et.R_sg.size)
    if pinfo.state == PLAYERSTATIC:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_og.r_player[pinfo.kind].pic_static[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)
    elif pinfo.state == PLAYERMOVE:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_og.r_player[pinfo.kind].pic_move[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)
    elif pinfo.state in [PLAYERATTACK,PLAYERSKILL1,PLAYERSKILL2,PLAYERSKILL3]:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_og.r_player[pinfo.kind].pic_attack[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)
    elif pinfo.state == PLAYERATTACKED:
        centerBlit(Et.R_sg.bg_pic_temp, Et.R_og.r_player[pinfo.kind].pic_attacked[int(pinfo.count / 4)][pinfo.pic_direction], pinfo.site)
