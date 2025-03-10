"""This program will ask the use for their name and favourite numbers and then perform some simple maths on the numbers"""

# Ask the use for their name and favourite numbers
name = input('What is your name? ')
num1 = int(input('What is your favourite number? '))
num2 = int(input('What is your second favourite number? '))

# Perform some simple maths on the numbers

add = num1 + num2
multiply = num1 * num2

# Greet the user and print the results

print(f'Hi {name}, here are some fun calculations with your favourite numbers: {num1} + {num2} = {add} \n {num1} * {num2} = {multiply}')