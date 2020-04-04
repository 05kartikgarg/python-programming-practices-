#6.Write a python program to calculate factorial of a number
num=5
fact=1
total=0
for i in range(0,5,1):
    total=fact*num
    fact=total
    num-=1
print("Factorial of a number is:",fact)
