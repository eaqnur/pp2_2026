#Using *args to accept any number of arguments
'''
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_func(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_func("Emil", "Tobias", "Linus")'''

def my_func(greeting, *names):
    for name in names:
        print(greeting, name)

my_func("Hello", "Emil", "Tobias", "Linus")

def my_func(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total
print(my_func(1,2,3))
print(my_func(10,20,30,40))
print(my_func(5))


#find max
def max(*numbers):
    if len(numbers)==0:
        return None
    max_num=numbers[0]
    for num in numbers:
        if num>max_num:
            max_num=num
    return max_num
print(max(3,7,2,9,1))

#Using **kwargs to accept any number of keyword arguments:

def my_func(**kid):
    print("His last name is "+kid["lname"])
my_func(fname="Tobias", lname="Refsnes")

def my_var(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:",myvar["age"])
    print("All dat:", myvar)
    my_var(name="Tobias", age=30, city="Bergen")

#using **kwargs with regular arguments
def my_func(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key+":", value)

my_func("emil123", age=25, city="Oslo", hobby="coding")

#combining *args and **kwargs
def combi(title, *args, **kwargs):
    print("Title:", title)
    print("Positional aeguments:", args)
    print("Keyword arguments:", kwargs)

combi("User Info", "Emil", "Tobias", age=25, city="Oslo")

#unpacking arguments
#unpacking lists with *
def unpack(a,b,c):
    return a+b+c

numbers=[1,2,3]
res=unpack(*numbers) #same as: unpack(1,2,3)
print(res)

#unpacking dictionaries with **
def my_func(fname, lname):
    print("Hello",fname, lname)
person={"fname":"Emil", "lname":"Refsnes"}
my_func(**person)

