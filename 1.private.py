# program to illustrate private access modifier in a class 

class Geek:
    __name = None
    __roll = None
    __branch = None
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch
    def __displayDetails(self):
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)
    def accessPrivateFunction(self):
        self.__displayDetails()

		
obj = Geek("Harshit Gupta","0827CS181089", "Computer Science Engineering") 
obj.accessPrivateFunction() 
