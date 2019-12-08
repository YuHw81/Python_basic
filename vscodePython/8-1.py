'''
두 명의 전사가 결투(류, 켄)
전사 (체력, 공격력, 공격)
'''

class Warrior:
    def __init__(self, hp, power):
        self.maxHp = hp
        self.hp = hp
        self.power = power
    def attack(self, target):
        target.hp = target.hp - self.power

ryu = Warrior(100, 10)
ken = Warrior(110, 5)

# 류와 켄의 체력
print(ryu.hp)
print(ken.hp)

# 류가 켄을 공격
ryu.attack(ken)
ryu.attack(ken)
# 공격 후의 켄의 체력
print(ken.hp)

# 켄이 류를 공격
ken.attack(ryu)
ken.attack(ryu)
# 공격 후의 류의 체력
print(ryu.hp)


# 전사를 글래디에이터로 전직
class Gladiator(Warrior):
    def attack(self, target):
        target.hp = target.hp - (self.power * 2)
    def heal(self):
        self.hp = self.hp + 50
        # 치유 후에 자기 객체의 최대 체력보다 커지면 현재 체력을 최대 체력으로 대입
        if self.hp > self.maxHp : self.hp = self.maxHp


ryu = Gladiator(100, 10)
ken = Warrior(100, 10)

# 류가 켄을 공격
ryu.attack(ken)
print(ken.hp)

# 켄이 류를 공격
ken.attack(ryu)
print(ryu.hp)
ryu.heal()
print(ryu.hp)
