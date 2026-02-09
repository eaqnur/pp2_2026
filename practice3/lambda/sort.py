students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

num=[-10, 3,-1,7,-5]
res=sorted(num, key=lambda x:abs(x))
print(res)

data=[(1,5),(3,2),(4,1),(2,7)]
res=sorted(data, key=lambda x:x[1])
print(res)

scores = {"Ali": 80, "Aknur": 95, "Dana": 70}
result = sorted(scores.items(), key=lambda x: x[1])
print(result)