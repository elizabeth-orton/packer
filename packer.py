#!/usr/bin/env python3
import argparse

#take in command line arguments
def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="This is your unencrypted code directory", type = str)
    parser.add_argument("-key", "-k", dest = "k", help = "Input your preferred key in integer form", type = int)
    parser.add_argument('-outfile', "-o", dest = "output", help ="Output directory name.", required = True, type = str)
    args = parser.parse_args()
    return args



#gets unencrypted data
def opendata(f):
    with open(f) as data:
     read_data = data.read()
    return read_data


def xwrite(f, k, o):
    def asciimultiplied(f, k):
        encrypted = []
        encrypted += [k*ord(i) for i in f]
        return encrypted
    cipher = asciimultiplied(f, k)
    #writes decryption algorithm to output file
    with open(o, "w") as t:
        t.write("""
def decrypt(f, k):
            decrypted = ""
            for i in f:
                j = int(i/k)
                decrypted += chr(j)
            return decrypted
        """)
    return cipher
def addwrite(f, k, o):
    #basically a caesar cipher but it does the same thing to every character, including non-alpha characters
    def additionEncryption(f, k):
        encrypted = []
        for i in f:
            encrypted += chr((k + ord(i))%128)
        return encrypted
    cipher = additionEncryption(f, k)
    #writes decryption algorithm to output file
    with open(o, "w") as t:
        t.write("""
def decrypt(f, k):
        decrypted = ""
        for i in f:
            decrypted = decrypted.__add__(chr((ord(i)-k)%128))
        return decrypted
        """)
    return cipher
def caesarwrite(f, k, o):
    #just a pure caesar cipher
    def caesar_cipher(text, shift):
        encrypted_text = []
        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                shifted = ord(char) + shift
                if shifted > ord('z'):
                    shifted -= 26
                char = chr(shifted)
                if is_upper:
                    char = char.upper()
            encrypted_text += char
        return encrypted_text
    cipher = caesar_cipher(f, k)
    with open(o, "w") as t:
        t.write("""
def decrypt(f, k):
    decrypted = ""
    for char in f:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = ord(char) - k
            if shifted < ord('a'):
                shifted += 26
            char = chr(shifted)
            if is_upper:
                char = char.upper()
        decrypted += char
    return decrypted
        """)
    return cipher
def restwrite(o, c, k):
    with open(o, "a") as t:
        t.write("\ncipher = " + str(c))
        t.write("\nkey =" + str(k))
        t.write("\nexec(decrypt(cipher, key))")
def test():
    print("hello world")


