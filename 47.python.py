#47.Write a python function to generate a table of any number entered by user.
def table(num):
    for i in range(1,11,1):
        print(num ,"*", i,"=",num*i )
    
num=int(input("Enter the number "))
table(num)
