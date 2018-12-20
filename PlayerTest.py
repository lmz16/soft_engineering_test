#
#    玩家模块测试
#

import Extern as Et
from Define import *
import Item as It
import Input as Ip
from Player import PlayerInfo, Player

#强行建类
class temp1():
    def __init__(self):
        self.size = [1000,1000]
class temp2():
    def __init__(self):
        self.p1_key = {'up': False, 'down': True, 'left': False, 'right': False}

class TPlayer():
    def __init__(self):
        #强行赋值
        Et.I_ctr = temp2()
        Et.R_sg = temp1()
        self.test_count = 6  #共六个小测试
        self.test_each = 5   #每个小测试有5个测试样例
        self.playerinfo = PlayerInfo()
        self.player = Player(self.playerinfo)
        self.count = 0
        self.sub_count = 0
        self.test_speed = 3  #测试速度
        self.test_sequence_1 = [
            
            #单独测试，无游戏指针self.game
            #加上了Et.fresh_time赋值

            #以下用于测试Player移动signal
            [[200,300], 100, 100, PLAYERSTATIC, RIGHT, [10,10], 0, True, 
            [10,10], [True,True,True,True], [0,0,0], [1,1,1], 5, None, MOVERIGHT, 
            [0,0,0], 12, [200,400], False, 12],
            [[0,0], 100, 100, PLAYERMOVE, RIGHT, [10,10], 0, True, 
            [10,10], [True,True,True,True], [0,0,0], [1,1,1], 5, 1, MOVEDOWN, 
            [0,0,0], 12, [200,400], False, 12],
            [[100,200], 100, 100, PLAYERSTATIC, RIGHT, [10,10], 0, True, 
            [10,10], [True,True,True,True], [0,0,0], [1,1,1], 5, 2, MOVEUPRIGHT, 
            [0,0,0], 12, [200,400], False, 12],
            [[500,300], 100, 100, PLAYERMOVE, RIGHT, [10,10], 0, True, 
            [10,10], [True,True,True,True], [0,0,0], [1,1,1], 5, 3, MOVEUPLEFT, 
            [0,0,0], 12, [200,400], False, 12],
            [[0,0], 100, 100, PLAYERMOVE, RIGHT, [10,10], 0, True, 
            [10,10], [True,True,True,True], [0,0,0], [1,1,1], 5, 4, MOVELEFT, 
            [0,0,0], 12, [200,400], False, 12],
             #以下用于测试三个球类技能
            [[200,300], 100, 100, PLAYERSTATIC, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, SKILL1, MOVEUP, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
            [[0,0], 100, 100, PLAYERMOVE, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [0,0,0], [2,2,2], 5, SKILL2, MOVEDOWNRIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
            [[100,200], 100, 100, PLAYERSTATIC, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [2,1,2], [3,3,3], 5, SKILL3, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
            [[500,300], 100, 100, PLAYERMOVE, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [3,3,3], [1,2,3], 5, SKILL1, MOVEUPLEFT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
            [[0,0], 100, 100, PLAYERSTATIC, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [4,5,5], [4,5,6], 5, SKILL2, MOVELEFT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
             #以下用于测试三个球类技能冷却
            [[200,300], 100, 100, PLAYERSTATIC, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, SKILL1, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
            [[0,0], 100, 100, PLAYERMOVE, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, SKILL2, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 11],
            [[100,200], 100, 100, PLAYERSTATIC, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [5,5,5], [2,2,2], 5, SKILL3, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 7],
            [[500,300], 100, 100,PLAYERMOVE, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [30,30,30], [0,0,0], 5, SKILL1, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 8],
            [[0,0], 100, 100,PLAYERMOVE, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [7,8,9], [1,1,1], 5, SKILL2, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 10],
             #以下用于测试三个球类技能前摇打断
            [[200,300], 100, 100, PLAYERSTATIC, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, SKILL1, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
            [[0,0], 100, 100, PLAYERMOVE, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, SKILL2, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 11],
            [[100,200], 100, 100, PLAYERSTATIC, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [5,5,5], [2,2,2], 5, SKILL3, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 7],
            [[500,300], 100, 100,PLAYERMOVE, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [30,30,30], [0,0,0], 5, SKILL1, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 8],
            [[0,0], 100, 100,PLAYERMOVE, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [7,8,9], [1,1,1], 5, SKILL2, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 10],
             #以下用于测试瞬移技能
            [[200,300], 100, 100, PLAYERSTATIC, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, SKILL1, MOVERIGHT, 
            [SKILLRETURN,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
            [[0,0], 100, 100, PLAYERMOVE, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, SKILL2, MOVERIGHT, 
            [SKILLRETURN,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 11],
            [[100,200], 100, 100, PLAYERSTATIC, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [5,5,5], [2,2,2], 5, SKILL3, MOVERIGHT, 
            [SKILLRETURN,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 7],
            [[500,300], 100, 100,PLAYERMOVE, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [30,30,30], [0,0,0], 5, SKILL1, MOVERIGHT, 
            [SKILLRETURN,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 8],
            [[0,0], 100, 100,PLAYERMOVE, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [7,8,9], [1,1,1], 5, SKILL2, MOVERIGHT, 
            [SKILLRETURN,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 10],
             #以下用于测试被攻击僵持
            [[200,300], 100, 100, PLAYERATTACKED, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, SKILL1, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
            [[0,0], 100, 100, PLAYERATTACKED, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, SKILL2, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
            [[100,200], 100, 100, PLAYERATTACKED, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, SKILL3, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
            [[500,300], 100, 100, PLAYERATTACKED, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, 1, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
            [[0,0], 100, 100, PLAYERATTACKED, RIGHT, [100,100], 0, True, 
            [10,10], [True,True,True,True], [10,10,10], [1,1,1], 5, 2, MOVERIGHT, 
            [SKILLBALLSTRAIGHT,SKILLBALLSINUS,SKILLBALLCIRCLE], 12, [200,400], False, 12],
        ]
    
    def PlayerCreate(self, n):   #根据test_sequence_1里面的信息创建Player类
        self.playerinfo.site = self.test_sequence_1[n][0]
        self.playerinfo.max_life = self.test_sequence_1[n][1]
        self.playerinfo.life_value = self.test_sequence_1[n][2]
        self.playerinfo.state = self.test_sequence_1[n][3]
        self.playerinfo.pic_direction = self.test_sequence_1[n][4]
        self.playerinfo.size = self.test_sequence_1[n][5]
        self.playerinfo.count = self.test_sequence_1[n][6]
        self.playerinfo.visible = self.test_sequence_1[n][7]
        self.player.info = self.playerinfo
        self.player.velocity = self.test_sequence_1[n][8]
        self.player.movable = self.test_sequence_1[n][9]
        self.player.skill_time = self.test_sequence_1[n][10]
        self.player.skill_cd = self.test_sequence_1[n][11]
        self.player.freeze_time = self.test_sequence_1[n][12]
        self.player.signal = self.test_sequence_1[n][13]
        self.player.direction = self.test_sequence_1[n][14]
        self.player.skill_type = self.test_sequence_1[n][15]
        self.player.max_count = self.test_sequence_1[n][16]
        self.player.return_site = self.test_sequence_1[n][17]
        self.player.return_released = self.test_sequence_1[n][18]
        Et.fresh_time = self.test_sequence_1[n][19]

    def test(self):   #总测试函数，引用所有类型的测试函数
        self.sub_count += 1
        if self.sub_count == self.test_speed:
            self.sub_count = 0
            self.MoveTest()
            self.BasicSkillTest()
            self.SkillCdTest()
            self.SkillBreakTest()
            self.ReturnSkillTest()
            self.AttackedFreezeTest()
            self.count += 1
            if self.count >= len(self.test_sequence_1)/self.test_count:
                self.count = 0
            

    def MoveTest(self): #Player移动测试，包含地图边界碰撞测试
        #现在还有问题，在边界碰撞那些地方测试不了
        print('Player移动测试')
        self.PlayerCreate(self.count + 0 * self.test_each)
        print('original position:' + str(self.player.info.site))
        print('signal:' + str(self.player.signal))
        print('original direction:' + str(self.player.direction))
        self.player.update()
        self.player.update()
        print('final position:' + str(self.player.info.site) + '\n')
    
    def BasicSkillTest(self):#三个球类技能测试
        print('球类技能测试')
        self.PlayerCreate(self.count + 1 * self.test_each)
        print('original state:' + str(self.player.info.state))
        print('signal:'+ str(self.player.signal))
        self.player.update()
        print('final state:' + str(self.player.info.state) + '\n')


    def SkillCdTest(self):#三个球类技能冷却时间测试
        print('三个球类技能冷却时间测试')
        self.PlayerCreate(self.count + 2 * self.test_each)
        print('original state:' + str(self.player.info.state))
        print('signal:' + str(self.player.signal))
        print('fresh time:' + str(Et.fresh_time))
        self.player.update()
        print('final state:' + str(self.player.info.state) + '\n')


    def SkillBreakTest(self):#三个球类技能前摇打断测试
        print('三个球类技能前摇打断测试')
        self.PlayerCreate(self.count + 3 * self.test_each)
        print('original state:' + str(self.player.info.state))
        print('signal:' + str(self.player.signal))
        self.player.update()
        print('middle state:' + str(self.player.info.state))
        self.player.signal = ATTACKED
        self.player.update()
        print('final state:' + str(self.player.info.state) + '\n')

    def ReturnSkillTest(self):#瞬移技能测试
        print('瞬移技能测试')
        self.PlayerCreate(self.count + 4 * self.test_each)
        print('original position:' + str(self.player.info.site))
        self.player.actSkill(1)
        self.player.info.site = [9,9]
        print('middle position:' + str(self.player.info.site))
        self.player.actSkill(1)
        print('final position:' + str(self.player.info.site) + '\n')

    def AttackedFreezeTest(self):#被攻击僵直弛豫测试
        print('被攻击僵直弛豫测试')
        self.PlayerCreate(self.count + 5 * self.test_each)
        print('original state:' + str(self.player.info.state))
        print('signal:' + str(self.player.signal))
        self.player.update()
        print('final state:' + str(self.player.info.state) + '\n')




