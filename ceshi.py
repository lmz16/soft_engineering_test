class Skill():
    def __init__(self):
        self.load()

    def load(self):
        self.size=[50,50]
        self.site=[100,100]
        self.damage=50
        self.life_value=100

    def attack_judge(self,target):
        return (
            ((self.site[0]-target.site[0])<(self.size[0]+target.size[0])/2) &
            ((self.site[1]-target.site[1])<(self.size[1]+target.size[1])/2)
        )

tempplayerskill=[]
tempplayerskill.append(Skill())

enemy_list=[]
enemy_list.append(Skill())

for skill in tempplayerskill:
    for enemy in enemy_list:
        if (skill.attack_judge(enemy)):
            enemy.life_value=enemy.life_value-skill.damage
            print('accept')
            del skill