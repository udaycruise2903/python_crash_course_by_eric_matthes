#simpe if statement

alien_color = 'green'

if alien_color == 'green':
    points=5
    
print("you earned "+str(points)+" points.")

alien_color = 'red'

if alien_color == 'green':
    points=5
    
print("you earned "+str(points)+" points.")


#simple if else block
alien_color = 'red'

if alien_color == 'green':
    points = 5
else:
    points = 10
    
print("you earned "+str(points)+" points.")

#simple if else block
alien_color = 'red'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
    
print("you earned "+str(points)+" points.")



#simple if statements
fruits = ['bananas','grapes']

print('\n\n')
if 'strawberries' in fruits:
    print(" I really like straberries.")
if 'bananas' in fruits:
    print(" I really like bananas.")
if 'oranges' in fruits:
    print("I really like oranges.")
if 'grapes' in  fruits:
    print(" I really like grapes.")
if 'apples' in fruits:
    print(" I really like apples.")
