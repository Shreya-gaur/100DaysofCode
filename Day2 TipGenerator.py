# -*- coding: utf-8 -*-
"""
Day-2: TipCalculator #100DaysofCode

Created on Sat May  7 16:53:00 2022

@author: Shreya Gaur
"""

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
people = float(input("How many people split the bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))

payable = round((bill*(1+0.01*tip))/people, 2)
print("Each person should pay: "+ str(payable))