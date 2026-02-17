
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
