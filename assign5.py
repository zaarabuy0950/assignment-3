"""5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age."""


tuple = ('yubaraj','Ghimire', 26)
list = []
list.append(tuple)
print(list)
a = ('Anil','Shah',24)
b = ('labin','kadel',25)
list.extend([a,b])
print(list)
sortt = sorted(list)
print(sortt)
by_using_key_sort=sorted(sortt, key=lambda var:var[2])
print(by_using_key_sort)
