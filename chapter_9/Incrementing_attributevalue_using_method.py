# The Car Class
class Car():
    """Initialise an attempt to model a car."""
    
    def __init__(self, make, model, year):
        """Initialise make, model and year attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = self.make + " " + self.model + " " + self.year + "."
        return long_name
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

# Modifying an attribute value through a method called update_odometer()
    def update_odometer(self, mileage):
        """
        Set the odometer value to the given values.
        Reject the change if the odometer is rolled back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rollback an odometer.")    
        
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
            
my_new_car = Car("Audi", "R4", "2010")
print(my_new_car.get_descriptive_name())
 
my_new_car.update_odometer(1230)
my_new_car.read_odometer()

my_new_car.increment_odometer(150)
my_new_car.read_odometer()
