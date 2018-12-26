import json

data = [{
    "pointer":3,
    "data":[
        {
            "config_file":"Resource/json/character1",
            "pic":"Resource/character/lmz/static0.png"
        },
        {
            "config_file":"Resource/json/character2",
            "pic":"Resource/character/wdn/static0.png"
        },
        {
            "config_file": "Resource/json/character3",
            "pic": "Resource/character/twd/static0.png"
        },
    ],
}]

with open ("json/player_choose","w") as f:
    json.dump(data,f)