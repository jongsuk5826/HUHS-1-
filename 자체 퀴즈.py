class Pokemon :
    def __init__(self, name, type, attack, hp) :
        self.name = name
        self.type = type
        self.attack = attack
        self.hp = hp
    
    def normalattack(self) :
        print("{0}의 차례다! \n{1} 피해를 입혔다!".format(self.name, self.attack))
    
    def hit(self, dmg) :
        print("{0}은(는) {1} 피해를 입었다!".format(self.name, dmg))
        self.hp -= dmg
        if self.hp <= 0 :
            print("{0}은(는) 쓰러졌다!".format(self.name))

class Electric :
    def __init__(self, skill_name, skill_dmg) :
        self.skill_name = skill_name
        self.skill_dmg = skill_dmg
    
    def skill(self) :
        print("{0}(으)로 공격! {1} 피해를 입혔다!".format(self.skill_name, self.skill_dmg))

class Pikachu(Pokemon, Electric) :
    def __init__(self, name, type, attack, hp, skill_name, skill_dmg, clothes) :
        Pokemon.__init__(self, name, type, attack, hp)
        Electric.__init__(self, skill_name, skill_dmg)
        self.clothes = clothes
    
    def skillattack(self) :
        print("{0}의 차례다!".format(self.name))
        self.skill()

def printHP() :
    print("피카츄:",jiu_pikachu.hp)
    print("로켓단:",rocket_pikachu.hp)
    print()

jiu_pikachu = Pikachu("피카츄", "전기", 55, 120, "백만볼트", 80,'doctor')
rocket_pikachu = Pikachu("로켓단", "전기", 45, 140, "볼트태클", 100, "idol")

jiu_pikachu.normalattack()
rocket_pikachu.hit(jiu_pikachu.attack)
printHP()
rocket_pikachu.skillattack()
jiu_pikachu.hit(rocket_pikachu.skill_dmg)
printHP()
jiu_pikachu.skillattack()
rocket_pikachu.hit(jiu_pikachu.skill_dmg)
printHP()
rocket_pikachu.normalattack()
jiu_pikachu.hit(rocket_pikachu.attack)
printHP()