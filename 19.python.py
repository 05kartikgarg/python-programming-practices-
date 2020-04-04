#19.Write a python program to generate prime number from 1 to 50.
for num in range(1,51):
    count=0
    for i in range(2,(num//2+1)):
        if (num%i==0):
            count+=1
            break
    if (count==0 and num!=1):
        print(num,end=" ")
    
