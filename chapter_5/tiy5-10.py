#checking usernames
current_users = ['gita' , 'mrunalini', 'aparna', 'sampath', 'siva']

new_users = ['Govind', 'vaishnavi', 'keertan','gita', 'siva']


for new_user in new_users:
    if new_user in current_users:
        print(new_user + " - please enter a new username.")
    else:
        print(new_user + " is available.")
        
