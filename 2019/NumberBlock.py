#-------------------------------------------------------------------------------
# Name:        Number Box
# Purpose:
#
# Author:      liyumichael.ren
#
# Created:     06/06/2019
# Copyright:   (c) liyumichael.ren 2019
# Licence:     <MIT>
#-------------------------------------------------------------------------------

def main():
	num = input("Enter max number:")
	for n in range(int(num)+1):
		if int(n) % 10 != 0:
			print(f"{n}".rjust(3," "), end=" ")
		else:
			print(f"\n {n}".rjust(3," "), end=" ")

main()