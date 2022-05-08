# -*- coding: utf-8 -*-
"""
Day 2.3: LifeinWeeks #100DaysofCode

Created on Sat May  7 17:27:41 2022

@author: Shreya Gaur
"""

age = int(input("What is your current age? "))

months_left = (90 - age) * 12

weeks_left = (90 - age) * 52

days_left = (90 - age) * 365

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left.") 