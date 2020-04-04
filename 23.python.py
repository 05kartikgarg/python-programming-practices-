#23.Write a python program to multiplies all the items in a list
l=[1,2,3,4,5,6]
num=1
total=0
for i in l:
    total=num*i
    num=total
print(total)
