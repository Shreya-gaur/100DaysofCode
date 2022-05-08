# -*- coding: utf-8 -*-
"""
Day 5- Password Generator #100daysofCode

Created on Sat May  7 19:40:28 2022

@author: Shreya Gaur
"""

import string
import random
print("Welcome to PyPassword Generator!")
len_pass = int(input("How many letters would you like your password to contain? "))
sym_cnt = int(input("How many symbols would you like? "))
num_cnt = int(input("How many numbers would you like? "))

if sym_cnt + num_cnt >= len_pass:
    print("Number of symbols and digits exceeded password length.")
else:
    symbols = ['!', '#', '$', '%', '&', '*', '+']
    ch_sym = random.choices(symbols,k = sym_cnt)
    
    numbers = list(string.digits)
    ch_num = random.choices(numbers,k = num_cnt)
    
    remain = len_pass - sym_cnt - num_cnt
    
    num_low = random.randint(1,remain)
    num_high = len_pass - num_low
    
    letters_lower = list(string.ascii_lowercase)
    ch_low = random.choices(letters_lower,k = num_low)
    
    letters_upper = list(string.ascii_uppercase)
    ch_high = random.choices(letters_upper,k = num_high)
    
    passwd_list = ch_sym + ch_num + ch_low + ch_high
    
    random.shuffle(passwd_list)
    
    password = ''
    for char in passwd_list:
        password = password + char
    
    print(f"\nYour password is: {password}")

