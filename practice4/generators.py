
#return an iterator from a tuple, and print each value
mytuple=("apple", "banana", "cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr="banana"
myit=iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#looping through an iterator
mytuple=("apple", "banana", "cherry")
for x in mytuple:
    print(x)


#iterate the characters of a string
mystr="banana"
for x in mystr:
    print(x)


class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=mynumbers()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#stopiteration
class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
        
myclass=mynumbers()
myiter=iter(myclass)
for x in myiter:
    print(x)


#generators
def my_gen(n):
    for i in range(n):
        yield i*i
    
for x in my_gen(5):
    print(x)

squares=(x*x for x in range(5))
print(list(squares))


#exercises
#1 Create a generator that generates the squares of numbers up to some number N.
def square(n):
    for i in range(1, n+1):
        yield i*i
n=int(input())
for x in square(n):
    print(x)
    

#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
n=int(input())
res=[]
for x in even(n):
    res.append(str(x))

print(",".join(res))


#3Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n
def div(n):
    for i in range(0, n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
for x in div(n):
    print(x)
    

#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def square(a,b):
    for i in range(a, b+1):
        yield i*i

a=int(input())
b=int(input())
for x in square(a,b):
    print(x)
    

#5 Implement a generator that returns all numbers from (n) down to 0.
def cout(n):
    for i in range(n, -1, -1):
        yield i

n=int(input())
for x in cout(n):
    print(x)