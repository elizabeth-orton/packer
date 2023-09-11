def asciix2(f):
    encrypted = []
    encrypted += [2*ord(i) for i in f]
    return encrypted
with open('unencryptedcode.py') as data:
    read_data = data.read()

cipher = asciix2(read_data)
t = open("packedcode.py", "x")
t.write("""
def decryptasciix2(f):
    decrypted = ""
    for i in f:
        j = int(i/2)
        decrypted += chr(j)
    return decrypted
""")
t.close()
t = open("packedcode.py", "a")
t.write("cipher = " + str(cipher))
t.write("\nexec(decryptasciix2(cipher))")
t.close()

