# Try it yourself 6-6
# looping through a dictionary 's keys in a order
fav_players = {
    'sagar' : 'ms dhoni',
    'sahil' : 'sachin',
    'likith' : 'ad de viliers',
    'uday' : 'chris gayle',
    }

friends = ['sagar', 'uday']
for name in fav_players.keys():
    print(name.title())

    if name in friends:
        print(" Hi, " + name.title() + ". your favourite player is " + 
        fav_players[name].title() + "!")
    else:
        print(name.title() + ", Please take the poll.")
         

