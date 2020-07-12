# try it yourself exercise 8-14
def make_car(name, series, **car_info):
    """Make a dictionarya about a car."""
    car = {}
    car['car_name'] = name
    car['car_series'] = series
    for key, value in car_info.items():
        car[key] = value
        return car
    
my_car = make_car('Audi','R8', airbags = 'Present')
print(my_car)
