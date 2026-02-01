#false values

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))



# functions can return a boolean
def myfunc():
    return True
print(myfunc())

if myfunc():
    print("YES!")
else:
    print("NO!")


x = 120
print(isinstance(x, int))