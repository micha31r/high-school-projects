#-------------------------------------------------------------------------------
# Name:        Dice Game
# Purpose:
#
# Author:      liyumichael.ren
#
# Created:     06/06/2019
# Copyright:   (c) liyumichael.ren 2019
# Licence:     <MIT>
#-------------------------------------------------------------------------------

import random

score = 0

def main():
    global score
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    score += dice1+dice2
    print("Roll 1 -----------------")
    print(f"You roll {dice1} and {dice2}")
    if dice1 != dice2:
        print(f"Your score is {score}\n")
        if input("Roll again (y/n)?") == "y":
            main()
        else:
            pass
    else:
        print("Snake eyes!!!\n")
        print("Game Over --------------")
        print(f"Your final score: {score}")
        score = 0

main()