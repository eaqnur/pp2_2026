fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#print only odd num
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#Skip negative num in a list
numbers = [3, -1, 5, -2, 4]
for n in numbers:
    if n < 0:
        continue
    print(n)

#Print numbers from 1 to 10, skip 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#pass statement
for x in [0,1,2]:
   pass