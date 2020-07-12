# ~ responses = {}

# ~ polling_active = True

# ~ while polling_active:
    # ~ name = input("\n What's your name? ")
    # ~ response = input("\n which country do you like to visit to? ")
    
# ~ responses[name] = response

# ~ repeat = input("\n Would you like another person to respond? (yes/no) ")
# ~ if repeat == 'no':
    # ~ polling_active = False
    
# ~ print("\n *** Poll results *** \n")

# ~ for name, response in responses.items():
    # ~ print(name + " would like to visit " + reponse + ".")
    
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
# Prompt for the person's name and response.

    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

# Store the response in the dictionary:
responses[name] = response
# Find out if anyone else is going to take the poll.
repeat = input("Would you like to let another person respond? (yes/ no) ")
if repeat == 'no':
    polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
