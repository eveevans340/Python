'''This program asks for an angle and then calculates the runway number of that angle, it then prints out each runway number in order'''

# Creates list for the runway numbers
runway_list = []
# Minimum angle
MIN_ANGLE = 0
# Maximum angle
MAX_ANGLE = 359
# Angle number for runway 0
ANGLE_36 = 36
# Number for Runway 0 
RUNWAY_0 = 0
# Number to add to the angle
NUM = 4
# Number to divide the angle by
DIVISOR = 10

# Asking and converting an angle to a runway number
while True:
    try:
        # Ask the user for an angle
        angle = (input('Enter your angle please: '))
        # Condition to break the loop
        if angle == 'complete':
            break
        # Converting the angle into an integer
        angle = int(angle)
        # Minimum and Maximum number for program to run
        if angle < MIN_ANGLE or angle > MAX_ANGLE:
            print('ERROR: INVALID ANGLE')
        else:
            # Calculating the runway number
            runway_calc = (angle + NUM) / DIVISOR
            # Rounding the runway number
            runway_number = int(runway_calc)
            # Calculating if the Runway is Runway 0
            if runway_number == ANGLE_36:
             runway_number = RUNWAY_0
            # Adding the runway number onto the list
            runway_list.append(runway_number)
    except ValueError:
        print('ERROR: INVALID ANGLE')

# Printing all of the runway numbers
for number in runway_list:
    print(number)