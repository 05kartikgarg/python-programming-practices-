#46.Write a python function to find factorial of a number.
def factorial(num):
    fact=1
    total=0
    for i in range(0,5,1):
        total=fact*num
        fact=total
        num-=1
    print("Factorial of a number is:",fact)


num=5
factorial(num)
