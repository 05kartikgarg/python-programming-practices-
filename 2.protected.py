#Python program to create protected variables and methods of a class
class Person:
  def __init__(self, firstName, lastName):
    self._firstName = firstName
    self._lastName = lastName
 
  def _display(self):
    print('My name is ', self._firstName, self._lastName)
 
p = Person("Harshit", "Gupta")
print('First name: ', p._firstName)
print('Last name: ', p._lastName)
p._display()
