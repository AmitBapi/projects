import random
stages_hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ["animal", "cloths", "household"]
lives = 6

# Choose a random word from the list and print it out.
choosen_word = random.choice(word_list)
len_cword = len(choosen_word)
print(choosen_word)

place_holder= "_"
for letter in range(len_cword):
    place_holder += "_"
print(place_holder)


#  # let user choose again using while loop
game_over = False
correct_letter_save = []
while not game_over:
    guess = input("\nChoose a letter to guess the word : ").lower()

    display = ""
    for letter in choosen_word:
        if letter == guess:
            display+=letter
            correct_letter_save.append(guess)
        elif letter in correct_letter_save:
            display+=letter
        else:
            display+="_"
    print(display)
    
    if guess not in choosen_word:
        lives-=1
        if lives == 0:
            game_over=True
            print("you loose")
    
    if "_" not in display:
        game_over =True
        print("you win")
    
    print(stages_hangman[lives])