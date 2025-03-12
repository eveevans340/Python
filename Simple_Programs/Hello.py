name = input('What is your name? ').title()
print(f'Hello {name}, nice to meet you!')

try:
    age = int(input('What is your age? '))
    if age <= 0:
          print('Please enter a positive number.')
except ValueError:
    print('Please enter a number')

if age == 29:
    print('Great age')
else:
    print('Lame')