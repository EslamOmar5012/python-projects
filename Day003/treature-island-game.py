print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Wellcome to Treasure Island.\n" + "Your mission is to find the treasure")

first_move = input("you're at a cross read. Where do you want to go? Type \"left\" or \"right\" \n").lower()

if first_move != "left":
    print("Fall into a hole. \n" + "game over.")
else:
    second_move = input(
        "you come to a lake. There is an island in the middle of the lake. Type \"wait\" for a boat. Type \"swin\" to swim across.\n").lower()
    if second_move != "wait":
        print("Attacked by trout. \n" + "game over.")
    else:
        third_move = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which colour do you choose?\n").lower()
        if third_move == "red":
            print("Burned by fire.\n" + "game over.")
        elif third_move == "blue":
            print("Eaten by beasts.\n" + "game over.")
        elif third_move == "yellow":
            print("You won!")
        else:
            print("Game Over.")
