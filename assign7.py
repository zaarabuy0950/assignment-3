"""7. Create a list of tuples of first name, last name, and age for your friends
and colleagues. If you don't know the age, put in None. Calculate the
average age, skipping over any None values. Print out each name,
followed by old or young if they are above or below the average age"""


friend_list=[('Yuvi','Ghimire',26), ('Anil', 'Shah', 24), ('Labin', 'Kadel', 25)]
age =[]
for i in range(len(friend_list)):
    age.append(friend_list[i][2])
print(age)
avg = sum(age)/len(age)
print(f"The average age is:{avg}")

for i in range(len(friend_list)):
    if friend_list[i][2] > avg:
        print(friend_list[i][0] + " is above the average age(seems old)")
    else:
        print(friend_list[i][0] + " is below the average age(young)")

