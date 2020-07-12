student = {'name': 'uday', 'age':19, 'courses': ['math', 'python']}
 
#print(student.get('phone', 'Not Found'))

student.update({'name': 'Jane', 'age': 18 })

print(student.keys())
print(len(student))
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)
