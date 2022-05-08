# -*- coding: utf-8 -*-
"""
Day 4: RockPaperSc #100DaysOfCode

Created on Sat May  7 18:58:40 2022

@author: Shreya Gaur
"""

import random

while True: 
    user = int(input("What did you chose? 0: ROCK, 1: PAPER, 2: SCISSORS 5: QUIT \n"))
    if user == 0:
        print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
    elif user == 1:
        print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)
    elif user == 2:
        print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)
    elif user == 5:
        print("GAME OVER")
        break
    else:
        print("INVALID INPUT")
    
    output_list = [0,1,2]
    
    computer = output_list[random.randint(0,2)]
    
    print("Computer's Choice:")
    if computer == 0:
        print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
    elif computer == 1:
        print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)
    elif computer == 2:
        print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)
    
    
    if computer==user:
        print("DRAW")
    elif computer == 0 and user == 1:
        print("You win")
    elif computer == 0 and user == 2:
        print("You lose")
    elif computer == 1 and user == 2:
        print("You win")
    elif computer == 1 and user == 0:
        print("You lose") 
    elif computer == 2 and user == 0:
        print("You win")
    elif computer == 2 and user == 1:
        print("You lose")
     
    

