#-------------------------------------------------------------------------------
# Name:        Count
# Purpose:
#
# Author:      liyumichael.ren
#
# Created:     06/06/2019
# Copyright:   (c) liyumichael.ren 2019
# Licence:     <MIT>
#-------------------------------------------------------------------------------

def main():
    number = input("Enter a number:")
    for i in range(int(number)):
    	print(i+1)
    for a in range(int(number)):
    	print(int(number) - a-1)

main()