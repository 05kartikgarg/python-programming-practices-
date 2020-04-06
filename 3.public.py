#Python program to create public variables and methods of a class
class Person:
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName
 
  def display(self):
    print('My name is ', self.firstName, self.lastName)
 
p = Person("Harshit", "Gupta")
print('First name: ', p.firstName)
print('Last name: ', p.lastName)
p.display()
