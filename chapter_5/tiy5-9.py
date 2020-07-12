    
# remove items from the lists
users = ['sagar', 'mahesh', 'ganesh', 'satya']

del users[2:]



user = 'sampath'

if user in users:
    print("Welcome")
else:
    print("We need some users")
print("*****")
    
# checking empty list
users = []

if user in users:
    for user in users:
        print("Welcome "+ user +".")
    print(" you have some notifications.")
else:
    print("We need some users")
