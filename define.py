#
#   宏定义模块，存储一些常量
#

#   开始界面背景图路径
start_background_filename='start_interface.jpg'
#   光标图片路径
cursor_filename='cursor.png'
#   开始按钮图片路径 单人游戏，联机对战，设置，帮助，自定义
start_button_filename='start_button_single.png'
start_button_online_filename='start_button_online.png'
start_button_setting_filename='start_button_setting.png'
start_button_help_filename='start_button_help.png'
start_button_custom_filename='start_button_custom.png'

#   主窗口尺寸
mainwindow_size=(1440,900)
#   光标尺寸
cursor_size=(30,40)
#   开始按钮尺寸
start_button_size=(250,50)
start_button_online_size=(250,50)
start_button_setting_size=(250,50)
start_button_help_size=(250,50)
start_button_custom_size=(250,50)

#   帮助文档
help_text_filename='help_text.png'
help_text_size=(800,600)

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

#   碰撞阈值
COLLISIONTHRESHOLD=10

#   帧率
fps=25

#   主游戏最底图层路径
gameinterface_filename='gameinterface.png'

#   人物状态
#   静止状态
PLAYERSTATIC=-1
#   移动状态
PLAYERMOVE=0
#   攻击状态
PLAYERATTACK=-2
#   技能一状态
PLAYERSKILL1=-4
#   被攻击状态
PLAYERATTACKED=-3

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

#   移动序列
movex=[0,0,-1,1,-1,1,-1,1]
movey=[-1,1,0,0,-1,-1,1,1]