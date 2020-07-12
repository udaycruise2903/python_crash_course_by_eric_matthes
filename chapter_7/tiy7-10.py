responses = {}

polling_active = True

while polling_active:
    name = input("\nwhat's your name? ")
    response = input("\nwhich country you like to visit in the future: ")
    
    responses[name] = response
    repeat = input("Would you like another person to take the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
print("\t\t\n *** POLL RESULTS ***")
for name, response in responses.items():
    print(name + " would like to visit "+ response + ".")
    
