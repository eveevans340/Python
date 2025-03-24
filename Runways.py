'''This program asks for an angle and then calculates the runway number of that angle, it then prints out each runway number in order'''

# Creates list for the runway numbers
runway_numbers = []

# Calculation for the runway numbers
runway_calculation = angle + 4 / 10

# Asking for an angle
while True:
    angle = (input('Enter your angle please:'))
    # Breaking the loop if 'complete' is entered
    if angle == 'complete':
        break
    # Converting the angle into an integer
    angle = int(angle)
    if runway_calculation == 36:
        runway_calculation = 0