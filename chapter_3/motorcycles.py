#programmer:uday    date:02-apr-2020
#create a list
motorcycles='gixxer','starcity','ns200','ktmduke'
print(motorcycles)
 

#append an element in a list
motorcycles=[]
motorcycles.append('ducati')
motorcycles.append('enfield')
motorcycles.append('impulse')
print(motorcycles)

#change an element in a list
motorcycles[0]='yamaha'
print(motorcycles)

#insert items in a list
motorcycles.insert(1,'harley davidson')
motorcycles.insert(3,'hayabusa')
print(motorcycles)

#delete an item in a list
del motorcycles[0]
print(motorcycles)

#removing an item using pop method()
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#using pop method from any position
first_owned=motorcycles.pop(0)
print('The first motorcycle i owned was '+first_owned.title()+'.')

#removing an item using del method()
expensive='hayabusa'
motorcycles.remove(expensive)
print(motorcycles)
print('\nA '+expensive.title()+' is too expensive for me'+'.')

