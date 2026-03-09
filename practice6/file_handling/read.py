f=open("demofile.txt","r")
print(f.read())

#using the with statement
with open("demofile.txt") as f:
    print(f.read())

#close the file when you are finished with it
f=open("demofile.txt", "r")
print(f.readline())
f.close()

#read only parts of the file
with open("demofile.txt") as f:
    print(f.read(5))


#read one line of the file
with open("demofile.txt") as f:
    print(f.readline())

#read two lines of the file
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())


#loop through the file line by line
with open("demofile.txt") as f:
    for x in f:
        print(x)