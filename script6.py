# from https://www.w3resource.com/python-exercises/generators-yield/python-generators-yield-exercise-4.php 

def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

# Accept input from the user
n = int(input("Input the number of Fibonacci numbers you want to generate? "))

print("Number of first ",n,"Fibonacci numbers:")
fib = fibonacci()
for _ in range(n):
    print(next(fib),end=" ")