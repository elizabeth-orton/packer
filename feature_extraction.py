import itertools
import numpy as np
#create dictionary with spots for each possible three-character sequence
charList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "*"] #this is to keep the complexity moderate
combs = np.array(itertools.combinations_with_replacement(charList, 3)) #maybe I'm using the numpy thing wrong
print(combs) #see what's in there
def fileDeal(file): #converts a file to just lowercase letters and changes all non-alpha characters to *
    nfile = []
    for char in file:
        if char.isalpha():
            nfile += char.lower()
        else:
            nfile += "*"
    return nfile
f = "Hello. xYz"
for i in f:
    #i am not sure what to do here
    continue


