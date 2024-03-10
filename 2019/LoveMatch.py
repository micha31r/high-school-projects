#-------------------------------------------------------------------------------
# Name:        Love Match
# Purpose:
#
# Author:      liyumichael.ren
#
# Created:     06/06/2019
# Copyright:   (c) liyumichael.ren 2019
# Licence:     <MIT>
#-------------------------------------------------------------------------------

def main():
    p1_name = input("Player 1 Name:")
    p2_name = input("Player 2 Name:")

    match = len(p1_name) * len(p2_name) % 11

    print("*"*match)

    if match <= 2:
    	print("You are a terrible match")
    elif match >= 3 and match <= 5:
    	print("You probably shouldn't bother")
    elif match >= 6 and match <= 8:
    	print("You are a good match")
    elif match >= 9 and match <= 10:
    	print("You are a perfect match!")


main()