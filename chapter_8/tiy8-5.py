 # try it yourself 8-5 exercise
def describe_city(city, country = 'india'):
    """Display information about a city."""
    print( city.title() + " is in "+ country.title() + ".\n")

describe_city(city = 'chennai')
describe_city(city = 'Bengaluru')
describe_city(city = 'Mysuru') 
describe_city(country = 'South Korea', city = 'seoul')   

