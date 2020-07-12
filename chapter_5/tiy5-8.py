
    
# remove items from the lists
users.remove[1:]

user = 'mahesh'

if user in users:
    print("Welcome")
else:
    print("We need some users")
    
# checking empty list
users = []

if users:
    for user in users:
        print("Welcome "+ user +".")
    print(" you have some notifications.")
else:
    print("We need some users")
    
#checking usernames
current_users = ['Gita' , 'mrunalini', 'aparna', 'sampath', 'siva']

new_users = ['govind', 'vaishnavi', 'keertan','gita', 'Siva']

for new_user in new_users:
    if new_user.lower() in current_users.lower():
        print(new_user + " - please enter a new username.")
    else:
        print(new_user + " is available.")
        
#ordinal numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if 'number' in numbers == 1:
    ordinal = 'st'
elif 'number' in numbers == 2:
    ordinal =  'nd'
else:
    ordinal == 'rd'

for number in numbers:
    print(number+ordinal)
    

#simple if else block
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == '1':
        ordinals = 'st'
    elif number == '2':
        ordinals = 'nd'
    elif number == '3':
        ordinals = 'rd'
    else:
        ordinals = 'th'

    
print(numbers + str(ordinals) + " place")






        

    
