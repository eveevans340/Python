'''This program asks for an angle and then calculates the runway number of that angle, it then prints out each runway number in order'''

# Creates list for the runway numbers
runway_list = []
# Minimum angle
MIN_ANGLE = 0
# Maximum angle
MAX_ANGLE = 359

# Asking for an angle
while True:
    try:
        angle = (input('Enter your angle please: '))

        # Condition to break the loop
        if angle == 'complete':
            break

        # Converting the angle into an integer
        angle = int(angle)

        # Minimum and Maximum number for program to run
        if angle < MIN_ANGLE or angle > MAX_ANGLE:
            print('ERROR: INVALID ANGLE')

        # Calculation for the runway number
        runway_number = (angle + 4 ) / 10
        runway_rounded = int(runway_number)

        # Changing the runway number to 0 if runway_calculation equals 36
        if runway_number == 36:
            runway_number = 0

        # Adding the runway number onto the list
        runway_list.append(runway_rounded)

    except ValueError:
        print('ERROR: INVALID ANGLE')

# Printing all of the runway numbers
for number in runway_list:
    print(number)