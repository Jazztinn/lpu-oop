class Player:
    def __init__(self, name, damage, health, weapon):
        self.name = name
        self.damage = damage
        self.health = health
        self.weapon = weapon

    def attack(self, enemy):
        enemy.health -= self.weapon.damage
        print(f"{self.name} attacks with {self.weapon.name} for {self.weapon.damage} damage!")

    def show_stats(self):
        print("=" * 30)
        print("Player Stats")
        print("=" * 30)
        print("Name:", self.name)
        print("Agility:", self.agility)
        print("Damage:", self.damage)
        print("Health:", self.health)
        print("Intelligence:", self.intelligence)
        print("Charisma:", self.charisma)
        print("=" * 30)

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
blade = Weapon("Blade", 250)


player1 = Player("Bumble Bee", 1.5, 100, 1000, 300, 500, blaster)

player1.show_stats()

print(player1.name, player1.health)

player1.attack(decepticon)
print(f"{decepticon.name}'s health: {decepticon.health}")

