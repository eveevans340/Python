"""Getting user input and then telling the user if they can vote in New Zealand or not"""

# Asking for the user name, age, and residency

name = input('Please enter your name: ').title()
age = int(input('Please enter your age: '))
residency = input('Are you a resident of New Zealand(yes/no): ').lower()

# Code to decide whether they can vote or not

if age > 17 and residency == 'yes':
    print(f'{name} you are able to vote.')
else:
    print('You are not able to vote.')