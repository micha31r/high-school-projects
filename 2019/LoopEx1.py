#-------------------------------------------------------------------------------
# Name:        Time Table
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
    for i in range(12):
    	print(f"{i+1} x {number} ="+str((i+1)*int(number)))

main()