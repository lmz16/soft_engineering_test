#
#   人物类
#

from define import *
import extern
import pygame
from pygame.locals import *

class Player():
    def __init__(self):
        self.site='人物位置(二维)'
        self.life_value='人物生命值'
        self.power='攻击力'
        self.mana='魔法值'
        self.attack_range='射程'
        self.velosity='速度'
        self.state=PLAYERSTATIC
        self.movable='人物是否可以移动'
        self.direction='人物朝向'
        self.signal='接收到的信号'
        self.size='人物的大小'
        self.load()

# 根据人物类型与位置的贴图函数
    def player_blit(self):
        pass

# 状态更新,有限状态机,每个不同角色单独实现
    def update(self):
        pass

# 事实上的构造函数,init里面只是声明一下变量,之所以不赋值,是因为这些值
# 可能要从文件里读取或者是根据游戏设置而定
    def load(self):
        pass

# 键盘侠类,继承自Player类
class KeyBoardMan(Player):
    def __init__(self):
        super(KeyBoardMan,self).__init__()
        pass
