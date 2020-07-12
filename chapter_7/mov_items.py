# start with the users that need to be verified
# an empty list to hold confirmed users

unconfirmed_users = ['sagar', 'mahesh', 'vinay', 'rohith']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("\n Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
    print("\n The following users have bee confirmed: ")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
