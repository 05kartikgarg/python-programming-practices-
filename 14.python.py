#14.Write a python program to find a given year is leap or not.
year=int(input("Enter the year:"))
if year%4==0 and year%100==0 and year%400==0:
    print("Leap Year")
else:
    print("Not Leap Year")
