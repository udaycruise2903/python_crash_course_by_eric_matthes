# ~ # 7-3 try it yourself exercise
# ~ prompt = ("Please order the snacks you need: ")
# ~ prompt += "\n (press 'quit' to end the program)"

# ~ while True:
    # ~ snacks = input(prompt)

    # ~ if snacks == 'quit':
        # ~ break
    
    # ~ else:
        # ~ print("\n I would like to have " + snacks + ".")

# 7-4 Try it yourself exercise
age = ("Please enter your age for movie tickets: ")
age += int("\n (press 'quit' to end the program)")


active = True
while active:
    tickets = input(age)
    
    if tickets == 'quit':
        active = False
        
    elif age < 3:
            price = 0
    
    elif age <=12:
            price = 10
    
    elif age > 12:
            price = 15
    
    else:
        print("\n The cost of your movie tickets are $" + str(price) + "." )
    
    
