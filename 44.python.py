#44.Write a python function to take list as argument and remove odd numbers from list.
def list_func(list):
    for i in list:
        if i%2!=0:
            list.remove(i)
    print(list)

list=[1,2,3,4,5,6,7,8,9,10]
list_func(list)
