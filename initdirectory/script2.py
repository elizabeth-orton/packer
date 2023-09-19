import os
import random
def hangman(word, wrongs, rights, letters):
    if wrongs>0:
        print("Incorrect guesses: ", letters)
    ##make the noose/hangman
    print("  __________________\n |                  |\n |                  |")
    if wrongs>0:
        print(" |                  O")
    if wrongs>1 and wrongs<5:
        print(" |                  |")
    if wrongs==5:
        print(" |                 /|")
    if wrongs==6:
        print(" |                 /|\ ")
    if wrongs==3:
        print(" |                 /")
    if wrongs>3:
        print(" |                 / \ ")
    if wrongs>=3:
        print(" |\n |\n |")
    if wrongs==2:
        print(" |\n |\n |\n |")
    if wrongs == 1:
        print(" |\n |\n |\n |\n |")
    if wrongs ==0:
        print(" |\n |\n |\n |\n |\n |")
    print("___")
    ##make the blanks/fill in where needed
    toprint = "       "
    for i in word:
        if i in rights:
            toprint+= i
        else:
            toprint+="_"
        toprint+=" "
    print(toprint)
letters="" ##the incorrect guesses
rights = [] ##the correct guesses
guesses=0 ##the number of incorrect guesses
won=False
print("Welcome to hangman!")



word = input("Player 1, input your word:\n")
os.system("clear") 



while not(won) and guesses<6:
    hangman(word,guesses,rights,letters)
    guess = input("Player 2, guess a letter:\n")
    if guess in word:
        rights+=guess
    else:
        letters+=guess
        guesses+=1
    won = True
    for i in word:
        if not(i in rights):
            won = False
    os.system("clear")
if won:
    hangman(word,guesses,rights,letters)
    print("Player 2 won!")
else:
    hangman(word,guesses,rights,letters)
    print("You lost. The word was", word)









