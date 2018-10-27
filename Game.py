#
#   游戏类
#

from define import *
import extern
import Player

import pygame
from pygame.locals import *

class Single_player_game():
    def __init__(self):
        self.single_player=Player.Player()
    # 调用初始化函数,加载关卡信息,敌人数量与类型,地图资源
        self.enemy_list=[]
        self.background="背景地图的图片对象"
        self.Load_from_json()
    # 技能列表
        self.skill_list=[]
    # 信号列表,用于暂存未处理的信号
        self.signal_list=[]

# 初始化函数,从json文件读入信息
    def load_from_json(self):
        pass

# 攻击判定方法,根据技能列表里的技能判断是否向message_list写入信号
    def attack_judge(self):
        pass

# 移动判定方法,判定对象是否可以移动,将结果写入成员对象的movable属性
    def move_judge(self):
        pass

# 信号处理函数,解决信号冲突,向每个对象发送信号
    def message_translate(self):
        pass

# 游戏画面与状态更新
    def game_update(self):
        pass

# 信号类
class Signal():
    def __init__():
        self.type='信号类型'
        self.receiver='信号接收者'
