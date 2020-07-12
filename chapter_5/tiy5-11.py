# ordinal numbers
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers = str(numbers)

for number in numbers:
    if number == 1:
        ordinals = 'st'

    elif number == 2:
        ordinals = 'nd'
    elif number == 3:
        ordinals = 'rd'
    else:
        ordinals = 'th'

for number in numbers:
    print(number + ordinals)






        

    
