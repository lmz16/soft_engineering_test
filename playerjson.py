import json

data = [{
    "size":[70,80],
    "realsize":[40,80],
    "life_value":1000,
    "static":[
        "Resource/character/wdn/static0.png",
        "Resource/character/wdn/static1.png",
        "Resource/character/wdn/static0.png",
    ],
    "move":[
        "Resource/character/wdn/move0.png",
        "Resource/character/wdn/move1.png",
        "Resource/character/wdn/move2.png",
    ],
    "attack":[
        "Resource/character/wdn/attack0.png",
        "Resource/character/wdn/attack1.png",
        "Resource/character/wdn/attack2.png",
    ],
    "attacked":[
        "Resource/character/wdn/attacked.png",
        "Resource/character/wdn/attacked.png",
        "Resource/character/wdn/attacked.png",
    ],
    "v":[5,5],
    "skill":[5,9,3]
}]

with open("Resource/json/character2","w") as f:
    json.dump(data,f)


import json

data = [{
    "size":[70,80],
    "realsize":[40,80],
    "life_value":1000,
    "static":[
        "Resource/character/twd/static0.png",
        "Resource/character/twd/static1.png",
        "Resource/character/twd/static2.png",
    ],
    "move":[
        "Resource/character/twd/static0.png",
        "Resource/character/twd/static1.png",
        "Resource/character/twd/static2.png",
    ],
    "attack":[
        "Resource/character/twd/attack0.png",
        "Resource/character/twd/attack1.png",
        "Resource/character/twd/attack2.png",
    ],
    "attacked":[
        "Resource/character/twd/attacked.png",
        "Resource/character/twd/attacked.png",
        "Resource/character/twd/attacked.png",
    ],
    "v":[5,5],
    "skill":[4,6,7]
}]

with open("Resource/json/character3","w") as f:
    json.dump(data,f)