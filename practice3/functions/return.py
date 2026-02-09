def myfunc():
    x=300
    print(x)

myfunc()

#func inside func
def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

#global scope
x=300
def myfunc():
    print(x)
myfunc()
print(x)

#naming variables
x=300
def my_func():
    x=200
    print(x)
my_func()
print(x)

#global keyword
def myfunc():
    global x
    x=400

myfunc()
print(x)

#nonlocal keyword
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

