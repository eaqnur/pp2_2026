
numbers=[1,2,3,4,5]
double=list(map(lambda x:x*2, numbers))
print(double)

num=[2,4,6,8]
def double(x):
    return x*2
res=list(map(double, num))
print(res)

#square
num=[1,2,3,4]
res=list(map(lambda x:x**2, num))
print(res)

#convert str to int
num=["1","2","3","4","5"]
res=list(map(lambda x:int(x), num))
print(res)

#ger length to each word
words=["banana", "ananas", "apple"]
res=list(map(lambda w: len(w), words))
print(res)

#add 10 to every num
num=[5,7,4,9]
res=list(map(lambda x:x+10, num))
print(res)

#use with input
num=list(map(lambda x:int(x)*2, input().split()))
print(num)

#round
num=[1.2, 3.7, 4.7,9.3]
res=list(map(lambda x:round(x), num))
print(res)

#upper
words=["hello", "python", "ahpp"]
res=list(map(lambda w:w.upper(), words))
print(res)

#a*b
a=[1,4,7,8]
b=[11,7,4,9]
res=list(map(lambda x,y:x*y, a,b))
print(res)