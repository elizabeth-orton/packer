#i made this in cmu sandbox also
words = ['red', 'color', 'dog', 'banana', 'apple', 'cat', 'sky', 'chair', 'tree', 'yellow', 'oak', 'wolf' 'love', 'cake']
import random
def secretWord(word):
    tries = 10
    correct=False
    input = app.getTextInput("Guess the secret word of the day.")
    if input == word:
        Label("You guessed the secret word. Congratulations!", 200, 30, size=16)
        correct=True
    tries -= 1
    while tries > 0 and correct==False:
        input = app.getTextInput("Try again. You have " + str(tries) + " tries remaining")
        if input == word:
            Label("You guessed the secret word. Congratulations!", 200, 30, size=16)
            correct=True
        tries -= 1
    if tries == 0 and correct==False:
        Label("The word was \"" + word +"\". Better luck next time!", 200, 30, size=16)
secretWord(random.choice(words))