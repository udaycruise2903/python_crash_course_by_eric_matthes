# Using arbitrary keyword arguments.
def build_profile(first, last, **user_info):
    """build a dictionary about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('APJ Abdul', 'Kalam', 
                location= 'India', field = 'Defense')
print(user_profile)
