class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
class battery():
    """An attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=90):
        """Initialise the battery attributes."""
        self.battery_size = battery_size
        
    def describe_battery_size(self):
        """Print a statement about the battery of the car."""
        print("This car has a" + str(self.battery_size) + "-kWh battery.")
        
class ElectricCar(Car):
    """Represent the aspects of a car, specific to electric vehicles.
    Then initialise attributes specific to electric car.
    """
    
    def __init__(self, make,model,year):
        """Initialise the values and attributes of parent class."""
        super().__init__(make, model, year)
        # ~ self.battery_size = 70
        self.battery = battery()
        
    # ~ def describe_battery(self):
        # ~ """Print a statement regarding battery."""
        # ~ print("The Car battery's capacity is " + str(self.battery_size) 
        # ~ + "-kWh.")
    
    # ~ def fill_gas_tank(self):
        # ~ """This car does not need a gas tank."""
        # ~ print("This car doesn't have a gas tank.")
        
my_tesla = ElectricCar("Tesla", "Model S", 2016)
print(my_tesla.get_descriptive_name())

# ~ my_tesla.describe_battery()

my_tesla.battery.describe_battery()

# ~ my_tesla.fill_gas_tank()
