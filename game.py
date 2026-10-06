class Player:
    def __init__(self, name, agility, damage, health, intelligence, charisma, weapon):
        self.name = name
        self.agility = agility
        self.damage = damage
        self.health = health
        self.intelligence = intelligence
        self.charisma = charisma
        self.weapon = weapon

    def attack(self, enemy):
        enemy.health -= self.weapon.damage * self.agility
        print(f"{self.name} attacks with {self.weapon.name} for {self.weapon.damage} damage!")

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

decepticon = Enemy("Megatron", 2000)
blaster = Weapon("Blaster", 300)

player1 = Player("Bumble Bee", 100, 1.5, 1000, 300, 500, blaster)

print(player1.name, player1.health)

player1.attack(decepticon)
print(f"{decepticon.name}'s health: {decepticon.health}")

print(input("whatever"))
