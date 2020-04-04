#18.Write a python program to find fibonacci series upto n terms.
num=int(input("Enter the number "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(0,num,1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
