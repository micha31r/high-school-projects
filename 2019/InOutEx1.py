#-------------------------------------------------------------------------------
# Name:        Sentence
# Purpose:
#
# Author:      liyumichael.ren
#
# Created:     06/06/2019
# Copyright:   (c) liyumichael.ren 2019
# Licence:     <MIT>
#-------------------------------------------------------------------------------

def main():
    name = input("What is your name?")
    age = input("How old are you?")
    height = input("What height are you?")
    sentence = f"Hello {name}. You are {age} years old, and your height is {height}"
    print(sentence)

main()