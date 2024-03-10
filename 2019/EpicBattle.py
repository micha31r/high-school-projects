#-------------------------------------------------------------------------------
# Name:        Epic Battle
# Purpose:
#
# Author:      liyumichael.ren
#
# Created:     06/06/2019
# Copyright:   (c) liyumichael.ren 2019
# Licence:     <MIT>
#-------------------------------------------------------------------------------

import random, sys

# 0 is player, 1 is enemy
turn = 0

def game():
    print("Health levels:")
    print(f"You {player.health}".ljust(2," "))
    print(f"Orc {enemy.e_health}\n".ljust(2," "))
    print("Possible actions:")
    print("[a]ttack with a weapon.".ljust(2," "))
    print("[d]efend with your shield.".ljust(2," "))
    print("[c]ast spell.".ljust(2," "))
    print("[q]uit game.\n".ljust(2," "))

class player:
    health = 50
    block = 0
    heal = 1
    fire = 1
    def get_input(self):
        key = input("Your choice?")
        if key == "a":
            weapon = input("Chose Weapon([s]word [d]agger):")
            player.p_attack(key, weapon=weapon)
        elif key == "d":
            player.p_attack(key, weapon=None)   
        elif key == "c":
            spell = input("Chose Spell([h]eal [f]ire):")
            if spell == "h":
                if self.heal <= 0:
                    print("Item not avalible")
                    self.get_input()
            elif spell == "f":
                if self.fire <= 0:
                    print("Item not avalible")
                    self.get_input()
            player.p_attack(key, weapon=None, spell=spell)
        elif key == "q":
            sys.exit()
        else:
            print("Unknown Command")
            self.get_input()

    def p_attack(self, key, **kwargs):
        global turn
        if key == "a":
            if kwargs["weapon"] == "s":
                hit = random.randint(1,20)
                print("You swing your sword... ")
                if random.randint(0,4) == 0:
                    print("You missed the orc")
                else:
                    print(f"You deal the orc {hit} damage")
                    enemy.e_health -= hit
            if kwargs["weapon"] == "d":
                hit = random.randint(1,10)
                print("You swing your Dagger... ")
                print(f"You deal the orc {hit} damage")
                enemy.e_health -= hit
        elif key == "c":
            if kwargs["spell"] == "h":
                print("You Healed your self by 20 HP")
                self.health += 20
                self.heal -= 1
            elif kwargs["spell"] == "f":
                hit = random.randint(20,30)
                print("You burned the orc...")
                print(f"You deal the orc {hit} damage")
                enemy.e_health -= hit
                self.fire -= 1
        elif key == "d":
            self.block = random.randint(0,1)
        turn = 1

class enemy:
    e_health = 100
    def e_attack(self):
        global turn
        hit = random.randint(1,20)
        print("The orc attacks with its axe...")
        if player.block == 0:
            # make the enemy having 50% of change of missing
            if random.randint(0,1) == 0:
                print(f"He deals you {hit} damage\n")
                player.health -= hit
            else:
                print(f"He missed you\n")
        elif player.block == 1:
            print("You raise your shield and deflect the blow")
            print(f"The rebounding blow deals the orc {hit} damage\n")
            self.e_health -= hit
        turn = 0

    
def check_health():
    if enemy.e_health <= 0:
        print("You defeated the orc! GameOver!")
        sys.exit()
    if player.health <= 0: 
        print("The orc smashed you! GameOver!")
        sys.exit()

# Game Loop
print("You are face-to-face with an angry orc\n")

player = player()
enemy = enemy()

while True:
    try:
        game()
        if turn == 0:
            player.get_input()
        if turn == 1:
            enemy.e_attack()
        check_health()
    except KeyboardInterrupt:
        break