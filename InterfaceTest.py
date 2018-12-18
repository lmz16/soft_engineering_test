#
#   界面模块测试文件
#

import Extern as Et
from Define import *
import Item as It

class TInterface():
    def __init__(self):
        self.test_squence_p = [
            [PLAYERSTATIC, RIGHT, 0, [200, 300]],
            [PLAYERSTATIC, RIGHT, 4, [200, 300]],
            [PLAYERSTATIC, RIGHT, 8, [200, 300]],
            [PLAYERSTATIC, RIGHT, 0, [200, 300]],
            [PLAYERATTACK, RIGHT, 0, [220, 300]],
            [PLAYERATTACK, RIGHT, 4, [220, 300]],
            [PLAYERATTACK, RIGHT, 8 , [220, 300]],
            [PLAYERATTACK, RIGHT, 0, [220, 300]],
            [PLAYERATTACK, RIGHT, 4, [220, 300]],
            [PLAYERATTACK, RIGHT, 8, [220, 300]],
            [PLAYERMOVE, RIGHT, 0, [340, 300]],
            [PLAYERMOVE, RIGHT, 4, [360, 300]],
            [PLAYERMOVE, RIGHT, 8, [380, 300]],
            [PLAYERMOVE, RIGHT, 0, [400, 300]],
            [PLAYERMOVE, RIGHT, 4, [420, 300]],
            [PLAYERMOVE, RIGHT, 8, [440, 300]],
            [PLAYERMOVE, RIGHT, 4, [460, 300]],
            [PLAYERMOVE, RIGHT, 8, [480, 300]],
            [PLAYERMOVE, RIGHT, 0, [500, 300]],
            [PLAYERMOVE, RIGHT, 4, [520, 300]],
            [PLAYERMOVE, RIGHT, 8, [540, 300]],
        ]
        self.test_squence_e = [
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
            [ENEMYATTACK, RIGHT, 0, [300, 100]],
        ]
        self.count = 0
        self.sub_count = 0
        self.test_speed = 3

    def test(self):
        self.sub_count += 1
        if self.sub_count == self.test_speed:
            self.sub_count = 0
            self.count += 1
            if self.count == len(self.test_squence_p):
                self.count = 0
        self.changeParamPlayer()
        self.changeParamEnemy()

    def changeParamPlayer(self):
        Et.Pr_info[0].state = self.test_squence_p[self.count][0]
        Et.Pr_info[0].pic_direction = self.test_squence_p[self.count][1]
        Et.Pr_info[0].count = self.test_squence_p[self.count][2]
        Et.Pr_info[0].site = self.test_squence_p[self.count][3]

    def changeParamEnemy(self):
        if len(Et.Em_info) == 0:
            Et.Em_info.append(It.EnemyInfo)
        Et.Em_info[0].state = self.test_squence_e[self.count][0]
        Et.Em_info[0].pic_direction = self.test_squence_e[self.count][1]
        Et.Em_info[0].count = self.test_squence_e[self.count][2]
        Et.Em_info[0].site = self.test_squence_e[self.count][3]


