#A lambda function is a small anonymous function.
x=lambda a:a+10
print(x(5))

#multiply argument a with b
x=lambda a,b:a*b
print(x(5,6))

#summarize
x=lambda a,b,c:a+b+c
print(x(5,6,2))

def myfunc(n):
    return lambda a:a*n
double=myfunc(2)
print(double(11))

def my_func(n):
    return lambda a:a*n
triple=my_func(3)
print(triple(11))

def myfunc(n):
    return lambda a:a*n
x2=myfunc(2)
x3=myfunc(3)
print(x2(11))
print(x3(11))