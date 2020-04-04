#17.Write a python program to print factorial of a num received as a user input.
num=int(input("Enter the number "))
fact=1
total=0
for i in range(0,num,1):
    total=fact*num
    fact=total
    num-=1
print("Factorial:",fact)
