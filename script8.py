#print primes
from math import sqrt
def isprime(n):
    if (n <= 1):
        return False
 
    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True

lower_limit=int(input("Enter the lower limit for the range:"))
upper_limit=int(input("Enter the upper limit for the range:"))
for j in range(lower_limit,upper_limit+1):
    if isprime(j):
        print(j)