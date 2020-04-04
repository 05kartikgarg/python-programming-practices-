#1.Write a python class to reverse a string word by word.
class Reverse_word:
    def rev_strr(self):
        string=input("Enter the string seperated by space\n").split(" ")
        for i in string[-1::-1]:
            print(i,end=" ")
    


obj=Reverse_word()
obj.rev_strr()
