# ~ with open('pi_digits.txt') as file_object:
    # ~ contents = file_object.read()
    # ~ print(contents.rstrip())

# ~ # using absolute file paths in open()
# ~ filepath = '/home/uday/workspace/python_work/chapter_10/pi_digits.txt'
# ~ with open(filepath) as file_object:
    # ~ contents = file_object.read()
    # ~ print(contents.rstrip())

# Using open() to read line by line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
