# try it yourself exercise 9-4
class  Restaurant():
    """An attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialise restaurant name and cusine type in response to command.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Print the statement in response to the command."""
        print("\n" + restaurant_name.title() 
        + " is the name of the restaurant.")
        print("\n" + cuisine_type.title() + 
        " is the name of the cuisine.")

    def open_restaurant(self):
        """Simulate that restaurant is open in respose to a command."""
        print(restaurant_name.title() + " is open.")

    def set_number_served(self):
        """print a statement in response to the command."""
        print("\n The number of customers that have been served: " 
        + str(self.number_served)  + ".")
        
    def update_number_served(self, more_people):
            if more_people >= self.number_served:
                self.number_served = more_people
            else:
                print("\n You cannot reduce the count.")
    
    def increment_number_served(self, more_people):
        """print the incremented value of customers served."""        
        self.number_served += more_people
        
# Making an instance from a class.
my_restaurant = Restaurant("adigas", "south indian")

print("The Restaurant name is " + my_restaurant.restaurant_name.title() + ".")
print("The cuisine type is " + my_restaurant.cuisine_type.title() + ".")
my_restaurant.set_number_served()

# MOdifying an attribute's value directly
my_restaurant.number_served = 4
my_restaurant.set_number_served()

my_restaurant.update_number_served(10)
my_restaurant.set_number_served()

my_restaurant.increment_number_served=20
my_restaurant.set_number_served()
