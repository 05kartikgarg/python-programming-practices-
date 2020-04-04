#3.Write a python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class Rectangle:
    def compute_area(self):
        length=int(input("Enter the length of the rectangle\n"))
        width=int(input("Enter the width of the rectangle\n"))
        return length*width


obj=Rectangle()
area=obj.compute_area()
print("Area of the Rectangle is: ",area)        
        
    
    
