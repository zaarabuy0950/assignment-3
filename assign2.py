#2.Write an if statement to determine whether a variable holding a year is a leap year.

year = int(input("Enter a Year:"))

if year %4 == 0 and year % 100 != 0 :
    print(year ," is Leap year")

elif year % 100 ==0:
    print(year, " is not a Leap year")

elif year % 400 == 0:
    print(year, " is Leap year")

else:
    print(year," is not a Leap Year")