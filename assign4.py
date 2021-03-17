#4. Create a list. Append the names of your colleagues and friends to it.
#Has the id of the list changed? Sort the list. What is the first item onthe list?
# What is the second item on the list?

list = []
print(id(list))
list.append('zanda')
list.append('yabin')
list.append('kendra')
print(list)
print(id(list))
print(f"Id list before:{id(list)}  and list id after:{id(list)} are same")
a = sorted(list)
print(a)
print(f"first item: {a[0]}")
print(f"second item: {a[1]}")


