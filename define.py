#
#   宏定义模块，存储一些常量
#

#   主窗口尺寸
mainwindow_size=(1440,900)
#   光标尺寸
cursor_size=(30,40)
#   开始按钮尺寸
start_button_size=(250,50)
#单人模式选择界面缩略图尺寸
single_choose_b_size=(500,300)
single_choose_bc_size=(550,340)
single_choose_p_size=(200,200)
single_choose_pc_size=(230,230)

#   帮助文档
help_text_size=(800,600)

#   自定义模式缩略图大小
custom_thumbnail_size=(100,160)
custom_pic_choose_size=(700,700)

#   游戏状态常量
#   初始状态
GAMEINIT=0
#   游戏开始状态
GAMESTART=1
#   游戏载入状态
GAMELOAD=-1
#   帮助所需状态
GAMEHELP=2
GAMEHELP2=3
GAMEINIT1=4
#   单人模式选择状态
GAMESINGLECHOOSE=5
#   自定义模式选择状态
GAMECUSTOMCHOOSE=20
#   自定义人物模式
GAMECUSTOMC=21
#   自定义关卡模式
GAMECUSTOMG=22

#   碰撞阈值
COLLISIONTHRESHOLD=10

#   帧率
fps=25

#   主游戏最底图层路径
gameinterface_filename='Resource/interface/gameinterface.png'

#   人物状态
#   静止状态
PLAYERSTATIC=-1
#   移动状态
PLAYERMOVE=0
#   攻击状态
PLAYERATTACK=-2
#   被攻击状态
PLAYERATTACKED=-3
#   技能一状态
PLAYERSKILL1=-4
#   技能二状态
PLAYERSKILL2=-5
#   技能三状态
PLAYERSKILL3=-6
#   死亡状态
PLAYERDEAD=-7

#   敌人状态
#   静止状态
ENEMYSTATIC=-1
#   移动状态
ENEMYMOVE=0
#   攻击状态
ENEMYATTACK=-2
#   被攻击状态
ENEMYATTACKED=-3
#   死亡状态
ENEMYDEAD=-4


#上      
MOVEUP=0
#下      
MOVEDOWN=1
#左      
MOVELEFT=2
#右      
MOVERIGHT=3
#左上 
MOVEUPLEFT=4
#右上 
MOVEUPRIGHT=5
#左下 
MOVEDOWNLEFT=6
#右下 
MOVEDOWNRIGHT=7
#1技能
SKILL1=8
#2技能
SKILL2=9
#3技能
SKILL3=10
#被攻击信号
ATTACKED=11
#死亡信号
DIE=12

#   移动序列
movex=[0,0,-1,1,-1,1,-1,1]
movey=[-1,1,0,0,-1,-1,1,1]
