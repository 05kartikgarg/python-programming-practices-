#4.Write a python class named Circle constructed by a radius and two methods which will compute the area and perimeter of a circle.
class Circle:
    def compute_area(self,rad):
        return 3.14*rad*rad
    def compute_perimeter(self,rad):
        return 2*3.14*rad



rad=int(input("Enter the radius of the circle\n"))
obj=Circle()
area=obj.compute_area(rad)
print("Area of the Circle is: ",area)
perimeter=obj.compute_perimeter(rad)
print("Perimeter of the Circle is: ",perimeter)
        
        
        
