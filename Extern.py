#
#   全局变量模块
#

from Define import *

#   游戏刷新时间
fresh_time = 0
#   初始化时间
init_time = 0

#   游戏进行状态
game_state = None

#   关卡选择结果
game_choice = 0
#   单人游戏选择界面控制
single_play_move1=10.0
single_play_move2=10.0
#   自定义模式资源
R_cu = None
custommode='自定义模式'
C_G = None
#   游戏资源
#   开始界面资源
R_if = None
#   选择界面资源
R_gc = None
#   单人游戏资源
R_sg = None
#   人物资源
R_pl = None
#   敌人资源
R_em = None
#   障碍物资源
R_ob = None
#   技能资源
R_sk = [None]*SKILLMAXINDEX
#   网络版本的资源
R_og = None

#   人物选择结果
player_choice = 0

#   游戏对象
S_game = None

#   键盘控制对象
I_ctr = None

#   人物信息对象
Pr_info = [None,None]

#   敌人信息对象
Em_info = []

#   障碍物信息对象
Os_info = []

#   技能信息对象
Sk_info = []

#   P1玩家人物
P1_choice = 0

#   P2玩家人物
P2_choice = 0

#   网络线程
t_net = None

#   网络游戏结束标志
online_over = 0

#   用于游戏结束状态的计数变量
over_count = 0

#   玩家id
fake_ip = 0

#   联机控制人物的坐标
online_player_site = [0,0]
#   
online_camp = 0
