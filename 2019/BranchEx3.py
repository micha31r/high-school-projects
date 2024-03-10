#-------------------------------------------------------------------------------
# Name:        Login
# Purpose:
#
# Author:      liyumichael.ren
#
# Created:     06/06/2019
# Copyright:   (c) liyumichael.ren 2019
# Licence:     <MIT>
#-------------------------------------------------------------------------------

def main():
	print("(Real UN and PW is admin, 12345)")
	username = input("Username:")
	passwd = input("Password:")
	if username == "admin":
		if passwd == "12345":
			print("Welcome!")
		else:
			print("Sorry, Wrong Password")
	else:
		print("Sorry, but your username is not recognised")

main()