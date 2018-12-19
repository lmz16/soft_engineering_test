import json

data = [{
    "main_bk_pic":"Resource/interface/start_interface.jpg",
    "cursor_pic":"Resource/interface/cursor.png",
    "single_button":"Resource/interface/start_button_single.png",
    "setting_button":"Resource/interface/start_button_setting.png",
    "online_button":"Resource/interface/start_button_online.png",
    "help_button":"Resource/interface/start_button_help.png",
    "custom_button":"Resource/interface/start_button_custom.png",
    "help_text":'Resource/interface/help_text.png',
    "setting_text":'Resource/interface/setting_text.png',
    "setting_choose":'Resource/interface/setting_choose.png',
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
    "v":[5,5]
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

data =[{
    "pic":"Resource/item/fire_ball.png",
    "realsize":[50,50],
    "size":[50,50],
    "damage":200,
    "v":[30,30],
    "life":5,
}]

with open("Resource/json/sk1","w") as f:
    json.dump(data,f)