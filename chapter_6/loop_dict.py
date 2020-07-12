#Looping through all key-value pairs
user_o = {
    'username': 'Leonardo',
    'first': 'Damon',
    'last':'Vinci',
    }
for key, value in user_o.items():
    print("\nKey: "+key)
    print("Value: "+value)
print("\n\n")
  
#looping through a dictionary 's keys in a order
favourite_foods = {
    'sagar' : 'puliogare',
    'sahil' : 'roti',
    'pilkith' : 'curd rice',
    'uday' : 'bisi bele bath',
    }

for name in sorted(favourite_foods.keys()):
    print(name.title() + ", thank you for taking the poll.")
    
print("\n\n")
 
#loopig through all the values in a dictionary
favourite_foods = {
    'sagar' : 'puliogare',
    'sahil' : 'roti',
    'pilkith' : 'curd rice',
    'uday' : 'bisi bele bath',
    }

print("The following foods have been mentioned")
for food in set(favourite_foods.values()):
        print(food.title())
