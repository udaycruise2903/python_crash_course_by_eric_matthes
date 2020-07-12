# Try it yourself exercise 8-9 
def show_magicians(magician_names, great_magicians):
    """
    print each magician name from magicianss until none are left.
    move appended magicians to great magicians.
    """

while magician_names:
    current_magician = magician_names.append("The Great")
    
    print("Printing magician: " + current_magician)
    great_magicians.append(current_magician)
    
def make_great(great_magicians):
    print("\n The Following magicians are great: ")
    for great_magician in great_magicians:
        print(great_magicians)

magician_names = ['line follower bot', 'doll', 'landscape mountains']
great_magicians = []

show_magicians(magician_names, great_magicians)
make_great(great_magicians)

