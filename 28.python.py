#28.Write a python program to add an item in a tuple.
t=(1,2,3,4.4,5.5,'a','b','c','abc','xyz')
l=list(t)
l.append(10)
t=tuple(l)
print(t)
