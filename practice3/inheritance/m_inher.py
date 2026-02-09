class A:
    def hello(self):
        print("Hello from A")

class B:
    def hi(self):
        print("Hi from B")
    
class C(A, B):
    pass

c=C()
c.hello()
c.hi()


class Person:
    def speak(self):
        print("I can speak")

class Worker:
    def work(self):
        print("I can work")
    
class Programmer(Person, Worker):
    def code(self):
        print("I write code")

p=Programmer()
p.speak()
p.work()
p.code()


class Camera:
    def take_photo(self):
        print("Photo taken")

class Phone:
    def call(self):
        print("Calling ...")

class Smartphone(Camera, Phone):
    pass
s=Smartphone()
s.take_photo()
s.call()

class A:
    def show(self):
        print("A")
class B:
    def show(self):
        print("B")
class C(A,B):
    def show(self):
        super().show()

c=C()
c.show()