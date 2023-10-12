import argparse
#takes in a file argument from command line
#this could be expanded to a directory i just haven't done that yet
parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
f = args.file

def fileDeal(file): #converts a file to just lowercase letters and changes all non-alpha characters to # (spaces are *)
    nfile = ""
    for char in file:
        if char.isalpha():
            nfile += char.lower()
        elif char == " ":
            nfile += "*"
        else:
            nfile += "#"
    return nfile
file = "Hello. www} w"
#this is what i think the feature vector for the example "file" should look like:
featureDictGoal = {"hel": 1, "ell": 1, "llo": 1, "lo#": 1, "o#*":1, "#*w":1, "*ww": 1, "www": 1, "ww#":1, "w#*": 1} 
#this transforms the file into a directory containing all of the three-character combinaions in the file
def makeVector(file):
    newfile = fileDeal(file)
    featureDict = {}
    i = 0
    while i < (len(newfile)-2):
        j = newfile[i:i+3]
        featureDict[j] = 1
        i+=1
    return featureDict
featureDict = makeVector(file)
#this is a check
if featureDict == featureDictGoal:
    print("Success!")
else:
    print("Not quite!")
#this does the same transformation to the file from the command line
with open(f) as file:
    readfile = file.read()
efvector = makeVector(readfile)
print(efvector)
