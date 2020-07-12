#programmer:uday    date:09-apr-2020
#if else statement
sweet='kaju katli'
if sweet == 'kaju katli':
    print(sweet.title()+" is a costly but a tasty sweet.")
else:
    print("not my favourite sweet")
    
#second conditional test
users=['ganesh','siri','mahesh','suresh','viresh']

new_user='Sahil'

if new_user.lower() in users:
    print("This user already exists.")
else:
    print("Welcome to the website.")

age= 21

if age >= 18:
    print("please enter your date of birth")
else:
    print("please comeback later")

profession = "working"
    
if age >= 18 and profession == 'student':
    print("enter your course:")
if age >= 18 and age <= 60 and profession == 'working':
    print("enter the your profession name")
    


