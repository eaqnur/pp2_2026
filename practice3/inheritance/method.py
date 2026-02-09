#add methods
class Person():
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear=year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x=Student("Mike", "Olsen", 2024)
x.welcome()


class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c=Cat()
c.speak()

#super+overriding
class Employee:
    def get_salary(self):
        return 1000

class Manager(Employee):
    def get_salary(self):
        base=super().get_salary()
        return base+500
    
m=Manager()
print(m.get_salary())

class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, a):
        self.a=a
    
    def area(self):
        return self.a*self.a
    
class Rectangle(Shape):
    def __init__(self, w,h):
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
    
s=Square(5)
r=Rectangle(4,3)
print(s.area())
print(r.area())