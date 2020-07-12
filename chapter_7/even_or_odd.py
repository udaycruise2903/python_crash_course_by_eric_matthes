# to determine whether an input number is even or odd
number = input("Enter a number to define whether it is odd or even ")
number = int(number)

if number %2 == 0:
    print("\n The number " + str(number) + " is even.")
else:
    print("\n The number " + str(number) + " is odd.")
