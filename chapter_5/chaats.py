# ~ requested_chaats = ['samosa','kachori','jalebi','bonda']

# ~ for requested_chaat in requested_chaats:
    # ~ print("preparing your "+requested_chaat+".")

# ~ print("Finished preparing your chaat")

# ~ #another example
# ~ requested_chaat = 'gobi manchuri'
# ~ requested_chaats = ['gobi manchuri', 'samosa', 'kachori']
# ~ for requested_chaat in requested_chaats:
    # ~ if requested_chaat == 'gobi manchuri':
        # ~ print("sorry, we are out of gobi manchuri now.")
    
    # ~ else:
        # ~ print("Adding " + requested_chaat + ".")

# ~ print("\nFinished making your chaat!")

#checking empty list
# ~ requested_chaats = []

# ~ if requested_chaats:
    # ~ for requested_chaat in requested_chaats:
        # ~ print("Preparing your "+requested_chaat+".")
    # ~ print("Finished making your chaat.")
# ~ else:
    # ~ print("Are you sure you want a plain chaat")
    
#checking through multiple lists
available_chaats = ['samosa', 'kachori', 'gobi manchuri', 'pani puri', 'masala puri', 'sev puri']
requested_chaats = ['bel puri', 'samosa']

for requested_chaat in requested_chaats:
    if requested_chaat in available_chaats:
        print("preparing your "+ requested_chaat + ".")
    else:
        print("Sorry, we don't have " + requested_chaat + ".")
        
print("finished preparing your chaat")
        
    


        
    
