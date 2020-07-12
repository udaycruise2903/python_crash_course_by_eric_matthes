# ~ # print preparing extras using functions.
# ~ def make_meals(*extras):
    # ~ """Print the sides that have been requested."""
    # ~ print(extras)

# ~ make_meals('South Indian Meals')
# ~ make_meals("Sambhar", "Curd", 'papad', 'keer')

# print meals with sides
def make_meals(*extras):
    """prepare meals with extras. """
    print("\n Preparing meals with following extras.")
    for extra in extras:
        print("-" + extra)
        
#make_meals("South Indian Meals")
#make_meals("curd", 'sambhar', 'papad', 'keer', 'pickle', 'salad')
