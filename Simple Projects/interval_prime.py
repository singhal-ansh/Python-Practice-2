print("This program will print all prime no.s between two numbers specified by the user (both no.s are inclusive).")

# Taking inputs from the user
r1 = int(input('Enter first number: '))
r2 = int(input('Enter second number: '))

if r2 > r1:
    print(f"The prime no.s between {r1} and {r2} are: ")
    for x in range(r1, r2 + 1):  # selecting and printing all prime no.s between r1 and r2
        if x > 1:  # 1 is not prime
            for i in range(2, x):
                if x % i == 0:
                    break
            else:
                print(x)
if r1 > r2:
    print(f"The prime no.s between {r2} and {r1} are: ")
    for x in range(r2, r1 + 1):  # selecting and printing all prime no.s between r2 and r1
        if x > 1:  # 1 is not prime
            for i in range(2, x):
                if x % i == 0:
                    break
            else:
                print(x)
if r1 == r2:
    print('please enter different values for first and second no.')
