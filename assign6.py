"""6. Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it."""


friends_list = ['yuvi', 'anil', 'labin', 'kendra', 'krishna']
friend_name = input("enter a friend name:")
found = False
for i in friends_list:
    if i.casefold() == friend_name.casefold():
        print("found")
        found = True
        break

if not found:
    print(" not found")

