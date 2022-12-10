print("This program will print first n Fibonacci numbers.")

# Taking input from user
n = int(input('Enter a positive value for n: '))

if n == 1:
    print(0)

elif n > 1:
    # storing and printing the first two fibonacci numbers
    x = 0
    y = 1
    print(x)
    print(y)
    i = 0
    while i < n - 2:  # loop to get fibonacci numbers for (n-2) numbers
        z = x + y
        x = y
        y = z
        print(z)
        i += 1

# for negative numbers and zero
else:
    print('Invalid input.')
