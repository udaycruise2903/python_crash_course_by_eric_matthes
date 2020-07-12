# Making an agrument optional
def get_formatted_name(first_name, last_name, middle_name = ''):
    """ Return a neatly formatted name."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' '+ last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
name = get_formatted_name('apj', 'abdul', 'kalam')
print(name)
