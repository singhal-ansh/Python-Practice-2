"""Write a Python program that takes an input n Then it prints the following for each number till n (including n) :
"Fizz" if the number is divisible by 3, "Buzz" if the number is divisible by 5, and "FizzBuzz" if the number is
divisible by both 3 and 5. """
# Taking input from user and converting input to integer
user = input("Enter a positive integer: ")
user = int(user)

# Program will check if input is divisible by 3, 5 or both and will give corresponding output as asked in the question.
# For other numbers a blank line will be printed.
for i in range(1, user + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print("")
