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
    ]
}]

with open("Resource/json/game1","w") as f:
    json.dump(data,f)

data = [{
    "size":[120,200],
    "realsize":[80,160],
    "life_value":1000,
    "static":[
        "Resource/character/diy1/static0.png",
        "Resource/character/diy1/static1.png",
        "Resource/character/diy1/static2.png",
    ],
    "move":[
        "Resource/character/diy1/move0.png",
        "Resource/character/diy1/move1.png",
        "Resource/character/diy1/move2.png",
    ],
    "attack":[
        "Resource/character/diy1/attack0.png",
        "Resource/character/diy1/attack1.png",
        "Resource/character/diy1/attack2.png",
    ],
    "attacked":[
        "Resource/character/diy1/attacked0.png",
        "Resource/character/diy1/attacked1.png",
        "Resource/character/diy1/attacked2.png",
    ],
    "v":[10,10]
}]

with open("Resource/json/character1","w") as f:
    json.dump(data,f)

data = [{
    "size":[60,100],
    "realsize":[30,80],
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