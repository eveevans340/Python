"""Records the users bank transactions"""
#tttt
# Defines how much money the user has after each transaction
money_list = [200]
# Inital bank balance
balance = 200

# Loop to get all the transactions
while True:
    try:
        money = int(input('Enter the money spent: '))
        if money == 0:
            break
        money_str = str(money)
        if '-' in money_str:
            print('This is not a valid transaction.')
        # Calculating balance
        balance = balance - money
        # Adding balances to money_list
        money_list.append(balance)
        #Conditions for the loop to break
        if balance <= 0:
            break 
    # Message if the user enters a non integer
    except ValueError:
        print('This is not a valid transaction.')

# Printing out the money_list
print('My bank balances have been:')
for word in money_list:
    print(word)
    