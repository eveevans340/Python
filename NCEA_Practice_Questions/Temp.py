"""Gets the temperature of porridge and tells the user whether is is too hot or too cold"""

# Defines the list of if the porridge is too cold, too hot or just right
porridge_list = []

# Mininum and maxium value for the porridge to be 'just right'
MIN_TEMP = 34
MAX_TEMP = 42

# Loop to get all the porridge temperatures
while True:
    try:
        porridge = int(input('Enter the temperature: '))
        #Breaking the loop if its -1
        if porridge == -1:
            break
        # Deciding if the porridge is just right or not
        if porridge >= MIN_TEMP and porridge <= MAX_TEMP:
            porridge_list.append('just right')
        elif porridge > MAX_TEMP:
            porridge_list.append('too hot')
        else:
            porridge_list.append('too cold')
    #Breaking the loop is the user enters a non number
    except ValueError:
        print('Invalid temperature.')

# Printing out the porridge_list
for word in porridge_list:
    print(word)
    