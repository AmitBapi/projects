print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************\n''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure")
choice1=input('you\'re at crossroad, where do you want to go? type "LEFT" or "RIGHT" = ').lower()
if choice1 == "left":
    choice2=input('you find a lake, there is a island middle of the'
                  'lake, do you want to -- "SWIM" or "WAIT" -- for'
                  'the current? ').lower()
    if choice2 == "wait":
        choice3 = input("you arrived at the island unharmed, there is a house with three different "
                        "color doors -- RED,GREEN,YELLOW -- which one you want to open ? ").lower()
        if choice3 == "green":
            print("Congratulations! You found the treasure!")
        elif choice3 == "yellow":
            print("You entered a room full of traps. Game Over.")
        elif choice3 == "red":
            print("Burned by fire.Game Over.")
        else:
            print("You chose a wrong color door. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")