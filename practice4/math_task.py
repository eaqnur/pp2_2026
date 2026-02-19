#max/min functions
x=min(5,10,25)
y=max(5,10,25)
print(x)
print(y) 

#abs function
x=abs(-7.25)
print(x)

#pow func
x=pow(4,3)
print(x)

#The math.sqrt() method for example, returns the square root of a number:
import math
print(math.sqrt(64))

x=math.ceil(1.4)
y=math.floor(1.4)
print(x)
print(y)

#math.pi
ix=math.pi
print(ix)

#random
import random
print(random.random())
print(random.randint(1,10))
print(random.choice([1,2,3]))
lst=[1,2,3,4]
random.shuffle(lst)
print(lst)


#exercises
#1Write a Python program to convert degree to radian.
import math
degree=float(input())
ra=degree*math.pi/180
print(f"{ra:.6f}".format(ra))


#2 Write a Python program to calculate the area of a trapezoid.

h=float(input())
b1=float(input())
b2=float(input())

area=(b1+b2)*h/2
print("Area:", area)

#3Write a Python program to calculate the area of regular polygon.
import math
n=int(input())
s=float(input())
area=(n*s**2)/(4*math.tan(math.pi/n))
print("The area:", area)

#4Write a Python program to calculate the area of a parallelogram.
base=float(input())
height=float(input())
area=base*height
print(area)