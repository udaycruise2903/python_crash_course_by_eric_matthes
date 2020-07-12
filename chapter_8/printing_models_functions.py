# printing models using functions
def print_models(unprinted_designs, completed_models):
    """
    print each model from unprinted designs until none are left.
    move printed models to completed models.
    """

while unprinted_designs:
    current_design = unprinted_designs.pop()
    
    print("Printing model: " + current_design)
    completed_models.append(current_design)
    
def show_completed_models(completed_models):
    print("\n The Following models are printed: ")
    for completed_model in completed_models:
        print(completed_models)

unprinted_designs = ['line follower bot', 'doll', 'landscape mountains']
completed_models = []

# ~ print_models(unprinted_designs, completed_models)
# ~ show_completed_models(completed_models)
