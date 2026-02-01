
i=1
while True:
    print(i)
    if i==5:
        break
    i+=1

#2
while True:
    num=int(input())
    if num==0:
        break
    print("You entered: ", num)

#first divisor of a num
n=20
i=2
while i<=n:
    if n%i==0:
        print(i)
        break
    i+=1

#stop the loop 
num=[1,2,3,0]
i=0
while i<len(num):
    if num[i]==0:
        print("Zero found, stop")
        break
    i+=1

import random
while True:
    n=random.randint(1, 10)
    print(n)
    if n==5:
        print("Caught 5, stop")
        break
