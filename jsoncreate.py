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
    "size":[120,200]

}]