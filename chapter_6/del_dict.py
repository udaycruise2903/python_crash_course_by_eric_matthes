alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0 ['points']
print(alien_0)

#a dictionary of favourite objects
favourite_languages = {
    'ganesh' : 'java',
    'sagar' : 'c',
    'santhosh' : 'c++',
    'uday' : 'python+',
    }

print("Sagar's favourite language is " +
    favourite_languages['sagar'].title() +
    ".")
