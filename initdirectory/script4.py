n1 = input("What is your divisor? \n")
n2 = input("What is your dividend? \n")
if not(n1.isnumeric() and n2.isnumeric()):
    print("Please enter two numbers")
    quit()
if int(n2)%int(n1) == 0:
    print("Yes,", n2, "is divisible by", n1, "!\nThe quotient is", int(n2)/int(n1))
else:
    print("No,", n2, "is not divisible by", n1, "\nThe remainder is", int(n2)%int(n1))
