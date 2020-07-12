# ~ # Try it yourself 7-4
# ~ # Using an active variable to control how long the loop runs
# ~ # Enter chats and print a line that you are preparing the chat
# ~ prompt = "Press 'quit' to end the program "
# ~ prompt += "Enter the chat you require: "

# ~ message = "" 
# ~ while message != 'quit':
    # ~ message = input(prompt)
    # ~ print(message)
# ~ print('\n\t\t ******************')
    
# Use a conditional in the while statement to stop the loop
prompt = "Press 'quit' to end the program "
prompt += "Enter the chat you require: "
        
while True:
    message = input(prompt)
    
    if message == 'quit':
        break
    else:
        print(message)
