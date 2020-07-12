#programmer:udaydate:02-apr-2020
#exercise 3-1 to 3-6
#print a personalised message to people in list

guests=['adarsh','sushmitha','gautham']
message1='hello, '+guests[0].title()+'. I invite you to the dinner at my house.'
message2='hello, '+guests[1].title()+'. I invite you to the dinner at my house.'
message3='hello, '+guests[2].title()+'. I invite you to the dinner at my house.'
print(message1)
print(message2)
print(message3)

#using pop method to print that guest is not available

popped_guest=guests.pop(0)
print(popped_guest.title()+' cannot make it to the dinner tonight.\n')

print('i found a bigger dinner table.\n')
guests.insert(0,'guide')
guests.insert(2,'coach')
guests.append('good person')
 

message4='hello, '+guests[0].title()+'. I invite you to the dinner at my house.\n'
message5='hello, '+guests[1].title()+'. I invite you to the dinner at my house.\n'
message6='hello, '+guests[2].title()+'. I invite you to the dinner at my house.\n'
message7='hello, '+guests[3].title()+'. I invite you to the dinner at my house.\n'
message8='hello, '+guests[4].title()+'. I invite you to the dinner at my house.\n'
print(message4,message5,message6,message7,message8)

#using pop method to remove items from the list.
print( 'The Bigger Dinner table would not arrive at the scheduled time.So i can invite only two people to the dinner')
popped_guest2=guests.pop(0)
print(popped_guest2.title()+' , I am sorry that i cannot invite you to the dinner.\n')
popped_guest3=guests.pop(1)
print(popped_guest3.title()+' , I am sorry that i cannot invite you to the dinner.\n')
popped_guest4=guests.pop(2)
print(popped_guest4.title()+' , I am sorry that i cannot invite you to the dinner.\n')
guests.remove('sushmitha')
guests.remove('gautham')
print(guests)
