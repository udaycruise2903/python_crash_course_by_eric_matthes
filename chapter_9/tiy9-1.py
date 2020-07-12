 # try it yourself exercise 9-4
class  Restaurant():
    """An attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialise restaurant name and cusine type in response to command.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Print the statement in response to the command."""
        print("\n" + restaurant_name.title() 
        + " is the name of the restaurant.")
        print("\n" + cuisine_type.title() + 
        " is the name of the cuisine.")

    def open_restaurant(self):
        """Simulate that restaurant is open in respose to a command."""
        print(restaurant_name.title() + " is open.")

# Making an instance from a class.
my_restaurant = Restaurant("adigas", "south indian")

print("The Restaurant name is " + my_restaurant.restaurant_name.title() + ".")
print("The cuisine type is " + my_restaurant.cuisine_type.title() + ".")

