# try it yourself 8-13
# Using arbitrary keyword arguments.
def build_profile(first, last, **user_info):
    """build a dictionary about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Uday', 'Kiran', 
                Hobbies = 'Volunteering', 
                Interests = 'A.I',
                Sports = 'football')
print(user_profile)
