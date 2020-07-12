def greet_users(names):
    """Greet users using a for loop."""
    for name in names:
        msg = "Hello, "+ name.title() + "!"
        print(msg)
    
usernames = ['suresh', 'ramesh', 'rakesh']
greet_users(usernames)
