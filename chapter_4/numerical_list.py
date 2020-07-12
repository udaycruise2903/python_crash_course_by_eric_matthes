#use range function to print numbers
for value in range(1,3):
	print(value)
	
#use list and range to print numbers
numbers=list(range(1,3))
print(numbers)

#use list and range to print even numbers
even_numbers=list(range(2,11,2))
print(even_numbers)

#print odd numbers
odd_numbers=list(range(1,11,2))
print(odd_numbers)

#print square numbers
squares=[]
for value in range(1,3):
	square=value**2
	squares.append(square)
	
print(squares)
print(len(squares))
print('\n\n')
#print(sum(squares))
