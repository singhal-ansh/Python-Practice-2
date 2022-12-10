# First we take input from the user and convert it to integer.
n = input('Please enter a positive number greater than 1: ')
n = int(n)

# Defining a new variable, the value of which will be the result.  
answer = 'prime'

# 1, 0 and negative integers cannot be prime numbers.
if n <= 1:
    answer = 'not prime'

if n == 2:
    answer = 'prime'

# The program will check if the input is divisible by all numbers within the range of 2 and the input itself (with
# the exception of the inputed number).

elif n % 2 == 0:
    answer = 'not prime'

else:
    for i in range(3, int(n ** 0.5) + 1, 2):
        print(f'Checking for {i}')
        if n % i == 0:
            answer = 'not prime'
            break  # this will not give repeated outputs

# Printing final result. 
print(answer)

'''
2 --> n
2, odd numbers
2, odd numbers till n//2
2, odd numbers till sqrt(n)
'''

'''
n = f1 * f2

n//2 

99 // 2 = 49
'''

'''
n --> prime or not

2, odd number till n//2

n = a * b

b > a

a <= 5 ** 0.5

144 --- 
12 * 12
4 * 36
9 * 16
18 * 8
....

sqrt(n)

2... sqrt(n)

'''
