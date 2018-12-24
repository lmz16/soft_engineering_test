# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 10:15:37 2018

@author: Kaifeng Deng
"""

import Skill
import time
import Extern as Et
from Define import *
import math

#模拟外部接口类
class PlayerInfo():
    def __init__(self):
        self.site = [0, 0]
        self.life_value = 0
        self.size = [0, 0]
        
class Player():
    def __init__(self,pinfo):
        self.info = pinfo
        self.signal = None
        self.return_site = [0, 0]
        self.return_released = False
        
class EnemyInfo():
    def __init__(self):
        self.site = [0, 0]
        self.life_value = 0
        self.size = [0, 0]
        
class Enemy():
    def __init__(self,einfo):
        self.info = einfo
        self.signal = None
        self.passive_move_flag = False
    def passiveMove(self,vec):
        self.passive_move_flag = True
        
class ObstacleInfo():
    def __init__(self):
        self.site = [0, 0]
        self.size = [0, 0]
        
class Obstacle():
    def __init__(self,einfo):
        self.info = einfo
        
class Game():
    def __init__(self):
        self.player = None
        self.enemy_list = []
        self.obstacle_list = []
        self.skill_list = []
        
class Resource():
    def __init__(self):
        self.size = [0,0]
        self.damage = 0
        self.duration = 0.5
        self.pic = None
        
#模拟外部接口初始化
game = Game()
playerinfo = PlayerInfo()
player = Player(playerinfo)
player.info.size = [100,100]
game.player = player
enemyinfo1 = EnemyInfo()
enemy1 = Enemy(enemyinfo1)
enemy1.info.size = [50,50]
enemyinfo2 = EnemyInfo()
enemy2 = Enemy(enemyinfo2)
enemy2.info.size = [50,50]
game.enemy_list.append(enemy1)
game.enemy_list.append(enemy2)
obstacleinfo1 = ObstacleInfo()
obstacle1 = Obstacle(obstacleinfo1)
obstacle1.info.size = [200,200]
obstacleinfo2 = ObstacleInfo()
obstacle2 = Obstacle(obstacleinfo2)
obstacle2.info.size = [200,200]
game.obstacle_list.append(obstacle1)
game.obstacle_list.append(obstacle2)
Et.R_sk[SKILLBOMBEXPLODING] = Resource()
Et.R_sk[SKILLAIMFIRED] = Resource()

def place(psite,e1site,e2site,o1site,o2site):
    player.info.site = psite[:]
    player.info.life_value = 400
    player.signal = None
    enemy1.info.site = e1site[:]
    enemy1.info.life_value = 400
    enemy1.signal = None
    enemy1.passive_move_flag = False
    enemy2.info.site = e2site[:]
    enemy2.info.life_value = 400
    enemy2.signal = None
    enemy2.passive_move_flag = False
    obstacle1.info.site = o1site[:]
    obstacle2.info.site = o2site[:]
    
def release(sk_type,size,direction,caster,velocity,damage,duration,extra_param1=0,extra_param2=0):
    Et.fresh_time = time.time()
    sk_info = Skill.SkillInfo()
    if sk_type == SKILLBALLSTRAIGHT:
        sk = Skill.SkillBallStraight(sk_info)
    elif sk_type == SKILLBALLSINUS:
        sk = Skill.SkillBallSinus(sk_info)
    elif sk_type == SKILLBALLCIRCLE:
        sk = Skill.SkillBallCircle(sk_info)
    elif sk_type == SKILLBLACKHOLE:
        sk = Skill.SkillBlackHole(sk_info)
        sk.effect_radius = extra_param1
        sk.displacement = extra_param2
    elif sk_type == SKILLHOOK:
        sk = Skill.SkillHook(sk_info)
    elif sk_type == SKILLBOMB:
        sk = Skill.SkillBomb(sk_info)
        sk.explosion_radius = extra_param1
    elif sk_type == SKILLAIM:
        sk = Skill.SkillAim(sk_info)
        sk.fire_range = extra_param1
    elif sk_type == SKILLKEKKAI:
        sk = Skill.SkillKekkai(sk_info)
        sk.radius = extra_param1
    elif sk_type == SKILLBALLRETURN:
        sk = Skill.SkillBallReturn(sk_info)
        sk.returning_velocity = extra_param1
    elif sk_type == SKILLTRIANGLE:
        sk = Skill.SkillTriangle(sk_info)
        next_info = Skill.SkillInfo()
        next_sk = Skill.SkillTriangle(next_info)
        next_sk.info.site = [extra_param1,extra_param2]
        sk.next = next_sk
        next_sk.next = sk
        sk.effective = True
    sk.game = game
    sk.init_site = caster.info.site[:]
    sk.init_time = Et.fresh_time
    sk.caster = caster
    sk.direction = direction
    sk.info.site = caster.info.site[:]
    sk.info.size = size
    sk.damage = damage
    sk.velocity = velocity
    sk.duration= duration
    game.skill_list.append(sk)
    while True:
        curr_time = time.time()
        if sk_type == SKILLAIM and (curr_time - sk.init_time) > 0.9 and (curr_time - sk.init_time) < 1.1:
            sk.setOff()
        if sk_type == SKILLBALLRETURN and (curr_time - sk.init_time) > 1.9 and (curr_time - sk.init_time) < 2.1:
            sk.returning = True
            enemy1.info.site = [0,0]
        if (curr_time - Et.fresh_time) > 1/fps:
            Et.fresh_time = curr_time
            sk.update()
            sk.influence()
            if sk.delflag:
                break
        if sk.delflag:
            break

#BallStraight
pass_test = True
place([50,100],[100,120],[150,30],[0,0],[0,0])
release(SKILLBALLSTRAIGHT,[50,50],MOVERIGHT,player,10,200,5)
if not (enemy1.info.life_value == 200 and enemy1.signal == ATTACKED and enemy2.info.life_value == 400 and enemy2.signal == None and player.info.life_value == 400 and player.signal == None):
    pass_test = False
place([250,50],[260,140],[150,30],[0,0],[0,0])
release(SKILLBALLSTRAIGHT,[50,50],MOVEUPLEFT,enemy1,10,200,5)
if not (enemy1.info.life_value == 400 and enemy1.signal == None and enemy2.info.life_value == 400 and enemy2.signal == None and player.info.life_value == 200 and player.signal == ATTACKED):
    pass_test = False
if pass_test:
    print("BallStraight test passed.")
else:
    print("BallStraight test failed.")
    
#BallSinus
pass_test = True
place([0,100],[50,170],[0,30],[0,0],[0,0])
release(SKILLBALLSINUS,[50,50],MOVERIGHT,player,10,200,5)
if not (enemy1.info.life_value == 200 and enemy1.signal == ATTACKED and enemy2.info.life_value == 400 and enemy2.signal == None and player.info.life_value == 400 and player.signal == None):
    pass_test = False
place([250,100],[350,100],[150,100],[0,0],[0,0])
release(SKILLBALLSINUS,[50,50],MOVELEFT,enemy1,10,200,5)
if not (enemy1.info.life_value == 400 and enemy1.signal == None and enemy2.info.life_value == 400 and enemy2.signal == None and player.info.life_value == 200 and player.signal == ATTACKED):
    pass_test = False
if pass_test:
    print("BallSinus test passed.")
else:
    print("BallSinus test failed.")
    
#BallCircle
pass_test = True
place([200,200],[200,350],[0,0],[0,0],[0,0])
release(SKILLBALLCIRCLE,[50,50],None,player,0,50,5)
if not (enemy1.info.life_value == 150 and enemy1.signal == ATTACKED and enemy2.info.life_value == 400 and enemy2.signal == None and player.info.life_value == 400 and player.signal == None):
    pass_test = False
if pass_test:
    print("BallCircle test passed.")
else:
    print("BallCircle test failed.")
    
#BlackHole
pass_test = True
place([500,500],[600,600],[700,500],[0,0],[0,0])
release(SKILLBLACKHOLE,[200,200],None,player,0,0,5,200,5)
if not (enemy1.passive_move_flag and not enemy2.passive_move_flag):
    pass_test = False
if pass_test:
    print("BlackHole test passed.")
else:
    print("BlackHole test failed.")
    
#Hook
pass_test = True
place([500,500],[0,0],[0,0],[500,100],[0,0])
release(SKILLHOOK,[50,50],MOVERIGHT,player,10,0,5,0,0)
if not (player.info.site == [500,500]):
    pass_test = False
release(SKILLHOOK,[50,50],MOVEUP,player,10,0,5,0,0)
if not (math.sqrt((player.info.site[0]-500)**2+(player.info.site[1]-250)**2)) <= 50:
    pass_test = False
if pass_test:
    print("Hook test passed.")
else:
    print("Hook test failed.")
    
#Bomb
pass_test = True
place([500,500],[600,600],[300,700],[0,0],[0,0])
release(SKILLBOMB,[50,50],None,player,0,200,5,200,0)
if not (enemy1.info.life_value == 200 and enemy1.signal == ATTACKED and enemy2.info.life_value == 400 and enemy2.signal == None and player.info.life_value == 400 and player.signal == None):
    pass_test = False
if pass_test:
    print("Bomb test passed.")
else:
    print("Bomb test failed.")
    
#Aim
pass_test = True
place([500,500],[600,500],[500,500],[0,0],[0,0])
release(SKILLAIM,[20,20],MOVERIGHT,player,10,200,5,50,0)
if not (enemy1.info.life_value == 200 and enemy1.signal == ATTACKED and enemy2.info.life_value == 400 and enemy2.signal == None and player.info.life_value == 400 and player.signal == None):
    pass_test = False
if pass_test:
    print("Aim test passed.")
else:
    print("Aim test failed.")
    
#Kekkai
pass_test = True
place([100,100],[180,100],[110,110],[0,0],[0,0])
release(SKILLKEKKAI,[200,200],None,player,0,200,5,100,0)
if not (enemy1.info.life_value == 200 and enemy1.signal == ATTACKED and enemy2.info.life_value == 400 and enemy2.signal == None and player.info.life_value == 400 and player.signal == None):
    pass_test = False
place([100,100],[100,210],[230,230],[0,0],[0,0])
release(SKILLKEKKAI,[200,200],None,player,0,200,5,100,0)
if not (enemy1.info.life_value == 200 and enemy1.signal == ATTACKED and enemy2.info.life_value == 400 and enemy2.signal == None and player.info.life_value == 400 and player.signal == None):
    pass_test = False
if pass_test:
    print("Kekkai test passed.")
else:
    print("Kekkai test failed.")
    
#BallReturn
pass_test = True
place([100,100],[120,100],[200,110],[0,0],[0,0])
release(SKILLBALLRETURN,[50,50],MOVERIGHT,player,10,200,5,30,0)
if not (enemy1.info.life_value == 200 and enemy1.signal == ATTACKED and enemy2.info.life_value == 0 and enemy2.signal == ATTACKED and player.info.life_value == 400 and player.signal == None):
    pass_test = False
if pass_test:
    print("BallReturn test passed.")
else:
    print("BallReturn test failed.")
    
#Triangle
pass_test = True
place([100,100],[150,170],[250,400],[0,0],[0,0])
release(SKILLTRIANGLE,[50,50],None,player,0,200,5,200,200)
if not (enemy1.info.life_value == 200 and enemy1.signal == ATTACKED and enemy2.info.life_value == 400 and enemy2.signal == None and player.info.life_value == 400 and player.signal == None):
    pass_test = False
place([100,100],[150,130],[0,-100],[0,0],[0,0])
release(SKILLTRIANGLE,[50,50],None,player,0,200,5,200,200)
if not (enemy1.info.life_value == 200 and enemy1.signal == ATTACKED and enemy2.info.life_value == 400 and enemy2.signal == None and player.info.life_value == 400 and player.signal == None):
    pass_test = False
if pass_test:
    print("Triangle test passed.")
else:
    print("Triangle test failed.")