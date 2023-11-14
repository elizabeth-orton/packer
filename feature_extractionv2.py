import argparse
import os
import csv
#takes in a directory argument from command line

parser = argparse.ArgumentParser()
parser.add_argument("directory")
args = parser.parse_args()
directory = args.directory
filelist = []
for subdir, dirs, files in os.walk(directory):
    for file in files:
        filelist.append(os.path.join(subdir, file))
def fileDeal(file): #converts a file to just lowercase letters and changes all non-alpha characters to # (spaces are *)
    nfile = ""
    for char in file:
        if char.isalpha():
            nfile += char.lower()
        elif char.isnumeric():
            nfile += char
        elif char == " ":
            nfile += "*"
        else:
            nfile += "#"
    return nfile
file = "Hello. www} w"
#this is what i think the feature vector for the example "file" should look like:
featureSetGoal = {"hel", "ell", "llo", "lo#", "o#*", "#*w", "*ww", "www", "ww#", "w#*"} 
#this transforms the file into a directory containing all of the three-character combinaions in the file
def makeVector(file):
    newfile = fileDeal(file)
    featureSet = set(())
    i = 0
    while i < (len(newfile)-2):
        featureSet.add(newfile[i:i+3])
        i+=1
    return featureSet
featureSet = makeVector(file)
#this is a check
if featureSet == featureSetGoal:
    print("Success!")
else:
    print("Not quite!")
#this does the same transformation on all the files in the directory in the command line
with open('vectorfilev2.csv', 'w', newline = '') as vf:
    writer = csv.writer(vf)
    writer.writerow(['name', 'vector'])
for i in filelist:
    try:
        with open(i) as file:
            readfile = file.read()
        efvector = makeVector(readfile)
        with open('vectorfilev2.csv', 'a', newline='') as vf:
            writer = csv.writer(vf)
            writer.writerow([i, efvector])
    except:
        pass
