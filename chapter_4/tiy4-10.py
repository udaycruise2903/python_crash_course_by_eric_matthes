#print the first three items using a list
chaats=['pani puri','samosa','bel puri','masala puri','gobi manchuri','kachori','sev puri','gobi rice']
print('\nThe first three items of the list are:')
for chaat in chaats[:3]:
	print(chaat.title())
	
#print the first three items using a list
print('\nThe three items from the middle of the list are:')
for chaat in chaats[3:6]:
	print(chaat.title())

#print the last three items using a list
print('\nThe last three items of the list are:')
for chaat in chaats[-1:4:-1]:
    print(chaat.title())


my_sweets=['laddoo','kaju katli','gulab jamun','jalebi']
friend_sweets=my_sweets[:]

#slicing,appending to lists using slicing
print("\nmy friend 's favourite sweets are:")
print(friend_sweets)

my_sweets.append('mysore pak')
friend_sweets.append('rasgulla')

print("\nMy favourite sweets are:")
for my_sweet in my_sweets:
	print(my_sweet)

print("\nMy Friend's favourite sweets are")
for friend_sweet in friend_sweets:
	print(friend_sweet)
