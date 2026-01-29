x=3 #x is of type int
y="Hello, World!" #y is of type str
z=3.14 #z is of type float

print(x)
print(y)
print(z)

a,b,c=7,6,5
print(a,b,c)

x="string"
print(x)

x=str(5)
y=int(9)
z=float(8)
print(x,y,z)


#legal veariable names:
myvar="Aho"
my_var="Aho"
_my_var="Aho"
myVar="Aho"
MYVAR="Aho"
myvar1="aho"

#illegal variable names:
'''
2myvar="Aho"
my-var="Aho"
my var="Aho"
'''

#multi words variable names

#camel case
myVariableName="Naz"

#pascal case
MyValiableName="Naz"

#snake case
my_variable_name="Naz"

x,y,z="Apple","Banan","Ananas"
print(x)
print(y)
print(z)

c=s=m="Strawberry"
print(c)
print(s)
print(m)

#unpack a list
fruit=['apple', 'banana', 'ananas']
x,y,z=fruit
print(x,y,z)

#global variables

x="easy to learn"

def myfunc():
    print("Python is" + x)

myfunc()

o="awesome"
def myfunc1():
    o="fantastic"
    print("Python is" + o)

myfunc1()
print("Python is"+o)

x = "awesome"

def myfunc2():
  global x
  x = "fantastic"

myfunc2()

print("Python is " + x)