import random
import os

HANGMANPICS = ['''
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

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
GUESS = 6
game_on = True
guess_animanl = random.choice(words)
#guess_animanl_list = list(guess_animanl)
blank = []
for i in range(len(guess_animanl)):
    blank += "_" 
while game_on:
    print(guess_animanl)
    print(GUESS)
    print("HANGMAN GAME")
    print(HANGMANPICS[len(HANGMANPICS) - GUESS - 1])
    print(blank)
    guess_letter = input("Guess The Word For Animal: ").lower()
    for position in range(len(guess_animanl)):
        if guess_letter in blank:
            print(f"you already guess letter {guess_letter}")
        elif guess_letter in guess_animanl[position]:
            print(f"Congratulation! Your Guess {guess_letter} is right")
            blank[position] = guess_letter
            if "_" not in blank:
                print(f"Congratulation! you won by {GUESS} Guess")
                os.system('clear')
                game_on = False
                break
    if guess_letter not in guess_animanl:
        GUESS = GUESS - 1
        if GUESS == 0:
            game_on = False
            print("You lose! Best of Luck for next time")
