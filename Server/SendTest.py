import Extern as Et

class HostTest():
    def __init__(self):
        self.count = 0
        self.test_sequence = [
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": True,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": True,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            {"player_kind": 0,
            "up": False,"down": False,"left": False,"right": False,
            "atk1": False,"atk2": False,"atk3": False,},
            
        ]


    def test(self):
        self.count += 1
        if self.count == len(self.test_sequence):
            self.count = 0
        return self.test_sequence[self.count]