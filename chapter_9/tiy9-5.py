# try it yourself 9-5 exercise
class User():
    """An attempt to model greetings to Users."""
    
    def __init__(self, first_name, last_name, login_attempts):
        """Initialise first_name and last_name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        """Simulating a personalised greeting in response to a command."""
        print(first_name.title() + " " + last_name.title() + ".")
    
    def read_login_attempts(self):
        """Print a statement on the number of login attempts."""
        print("\n The number of login attempts are: " 
        + str(self.login_attempts) + ".")
    
    def increment_login_attempts(self):
        """
        Increment the attribute by 1 after login attempt.
        """
        self.login_attempts = self.login_attempts + 1
        print("\n The NUmber of login attempts = " + str(self.login_attempts)
        + ".")
    
    def reset_login_attempts(self):
        """Reset the login attempts to 0"""
        self.login_attempts = 0
        print("\n The Number of login attempts = " + str(self.login_attempts)
        + ".")
        
# Make an instance from a class.
my_user = User("uday", "kiran",0)

print("My name is " + my_user.first_name.title() +
    " " + my_user.last_name.title() + ".") 

my_user.read_login_attempts()

# Calling increment_login_attempts method to increment login attempts by 1.
my_user.increment_login_attempts()

# Calling reset_login_attempts method to reset login attempts to 0. 
my_user.reset_login_attempts()
