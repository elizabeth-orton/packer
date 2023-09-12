def asciimultiplied(f, k):
    encrypted = []
    encrypted += [k*ord(i) for i in f]
    return encrypted
with open('unencryptedcode.py') as data:
    read_data = data.read()
key = 3
cipher = asciimultiplied(read_data, key)
with open("packedcode.py", "x") as t:
    t.write("""
def decryptasciix(f, k):
        decrypted = ""
        for i in f:
            j = int(i/k)
            decrypted += chr(j)
        return decrypted
    """)
with open("packedcode.py", "a") as t:
    t.write("\ncipher = " + str(cipher))
    t.write("\nkey =" + str(key))
    t.write("\nexec(decryptasciix(cipher, key))")
