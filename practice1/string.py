#'hello' is the same as "hello".
print("Hello")
print('Hello')

a="Ahooo"
print(a)

a="Hello, World"
print(a[1])

#loop through a str
for x in "ananas":
    print(x)

a="Hello, Alem"
print(len(a))

#check str
text="The best things in life are free!"
print("best" in text)

text="The best things in life are free!"
if "life" in text:
    print("Yes, 'life' is present")


#check if not
text="The best things in life are free!"
print("cool" not in text)

text="The best things in life are free!"
if 'cool' not in text:
    print("'cool' is not present")