# Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up
# in finished_sandwiches.

chat_orders = ['sev puri','samosa', 'sev puri','kachori', 'masala puri', 'pani puri', 'sev puri', 'gobi manchuri']
finished_orders = []

while 'sev puri' in chat_orders:
    chat_orders.remove('sev puri')
print("\n Sorry, we are out of 'sev puri'.")

while chat_orders:
    current_order = chat_orders.pop()     
    print("Preparing order: " + current_order.title())
    finished_orders.append(current_order)

print("\n The folllowing orders have been prepared: ")
for finished_order in finished_orders:
    print(finished_order.title())
