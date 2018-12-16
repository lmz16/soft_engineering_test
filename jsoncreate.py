import json

data = [{
    "main_bk_pic":"Resource/interface/start_interface.jpg",
    "cursor_pic":"Resource/interface/cursor.png",
    "single_button":"Resource/interface/start_button_single.png",
}]

with open("Resource/json/interface","w") as f:
    json.dump(data,f)

data = [{
    "bottom_pic":'Resource/interface/single_choose_background.jpg'
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
}]

with open("Resource/json/character1","w") as f:
    json.dump(data,f)

data = [{
    "size":[60,100],
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
}]

with open("Resource/json/enemy1","w") as f:
    json.dump(data,f)