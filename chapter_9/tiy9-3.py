# try it yourself 9-3 exercise
class User():
    """An attempt to model greetings to Users."""
    
    def __init__(self, first_name, last_name):
        """Initialise first_name and last_name attributes."""
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        """Simulating a personalised greeting in response to a command."""
        print(first_name.title() + " " + last_name.title() + ".")

# Make an instance from a class.
my_user = User("uday", "kiran")

print("My name is " + my_user.first_name.title() +
    " " + my_user.last_name.title() + ".") 
