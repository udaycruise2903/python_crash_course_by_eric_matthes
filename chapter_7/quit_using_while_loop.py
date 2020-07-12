prompt = ("Enter anything to repeat again. ")
prompt += ("\n press 'quit' to end the program. ")

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
        
    else:
        print(message)
