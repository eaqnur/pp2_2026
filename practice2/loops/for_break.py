fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
for i in range(1, 10):
    print(i)
    if i == 5:
        break

numbers = [1, 3, 5, 6, 7]
for n in numbers:
    if n % 2 == 0:
        print("First even number:", n)
        break

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

words = ["hello", "world", "stop", "python"]
for w in words:
    if w == "stop":
        print("Stop word found!")
        break
    print(w)

