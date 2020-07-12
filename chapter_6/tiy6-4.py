# try it yourself 6-1
# glossary using dictionary
glossary_lists = {
    'string': "a set of characters", 
    'tuples': "A list that cannot be modified", 
    'list': "store values", 
    'variable': "stores a data value",
    'string': "a set of characters", 
    'tuples': "A list that cannot be modified", 
    'list': "store values", 
    'variable': "stores a data value",
    }

for name, glossary_list in glossary_lists.items():
    print( name.title() + " : " + glossary_list.title())
print("\n\t\t *****\n")

#try it yourself 6-5
rivers = {'Ganga' : 'India',
    'Thames' : 'England',
    'Yangtze' : 'China',
    'Amur' : 'Russia'
    }

for name, river in rivers.items():
    print( name.title() + " : " + river.title())
print("\n\t\t *****\n")



    
    
    
