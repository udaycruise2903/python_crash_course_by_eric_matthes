def describe_pet(animal_type, pet_name):
    """Display the information about pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog', 'jimmy')
describe_pet('cat', 'chandni')
