#51.Write a python function to sum all the numbers in a list.
def sum_all(list):
    total=0
    for i in list:
        total+=i
    print("Sum of all the list elements is:",total)

list=[1,2,3,4,5,6,7,8,9,10]
sum_all(list)
