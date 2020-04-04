#45.Write a python function to find fibonacci series upto to n terms.
def fibonacci(num,a,b):
    for i in range(0,num,1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

num=int(input("Enter the number "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
fibonacci(num,a,b)

    
