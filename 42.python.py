#42.Write a python program to sum all the items in a dictionary.
d={'a':10,'b':20,'c':30,'d':40,'e':50}
total=0
for i in d:
    total+=d[i]
print("Sum of all the items is: ",total)
