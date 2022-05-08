# -*- coding: utf-8 -*-
"""
Day 3: Treasure Island #100DaysOfCode

Created on Sat May  7 18:20:48 2022

@author: Shreya Gaur
"""

#print('''                            _.--.
#                        _.-'_:-'||
#                    _.-'_.-::::'||
#               _.-:'_.-::::::'  ||
#             .'`-.-:::::::'     ||
#            /.'`;|:::::::'      ||_
#           ||   ||::::::'     _.;._'-._
#           ||   ||:::::'  _.-!oo @.!-._'-.
#           \'.  ||:::::.-!()oo @!()@.-'_.|
#            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
#              `>'-.!@%()@'@_%-'_.-o _.|'||
#               ||-._'-.@.-'_.-' _.-o  |'||
#               ||=[ '-._.-\U/.-'    o |'||
#               || '-.]=|| |'|      o  |'||
#               ||      || |'|        _| ';
#               ||      || |'|    _.-'_.-'
#               |'-._   || |'|_.-'_.-'
#            jgs '-._'-.|| |' `_.-'
#                    '-.||_/.-'
#
#''')

print("Welcome to the Treasure Island!")
print("Your Mission is to find the treasure.")
choice = input("You are at a cross road. You can choose to go \"left\" or \"right\". \n").lower()
if choice == "right":
   print("You fell into a Hole. Game Over.")
elif choice == "left":
    choice2 = input("You have reached a torrid river with no bridge on top. Do you want to \"swim\" or \"wait?\". \n").lower()
    if choice2 == "wait":
       print("A lion came and ate you. Game Over.")
    elif choice2 == "swim":
        print("It was very difficult but you reached the other shore.")
        choice3 = input("You arrive at a house unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n").lower()
        if choice3 == "red":
            print("You found the Treasure. You won!")
        elif choice3 == "yellow":
            print("You found a bag of poisonous snakes inside. You got bit. Game Over.")
        elif choice3 == "blue":
            print("You found a piece of iron. Game Over.")
    else:
        print("You didn't make the right choice. Rewrite Command.")
else:
    print("You didn't make the right choice. Rewrite Command.")
        