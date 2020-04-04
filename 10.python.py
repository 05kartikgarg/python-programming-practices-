#10.Write a python program to find greatest among three numbers.
num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))
num3=int(input("Enter the third number "))
if num1>num2 and num1>num3:
    print("First number is Greater")
elif num2>num1 and num2>num3:
    print("Second number is Greater")
else:
    print("Third number is Greater")
