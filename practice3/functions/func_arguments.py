def name(fname):
    print(fname+" Refsnes")
name("Email")
name("Tobias")
name("Linus")


def my_func(name): #name is a parameter
    print("Hello", name)

my_func("Emil")#"Emil" is an argument

def fullname(fname, lname):
    print(fname+" "+lname)

fullname("Jimin", "Park")

#default parameter values
#If the func is called without an argument, it uses the default value
def func(name="friend"):
    print("Hello", name)

func("AHOO")
func()

def country(country="Kazakhstan"):
    print("I am from", country)
country("Sweden")
country()


#keywords arguments
def my_pet(animal, name):
    print("I have a", animal)
    print("My", animal+"'s name is", name)

my_pet(animal="cat", name="Kitty")

#positional arguments
#pos arguments must be in the correct order
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

#mixing pos and keyword arguments
def pet(animal, name,age):
    print("I have a", age, "year old", animal, "named", name)

pet("dog", age=5, name="Buddy")

#passing different data types
#sending a list as an argument
def my_func(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits=["apple", "cherry", "strawberry"]
my_func(my_fruits)

#sending a dictionary as an argument
def people(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

person={"name":"Emil", "age":25}
people(person)


#return values
def add(x, y):
    return x+y
result=add(4,8)
print(result)

#a func that returns a list
def list():
    return ["apple", "banana","cherry"]
fruits=list()
print(fruits[0])
print(fruits[1])

#a func that returns a tuple
def tuple():
    return (10,20)
x,y=tuple()
print(x)
print(y)

#positional-only arguments
#to specify positional-only arguments, add, / after arg
def my_func(name, /):
    print("Hello", name)
my_func("AHo")

#keyword-only arguments
#to specify that a func can have only keyword arguments, add *, before arg
def my_func(*, name):
    print("Hello", name)
my_func(name="MAsha")

#combining positional-keyword-on;y arg
def my_func(a,b,/,*,c,d):
    return a+b+c+d
result=my_func(5,10,c=15,d=20)
print(result)