#one_line if statement:
a=5
b=2
if a>b: print("a is greater than b")

#one_line if/else that prints a value:
a=2
b=356
print("A") if a>b else print("B")

a=10
b=20
bigger=a if a>b else b
print("Bigger is", bigger)

#multiple conditions on one line
a=330
b=330
print("A") if a>b else print("=") if a==b else print("B")

#max
x=15
y=20
max=x if x>y else y
print("Maximum value:", max)
