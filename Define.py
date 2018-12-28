#
#	宏定义模块
#

#	游戏界面常量
mainwindow_size=(960,600)	#主窗口尺寸
cursor_size=(20,30)	        #光标尺寸
start_button_size=(160,34)	#主界面按钮尺寸
help_text_size=(500,400)    #帮助文档和设置文档尺寸
#   单人模式选择界面缩略图尺寸
single_choose_b_size=(300,200)
single_choose_bc_size=(330,225)
single_choose_p_size=(130,140)
single_choose_pc_size=(150,150)
#   单人模式游戏界面尺寸
#谢福生12月26日修改
single_game_portrait_size=(80,80)
single_game_skill_size=(45,45)
single_game_hp_size=(170,40)
single_game_map_size=(260,140)
single_game_p_size=(8,8)
single_game_state_size=(240,200)
#   敌人血条
enemy_hp_size=(80,10)

#   游戏帧率
fps = 25
#   自定义模式缩略图大小
custom_thumbnail_size=(60,100)
custom_pic_choose_size=(540,340)
custom_button_size=(130,50)#自定义人物模式按钮尺寸
custom_G_face_size=(590,290)

online_arrow_size=(25,25)

#   碰撞检测阈值
COLLISIONTHRESHOLD = 6

#   游戏状态常量
#   初始状态
GAMEINIT=0
#   游戏开始状态
GAMESTART=1
#   游戏副载入状态
GAMELOADSUB=-2
#   游戏载入状态
GAMELOAD=-1
#   帮助所需状态
GAMEHELP=2
GAMEHELP2=3
GAMEINIT1=4
#   单人模式选择状态
GAMESINGLECHOOSE=5
#   设置
GAMESETTING=10
#   联机开始状态1
GAMEONLINEINIT1=15
#   联机选择人物状态
GAMEONLINECHOOSE=155
#   联机开始状态2
GAMEONLINEINIT2=16
#   联机游戏进行状态
GAMEONLINE=17
#   自定义模式选择状态
GAMECUSTOMCHOOSE=20
#   自定义模式载入状态
GAMECUSTOMCLOAD=201
#   自定义人物模式
GAMECUSTOMC=21
GAMECUSTOMC2=212
#   自定义关卡模式
GAMECUSTOMG=22
GAMECUSTOMG2=222

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
#   巡逻状态
ENEMYPATROL=-5

#人物朝向
LEFT = 1
RIGHT = 0

#上
MOVEUP = 0
#下
MOVEDOWN = 1
#左
MOVELEFT = 2
#右
MOVERIGHT = 3
#左上
MOVEUPLEFT = 4
#右上
MOVEUPRIGHT = 5
#左下
MOVEDOWNLEFT = 6
#右下
MOVEDOWNRIGHT = 7
#1技能
SKILL1 = 8
#2技能
SKILL2 = 9
#3技能
SKILL3 =10
#被攻击信号
ATTACKED = 11
#死亡信号
DIE = 12

#技能类型
SKILLBALLSTRAIGHT=0
SKILLBALLSINUS=1
SKILLBALLCIRCLE=2
SKILLRETURN=3
SKILLBLACKHOLE=4
SKILLHOOK=5
SKILLBOMB=6
SKILLBOMBEXPLODING=7
SKILLAIM=8
SKILLAIMFIRED=9
SKILLKEKKAI=10
SKILLBALLRETURN=11
SKILLPORTAL=12
SKILLTRIANGLE=13
SKILLMAXINDEX=14

#   移动序列
movex = [0,0,-1,1,-1,1,-1,1]
movey = [-1,1,0,0,-1,-1,1,1]


skill_file = [
    "Resource/json/sk0",
    "Resource/json/sk1",
    "Resource/json/sk2",
    "Resource/json/sk3",
    "Resource/json/sk4",
    "Resource/json/sk5",
    "Resource/json/sk6",
    "Resource/json/sk7",
    "Resource/json/sk8",
    "Resource/json/sk9",
    "Resource/json/sk10",
    "Resource/json/sk11",
    "Resource/json/sk12",
    "Resource/json/sk13",
]