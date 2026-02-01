i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#print odd
i=1
while i<=10:
  if i%2==0:
    i+=1
    continue
  print(i)
  i+=1

#  Skip negative numbers from a list
numbers = [3, -1, 5, -2, 4]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1

num = 1
while num <= 10:
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1



