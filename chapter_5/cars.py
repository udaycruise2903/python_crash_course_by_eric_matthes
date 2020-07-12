#if else statement
cars=['bmw','audi','porsche','lexus']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#checking whether a value is not in the list
banned_users=['jeevan','karan','kabali']

user='uday'

if user not in banned_users:
    print(user.title()+", You can post anything as you wish.")
    
