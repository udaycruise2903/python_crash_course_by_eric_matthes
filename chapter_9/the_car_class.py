# The Car Class
class Car():
    """Initialise an attempt to model a car."""
    
    def __init__(self, make, model, year):
        """Initialise make, model and year attributes."""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = self.make + " " + self.model + " " + self.year + "."
        return long_name
    
my_car = Car("Audi", "R4", "2010")
print(my_car.get_descriptive_name())
