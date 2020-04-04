#50.Write a python function to check whether input number is even or odd.
def even_odd(num):
    if num%2==0:
        print("EVEN")
    else:
        print("ODD")

num=int(input("Enter the number "))
even_odd(num)
