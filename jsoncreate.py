import json

data = [{
    "main_bk_pic":"Resource/interface/start_interface.jpg",
    "cursor_pic":"Resource/interface/cursor.png",
    "single_button":"Resource/interface/start_button_single.png",
    "setting_button":"Resource/interface/start_button_setting.png",
    "online_button":"Resource/interface/start_button_online.png",
    "help_button":"Resource/interface/start_button_help.png",
    "custom_button":"Resource/interface/start_button_custom.png",
    "help_text":"Resource/interface/help_text.png",
    "setting_text":"Resource/interface/setting_text.png",
    "setting_choose":"Resource/interface/setting_choose.png",
    "single_frame_pic":"Resource/interface/gameinterface.png",
    "single_hp":"Resource/interface/single_game_hp.png",
    "single_game_smallplayer":"Resource/interface/single_game_smallplayer.png",
    "custom_choose":"Resource/interface/custom_choose.png",
    "custom_choose_bk":"Resource/interface/custom_choose_bk.png",
    "pic_choose_bk":"Resource/interface/pic_choose_bk.png",
    "custom_frame":"Resource/interface/frame.png",
    "custom_choose_choose":"Resource/interface/custom_choose_choose.png",
}]

with open("Resource/json/interface","w") as f:
    json.dump(data,f)

data = [{
    "bottom_pic":'Resource/interface/single_choose_background.jpg',
    "single_choose_frame":'Resource/interface/single_choose_frame.png',
    "single_choose_b":['Resource/interface/single_choose_b1.png',
        'Resource/interface/single_choose_b2.png',
        'Resource/interface/single_choose_b3.png'],
    "single_choose_p":['Resource/interface/single_choose_p1.png',
        'Resource/interface/single_choose_p2.png',
        'Resource/interface/single_choose_p3.png'],
    "single_choose_play":'Resource/interface/single_choose_play.png',
    "single_choose_choose":'Resource/interface/single_choose_choose.png',
}]

with open("Resource/json/game_choose","w") as f:
    json.dump(data,f)

data = [{
    "p1_site":[200,400],
    "bg_pic":"Resource/singleplayergame/game1/background2.png",
    "bg_size":[1160,600],
    "enemy":[
        {
            "site":[700,400],
            "kind":0,
         },
    ],
    "obstacle":[
        {
            "site":[500,200],
            "size":[100,100],
            "kind":0
        },
        {
            "site":[100,200],
            "size":[100,100],
            "kind":0
        },
        {
            "site":[1000,50],
            "size":[10000,100],
            "kind":1
        },
    ]
}]

with open("Resource/json/game1","w") as f:
    json.dump(data,f)

data = [{
    "size":[70,80],
    "realsize":[40,80],
    "life_value":1000,
    "static":[
        "Resource/character/lmz/static0.png",
        "Resource/character/lmz/static1.png",
        "Resource/character/lmz/static0.png",
    ],
    "move":[
        "Resource/character/lmz/move0.png",
        "Resource/character/lmz/move1.png",
        "Resource/character/lmz/move2.png",
    ],
    "attack":[
        "Resource/character/lmz/attack0.png",
        "Resource/character/lmz/attack1.png",
        "Resource/character/lmz/attack2.png",
    ],
    "attacked":[
        "Resource/character/lmz/attacked.png",
        "Resource/character/lmz/attacked.png",
        "Resource/character/lmz/attacked.png",
    ],
    "v":[5,5],
    "skill":[0,5,2]
}]

with open("Resource/json/character1","w") as f:
    json.dump(data,f)

data = [{
    "size":[48,80],
    "realsize":[48,80],
    "life_value":1000,
    "static":[
        "Resource/enemy/enemy1/enemy1_static.jpeg",
        "Resource/enemy/enemy1/enemy1_static.jpeg",
        "Resource/enemy/enemy1/enemy1_static.jpeg",
    ],
    "move":[
        "Resource/enemy/enemy1/enemy1_static.jpeg",
        "Resource/enemy/enemy1/enemy1_static.jpeg",
        "Resource/enemy/enemy1/enemy1_static.jpeg",
    ],
    "attack":[
        "Resource/enemy/enemy1/enemy1_static.jpeg",
        "Resource/enemy/enemy1/enemy1_static.jpeg",
        "Resource/enemy/enemy1/enemy1_static.jpeg",
    ],
    "attacked":[
        "Resource/enemy/enemy1/enemy1_static.jpeg",
        "Resource/enemy/enemy1/enemy1_static.jpeg",
        "Resource/enemy/enemy1/enemy1_static.jpeg",
    ],
    "v":[10,10],
}]

with open("Resource/json/enemy1","w") as f:
    json.dump(data,f)

data = [{
    "pic":"Resource/item/ob1.png",
    "size":[100,100]
}]

with open("Resource/json/ob1","w") as f:
    json.dump(data,f)

#SkBallStraight
data =[{
    "pic":"Resource/item/hand_sword.png",
    "realsize":[30,30],
    "size":[30,30],
    "damage":50,
    "v":10,
    "life":5,
    "extra_param1":0,
    "extra_param2":0,
}]

with open("Resource/json/sk0","w") as f:
    json.dump(data,f)

#SkBallSinus
data =[{
    "pic":"Resource/item/fire_ball.png",
    "realsize":[30,30],
    "size":[30,30],
    "damage":50,
    "v":10,
    "life":5,
    "extra_param1":0,
    "extra_param2":0,
}]

with open("Resource/json/sk1","w") as f:
    json.dump(data,f)
    
#SkBallCircle
data =[{
    "pic":"Resource/item/circle_ball.png",
    "realsize":[30,30],
    "size":[30,30],
    "damage":50,
    "v":10,
    "life":5,
    "extra_param1":0,
    "extra_param2":0,
}]

with open("Resource/json/sk2","w") as f:
    json.dump(data,f)
    
#SkReturn
data =[{
    "pic":"Resource/item/shadow.png",
    "realsize":[50,100],
    "size":[50,100],
    "damage":0,
    "v":0,
    "life":0,
    "extra_param1":0,
    "extra_param2":0,
}]

with open("Resource/json/sk3","w") as f:
    json.dump(data,f)
    
#SkBlackHole
data =[{
    "pic":"Resource/item/blackhole.png",
    "realsize":[300,300],
    "size":[300,300],
    "damage":0,
    "v":0,
    "life":5,
    "extra_param1":150,
    "extra_param2":10,
}]

with open("Resource/json/sk4","w") as f:
    json.dump(data,f)

#SkHook
data =[{
    "pic":"Resource/item/hook.png",
    "realsize":[30,30],
    "size":[30,30],
    "damage":0,
    "v":10,
    "life":5,
    "extra_param1":0,
    "extra_param2":0,
}]

with open("Resource/json/sk5","w") as f:
    json.dump(data,f)

#SkBomb
data =[{
    "pic":"Resource/item/bomb.png",
    "realsize":[50,50],
    "size":[50,50],
    "damage":300,
    "v":0,
    "life":10,
    "extra_param1":200,
    "extra_param2":0,
}]

with open("Resource/json/sk6","w") as f:
    json.dump(data,f)
    
#SkBombExploding
data =[{
    "pic":"Resource/item/explosion.png",
    "realsize":[320,400],
    "size":[320,400],
    "damage":0,
    "v":0,
    "life":0.5,
    "extra_param1":0,
    "extra_param2":0,
}]

with open("Resource/json/sk7","w") as f:
    json.dump(data,f)
    
#SkAim
data =[{
    "pic":"Resource/item/aim.png",
    "realsize":[20,20],
    "size":[20,20],
    "damage":500,
    "v":10,
    "life":10,
    "extra_param1":50,
    "extra_param2":0,
}]

with open("Resource/json/sk8","w") as f:
    json.dump(data,f)
    
#SkAimFired
data =[{
    "pic":"Resource/item/fired.png",
    "realsize":[100,100],
    "size":[100,100],
    "damage":0,
    "v":0,
    "life":0.5,
    "extra_param1":0,
    "extra_param2":0,
}]

with open("Resource/json/sk9","w") as f:
    json.dump(data,f)
    
#SkKekkai
data =[{
    "pic":"Resource/item/kekkai.png",
    "realsize":[300,300],
    "size":[300,300],
    "damage":400,
    "v":0,
    "life":10,
    "extra_param1":150,
    "extra_param2":0,
}]

with open("Resource/json/sk10","w") as f:
    json.dump(data,f)

#SkBallReturn
data =[{
    "pic":"Resource/item/flash.png",
    "realsize":[30,30],
    "size":[30,30],
    "damage":50,
    "v":10,
    "life":10,
    "extra_param1":40,
    "extra_param2":0,
}]

with open("Resource/json/sk11","w") as f:
    json.dump(data,f)

#SkPortal
data =[{
    "pic":"Resource/item/portal.png",
    "realsize":[100,100],
    "size":[100,100],
    "damage":0,
    "v":0,
    "life":10,
    "extra_param1":50,
    "extra_param2":0,
}]

with open("Resource/json/sk12","w") as f:
    json.dump(data,f)
    
#SkTriangle
data =[{
    "pic":"Resource/item/pin.png",
    "realsize":[20,20],
    "size":[20,20],
    "damage":400,
    "v":0,
    "life":10,
    "extra_param1":0,
    "extra_param2":0,
}]

with open("Resource/json/sk13","w") as f:
    json.dump(data,f)