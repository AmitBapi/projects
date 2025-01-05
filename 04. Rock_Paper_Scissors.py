import random

print("PLAY ROCK PAPER SCISSORS ")
print('"0" for rock -- "1" for paper -- "2" for scissors')
# Rock
rock = ('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''')

# Paper
paper = ('''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    ''')

# Scissors
scissors = ('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')

game_images = [rock, paper, scissors]

user_choice = int(input("Enter your choice: "))
if user_choice >=0 and user_choice <=2:
    print("you choose \n", game_images[user_choice])
computer_choice = random.randint(0, 2)
print("Computer choose \n", game_images[computer_choice])

if (user_choice >=2 or user_choice <0):
    print("Invalid choice. Please enter a number between 0 and 2.")
    exit()
elif (user_choice==computer_choice):
    print("match draw")
    exit()
elif ((user_choice==0 and computer_choice==2) or 
      (user_choice==1 and computer_choice==0) or 
      (user_choice==2 and computer_choice==1)):
    print("You win!")
    exit()
else:
    print("You lose!")
    exit()


#or
# user_choice = int(input("Enter your choice: "))
# computer_choice = random.randint(0, 2)

# if user_choice==0:
#     print("You chose rock.\n", rock)
#     if computer_choice==0:
#         print("Computer chose rock. It's a tie!\n", rock)
#         exit()
#     elif computer_choice==1:
#         print("Computer chose paper. You lose!\n", paper)
#         exit()
#     else:
#         print("Computer chose scissors. You win!\n", scissors)
#         exit()
# elif user_choice==1:
#     print("You chose paper.\n", paper)
#     if computer_choice==0:
#         print("Computer chose rock. You win!\n", rock)
#         exit()
#     elif computer_choice==1:
#         print("Computer chose paper. It's a tie!\n", paper)
#         exit()
#     else:
#         print("Computer chose scissors. You lose!\n", scissors)
#         exit()
# elif user_choice==2:
#     print("You chose scissors.\n",scissors)
#     if computer_choice==0:
#         print("Computer chose rock. You lose!\n",rock)
#         exit()
#     elif computer_choice==1:
#         print("Computer chose paper. You win!\n", paper)
#         exit()
#     else:
#         print("Computer chose scissors. It's a tie!\n", scissors)
#         exit()
# else:
#     print("Invalid choice. Please try again.")
#     exit()
