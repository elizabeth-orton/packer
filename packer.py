import argparse

#take in command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("file", help="This is your unencrypted code file", type = str)
parser.add_argument("-key", "-k", dest = "k", help = "Input your preferred key in integer form", required=True, type = int)
parser.add_argument("-algorithm", "-a", dest = "a", nargs='?', choices = ["ASCII mulitplication"], help = "Defaults to ASCII multiplication, which is also the only option.")
parser.add_argument('-outfile', "-o", dest = "output", help ='Output file name', required = True, type = str)
args = parser.parse_args()
#initial encryption algorithm
def asciimultiplied(f, k):
    encrypted = []
    encrypted += [k*ord(i) for i in f]
    return encrypted
#gets unencrypted data
with open(args.file) as data:
    read_data = data.read()
key = args.k
#encrypts said data
if args.a == "ASCII multiplication" or args.a == None:
    cipher = asciimultiplied(read_data, key)
    #writes decryption algorithm to output file
    with open(args.output, "w") as t:
        t.write("""
    def decryptasciix(f, k):
            decrypted = ""
            for i in f:
                j = int(i/k)
                decrypted += chr(j)
            return decrypted
        """)
#writes encrypted code to output file and tells it to decrypt itself
with open(args.output, "a") as t:
    t.write("\ncipher = " + str(cipher))
    t.write("\nkey =" + str(key))
    t.write("\nexec(decryptasciix(cipher, key))")


