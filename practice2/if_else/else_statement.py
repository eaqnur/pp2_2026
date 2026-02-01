a=187
b=33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b is equal")
else:
    print("a is greater than b")

#else without elif
a=198
b=87
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#checking even or odd
num=7
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

#temperature classifier
temp=27
if temp>30:
    print("It's hot outside!")
elif temp>20:
    print("it's warm outside")
elif temp>10:
    print("It's cool outside")
else:
    print("It's cold outside!")

#else as fallback
username="Email"
if len(username)>0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty")