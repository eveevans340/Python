""" This program checks a battery's voltage and outputs the correct sound """

# Defines the list of voltages
volt_list = []

# Minimum amount of volts a battery needs to be good
MIN_VOLTS = 1.2

# Loop to get all the battery values
while True:
    try:
        battery = float(input('Enter your input: '))
        #Breaking the loop if its a negative number
        battery_str = str(battery)
        if '-' in battery_str:
            break
        # Deciding whether the battery is good or not
        if battery >= MIN_VOLTS:
            volt_list.append('Beep')
        else:
            volt_list.append('Boop')
    #Breaking the loop is the user enters a non number
    except ValueError:
        print('Not robot compliant!')
        break

# Printing out the volt_list
for word in volt_list:
    print(word)
    