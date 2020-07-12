# Programmer: Uday  Date : 12-apr-2020
# convert a numerical input which is a string to a number using string ()
height = input("how tall are you in inches?")
height = int(height)

if height >= 50:
    print("\n You are tall enough to ride!")
else:
    print("\n Come back when you are old enough to ride")
