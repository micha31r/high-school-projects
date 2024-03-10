#-------------------------------------------------------------------------------
# Name:        BMI
# Purpose:
#
# Author:      liyumichael.ren
#
# Created:     06/06/2019
# Copyright:   (c) liyumichael.ren 2019
# Licence:     <MIT>
#-------------------------------------------------------------------------------

def main():
    height = input("What is your height?")
    weight = input("What is your weight?")
    bmi = float(weight) / (float(height) * float(height))
    print(f"Your BMI is {bmi}")

main()
