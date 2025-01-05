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

user_choice = int(input("Enter your choice: "))
computer_choice = random.randint(0, 2)

if user_choice==0:
    print("You chose rock.")
    print(rock)
    if computer_choice==0:
        print("Computer chose rock. It's a tie!")
        print(rock)
        exit()
    elif computer_choice==1:
        print("Computer chose paper. You lose!")
        print(paper)
        exit()
    else:
        print("Computer chose scissors. You win!")
        print(scissors)
        exit()
elif user_choice==1:
    print("You chose paper.")
    print(paper)
    if computer_choice==0:
        print("Computer chose rock. You win!")
        print(rock)
        exit()
    elif computer_choice==1:
        print("Computer chose paper. It's a tie!")
        print(paper)
        exit()
    else:
        print("Computer chose scissors. You lose!")
        print(scissors)
        exit()
elif user_choice==2:
    print("You chose scissors.")
    print(scissors)
    if computer_choice==0:
        print("Computer chose rock. You lose!")
        print(rock)
        exit()
    elif computer_choice==1:
        print("Computer chose paper. You win!")
        print(paper)
        exit()
    else:
        print("Computer chose scissors. It's a tie!")
        print(scissors)
        exit()
else:
    print("Invalid choice. Please try again.")
    exit()