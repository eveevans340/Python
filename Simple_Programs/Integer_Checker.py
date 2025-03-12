"""This program will check to see if the user has entered a valid integer in a specific range of values"""

# Use constants for the low and high variables
LOW = 1
HIGH = 10

# Ask the user to enter a number

num = input('Please enter a number ')

# Check to see if the number is valid
if num.lstrip('-').isnumeric():
    num = int(num)
    if num < LOW:
        print(f'{num} is lower than {LOW}')
    elif num > HIGH:
        print(f'{num} is higher than {HIGH}')
    else:
        print(f'Your number is {num}')
else:
    print(f'{num} is not an integer')