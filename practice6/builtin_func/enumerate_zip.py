#enumerate
names=["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(index, name)


for index, name in enumerate(names, start=1):
    print(index, name)

numbers=[10,20,30]
for i , num in enumerate(numbers):
    print("Index:", i, "Value:", num)
#zip
names=["Alice", "Bob", "Charlie"]
scores=[90, 85, 95]
for name, score in zip(names, scores):
    print(name, score)

ages=[20,19,21]
for names, scores, ages in zip(name, scores, ages):
    print(name, scores, ages)


#converting zip to list
names = ["Alice", "Bob", "Charlie"]
scores = [90,85,95]
pairs = list(zip(names, scores))
print(pairs)


#using zip to create dictionary
student_scores=dict(zip(names, scores))
print(student_scores)

#unzip example
pairs=[("Alice", 90), ("Bob", 85), ("Charlie", 95)]
names2, scores2=zip(*pairs)
print("Names:", names2)
print("Scores:", scores2)