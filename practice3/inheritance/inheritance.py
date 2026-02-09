class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass
#Use the pass keyword when you do not want to add any other properties or methods to the class.

x=Student("Mike", "Olsen")
x.printname()

#add the __init
#the __init__()function is called automatically every time the class is being used to create a new object.
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x=Student("Mike", "Olsen")
x.printname()
