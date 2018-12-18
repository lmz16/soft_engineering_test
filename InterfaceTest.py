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
            [PLAYERSTATIC, LEFT, 3, [100, 300]],
            [PLAYERMOVE, RIGHT, 7, [200, 400]],
            [PLAYERMOVE, LEFT, 11, [250, 350]],
            [PLAYERATTACKED, LEFT, 11, [600, 600]],
            [PLAYERATTACKED, RIGHT, 7, [0, 300]],
            [PLAYERATTACK, LEFT, 3 , [300, 500]],
            [PLAYERATTACK, RIGHT, 0, [200, 300]],
        ]
        self.test_squence_e = [
            [ENEMYSTATIC, RIGHT, 0, [300, 300]],
            [ENEMYSTATIC, LEFT, 3, [100, 400]],
            [ENEMYMOVE, RIGHT, 7, [300, 400]],
            [ENEMYMOVE, LEFT, 11, [250, 150]],
            [ENEMYATTACKED, LEFT, 11, [500, 500]],
            [ENEMYATTACKED, RIGHT, 7, [0, 200]],
            [ENEMYATTACK, LEFT, 3, [300, 400]],
            [ENEMYATTACK, RIGHT, 0, [200, 600]],
        ]
        self.count = 0
        self.sub_count = 0
        self.test_speed = 5

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


