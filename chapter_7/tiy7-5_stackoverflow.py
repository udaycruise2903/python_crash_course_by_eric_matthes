loop = True
#while loop = true run 'while loop'
while loop:
#Print message
    print ('Please enter your age.')
#receive input from user
    age = input()
#check if the user input "quit" if so end loop. Break ends program but should be replaceable by
#if age == 'quit':
#   loop = False
#resulting the the same effect (ending loop)
    if age == 'quit':
        break
#Convert age input by user to int so it is recognized as a number by python
    age = int(age)
#If/ elif pretty self explanatory   
    if age < 3:
        price = 5
    elif age < 12:
        price = 10
    elif age > 12:
        price = 15
    else:
        print('Input not recognized')
        break
#Print ticket price based on age and ask user if they need another price/inform them how to exit program        
    print('Your ticked price is $' + str(price) + '.')
    print('\n If you would like to check the price for another person please enter their age now or type "quit" to exit')
