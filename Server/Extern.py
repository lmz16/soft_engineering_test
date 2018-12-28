#
#   在线游戏的全局变量文件
#

from Define import *

#   游戏刷新时间
fresh_time = 0
#   游戏初始时间
init_time = 0

#   游戏状态
game_state = GAMEWAIT

#   信息列表
Pr_info = []
Sk_info = []
Ob_info = []

#   在线游戏
online_game = None

#   ip与玩家对应列表
num_ip = []

#   当前数据包
data = None

#   技能配置资源
R_skill = [None]*SKILLMAXINDEX

#	
count = 0
