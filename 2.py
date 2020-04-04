#2.Write a python class which has two methods get string and print string.get string accept a string from the user and print string print the string in UPPERCASE.
class String:
    def get_string(self):
        string=input("Enter the string\n")
        return string
    def print_string(self,strr):
        print(strr.upper())

obj=String()
strr=obj.get_string()
obj.print_string(strr)
        
