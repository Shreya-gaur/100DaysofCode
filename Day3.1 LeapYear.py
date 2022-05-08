# -*- coding: utf-8 -*-
"""
Day 3.1: Leap Year Challenge

Created on Sat May  7 17:50:13 2022

@author: Shreya Gaur
"""

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.") 
    else:
        print(f"{year} is a leap year.")
else:
   print(f"{year} is not a leap year.")  
    