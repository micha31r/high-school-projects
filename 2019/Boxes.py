#-------------------------------------------------------------------------------
# Name:        Boxes
# Purpose:
#
# Author:      liyumichael.ren
#
# Created:     06/06/2019
# Copyright:   (c) liyumichael.ren 2019
# Licence:     <MIT>
#-------------------------------------------------------------------------------

def main():
	width = input("Enter a width:")
	height = input("Enter a height:")
	filled = input("Fill Box(y/n):")
	print("Here is your box:")
	for h in range(int(height)):
		if filled == "y":
			print("+ "*int(width))
		elif filled == "n":
			if h == 0 or h == int(height)-1:
				print("+ "*int(width))
			else:
				print("+ ".ljust(int(width)*2-3, " "), "+")

main()
