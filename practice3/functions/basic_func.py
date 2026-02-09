def my_func():
    print("Hello from a function")

my_func()

#call the same func multiple time
my_func()
my_func()
my_func()

'''
valid function names:
calculate_sum()
_private_func()
myfuncion2()
'''
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(68))
print(fahrenheit_to_celsius(92))

#return values
def get_greeting():
    return "HELLO"

message=get_greeting()
print(message)

#if a function doesn't have a return statement, it returns NONE by default

def my_function():
    pass

