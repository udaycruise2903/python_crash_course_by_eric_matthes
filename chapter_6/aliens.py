
#programmer:uday  date: 10-apr-2020
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print("\n\n")

#accessing values in a dictionary
alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("You just earned "+ str(new_points) + " points!")
print("\n\n")


#accessing key value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("\n\n")

#starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
print("\n\n")

#modifying value in a dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'color': 'yellow'}
print("The alien is " + alien_0['color'] + ".")
print("\n\n")

#incrementing values in dictionary
alien_0 = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('original x-postion: '+ str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:  
    x_increment = 3
    
alien_0['x_position'] = alien_0['x_position'] + x_increment
print( "new x-position: " + str(alien_0['x_position']))
print("\n\n")

 
