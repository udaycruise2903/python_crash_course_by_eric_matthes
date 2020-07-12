#if elif else 
age=90

if age < 4:
    print("Your admission cost is 0$.")
elif age < 18: 
    print("Your admission cost is 5$.")
else:
    print("Your admission cost is 10$.")

#updated billing code.
age = 12
 
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission price is $"+str(price)+".")

#updated billing code with elif
age = 67
 
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 8 

print("Your admission price is $"+str(price)+".")
