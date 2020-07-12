loop = True
while loop:
    print("Please enter your age: ")
    age = input()
    
    if age == 'quit':
        break
    
    age = int(age)
    
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    elif age > 12:
        price = 15
    else:
        print("Input unrecognised")
        break

print('Your ticked price is $' + str(price) + '.')


