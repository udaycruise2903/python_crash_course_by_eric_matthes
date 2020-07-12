#store information about a person in a dictionary
persons = {
    'first name': 'uday', 
    'last name': 'kiran', 
    'age': '19', 
    'city': 'bengaluru'
    }
    
for name, person in persons.items():
    print( name.title() + " : " + person.title())
print("\t\t *****")

#favourite numbers of five people
fav_numbers = {
    'Darshan': '3', 
    'sahil': '54', 
    'vignesh': '2', 
    'vinod': '7', 
    'vishruth': '10'
    }
    
for name, fav_number in fav_numbers.items():
    print( name.title() + " : " + fav_number.title())
print("\t\t *****")

#glossary using dictionary
glossary_lists = {
    'string': "a set of characters", 
    'tuples': "A list that cannot be modified", 
    'list': "store values", 
    'variable': "stores a data value",
    }

for name, glossary_list in glossary_lists.items():
    print( name.title() + " : " + glossary_list.title())
