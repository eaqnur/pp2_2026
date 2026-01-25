#Built-in Data Types

'''
Text typ:str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''







x=5
y="Aho"
print(type(x))
print(type(y))

a="John"
a='John'
#is th same as

a=6
A="Mira"
#A will not overwrite a

x=10
y=5.99
z="Python"
a=True
print(type(x))
print(type(y))
print(type(z))
print(type(a))

x=1j #complex
print(type(x))

#list
list=['apple', 'orange', 'cherry', 'ananas']
print(type(list))

#tuple
x=('apple', 'orange', 'cherry', 'ananas')
print(type(x))

x=range(7) #range
print(type(x))

#dict
x = {"name" : "Aho", "age" : 18}
print(type(x))

#set
x = {"apple", "banana", "cherry"}


#casting
a=int(3.6)
b=float(9)
c=str(100)
print(a,b,c)

#convert from one type to another
x=2
y=3.14
z=1j

#convert from int to float
a=float(x)

#convert from float to int
b=int(y)

#convert from int to complex
c=complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#You cannot convert complex numbers into another number type.

#randooom
import random
print(random.randrange(1,10))