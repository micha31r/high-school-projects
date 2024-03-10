#-------------------------------------------------------------------------------
# Name:        Age group
# Purpose:
#
# Author:      liyumichael.ren
#
# Created:     06/06/2019
# Copyright:   (c) liyumichael.ren 2019
# Licence:     <MIT>
#-------------------------------------------------------------------------------

def main():
    age = input("What is your year group?")
    if int(age) <= 10:
        print("You are a junior student")
    else:
        print("You are a senior student")

main()