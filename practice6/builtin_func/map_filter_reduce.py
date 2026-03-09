#map
numbers=[1,2,3,4,5]
squares=list(map(lambda x: x**2, numbers))
print("Squares:", squares)

numbers=['1','2','3','4']
nums=list(map(int, numbers))
print("Converted to int:", nums)

words=['apple', 'banana', 'cherry']
len=list(map(len, words))
print("Word lengths:", len)


#filter
numbers=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0, numbers))
print("Even numbers:", even)

numbers=[2,4,6,8,9,3,7]
greater5=list(filter(lambda x:x>5, numbers))
print("Numbers>5:", greater5)

#reduce
from functools import reduce
numbers=[1,2,3,4]
sum=reduce(lambda x,y: x+y, numbers)
print("Sum:", sum)

numbers=[5,8,2,10,11]
max=reduce(lambda a,b: a if a>b else b, numbers)
print("Maximum:", max)

numbers=[4,5,7,9,2]
prod=reduce(lambda x,y: x*y, numbers)
print("Product:", prod)