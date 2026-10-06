#Legaspi, Jazztinn Kyle G.
#CS 202
#10/6/2026
#Act1

import random

#weapon class
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

#player config
class Player:
    def __init__(self, name, damage, health, weapon, level=1, xp=0):
        self.name = name
        self.damage = damage
        self.health = health
        self.weapon = weapon
        self.level = level
        self.xp = xp

    #attack and crit
    def attack(self, enemy):
        critical = random.random() < 0.2
        damage = self.damage * self.weapon.damage
        if critical:
            damage *= 2
            print("CRITICAL HIT!")

        #damage & health calculation
        enemy.health = max(0, enemy.health - damage)
        print(
            f"{self.name} attacks {enemy.name} using {self.weapon.name} "
            f"for {int(damage)} damage."
        )
        print(f"{enemy.name} HP: {int(enemy.health)}")
        return damage

    def fireball(self, enemy):
        damage = self.damage * self.weapon.damage * 2
        enemy.health = max(0, enemy.health - damage)
        print(
            f"{self.name} casts Fireball at {enemy.name} "
            f"for {int(damage)} damage."
        )
        print(f"{enemy.name} HP: {int(enemy.health)}")
        return damage

    #heal method
    def heal(self, amount=25):
        old_health = self.health
        self.health = min(100, self.health + amount)
        print(f"{self.name} heals for {self.health - old_health} HP.")

    #stats config
    def show_stats(self):
        print("=" * 30)
        print("Player Stats")
        print("=" * 30)
        print("Name:", self.name)
        print("Level:", self.level)
        print("Damage:", self.damage)
        print("Health:", self.health)
        print("XP:", self.xp)
        print("Weapon:", self.weapon.name)
        print("=" * 30)

    def menu(self):
        print("=== MENU ===")
        print("1. Attack")
        print("2. Heal")
        print("3. Show Stats")
        print("4. Exit")
        choice = input("Choose an action: ")
        return choice

    
#enemy method
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

#weapons
sword = Weapon("Sword", 30)
staff = Weapon("Staff", 25)
bow = Weapon("Bow", 20)

#players
knight = Player("Knight", 1, 100, sword)
mage = Player("Mage", 1, 100, staff)
archer = Player("Archer", 1, 100, bow)

#enemies
goblin = Enemy("Goblin", 100)
skeleton = Enemy("Skeleton", 100)
zombie = Enemy("Zombie", 100)

knight.show_stats()

knight.menu()

print("=== BATTLE START ===")
knight.attack(goblin)
mage.fireball(skeleton)
archer.attack(zombie)

