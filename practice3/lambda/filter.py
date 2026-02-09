num=[1,2,3,4,5,6,7,8]
odd_num=list(filter(lambda x:x%2!=0, num))
print(odd_num)

#even num
l=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0, l))
print(even)

#pos num
l=[-5, 3,-9,8,-7,-5,-3,2]
pos=list(filter(lambda x:x>0, l))
print(pos)

data = [1, "hi", 3, "python", 7, "code"]

result = list(filter(lambda x: isinstance(x, str), data))
print(result)


#palindrom
words=["level", "qazaq", "radar", "dog", "cat"]
res=list(filter(lambda w:w==w[::-1], words))
print(res)