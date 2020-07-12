prompt = "\n Tell me the name of the cities you have visited: "
prompt += "\n (Press 'quit' to end the program.) "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    
    else:
        print("\n I would like to visit " + city.title() + ".")
