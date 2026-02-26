import re

#check if the string starts with "The" and ends with "Spain"

txt="The rain in Spain"
x=re.search("^The.*Spain$",txt)
if x:
    print("YES! We have a match!")
else:
    print("NO match")


#metacharacters

# [] -a set of characters
txt="The rain in Spain"
#find all lowercase chars alphabetically between "a" and "m"
x=re.findall("[a-m]", txt)
print(x)


# / -signals a special sequence 
txt='That will be 59 dollars'
#Find all digit characters
x=re.findall("\d", txt)
print(x)


# . -any character(except newline character)
text="hello planet"
#search for a sequence that starts with 'he',followed by two(any)characters, and an 'o'
x=re.findall("he..o",text)
print(x)

# ^ -starts with
txt="hello planet"
#check if the string starts with 'hello'
x=re.findall("^hello", txt)
if x:
    print("yes")
else:
    print("no match")



# $ -ends with
txt="hello planet"
#Check if the string ends with 'planet'
x=re.findall("planet$", txt)
if x:
    print("Yes")
else:
    print("no")



# * -zero or more occurrences
#search for a sequence that starts with 'he', followed by 0 or more (any) characters, and an 'o'
x=re.findall("he.*o",txt)
print(x)

# + -one or more occurrences
#search for a sequence that starts with 'he', followed by 1 or more(any) characters, and an 'o'
x=re.findall("he.+o", txt)
print(x)


# ? -zero or more occurrences
#search for a sequence that starts with 'he',followed by 0 or 1(any) character, and an 'o'
x=re.findall("he.?o",txt)
print(x)

# {} -exactly the specified number of occurrences
#search for a sequence that starts with 'he',followed exactly 2(any) characters, and an 'o'
x=re.findall("he.{2}o",txt)
print(x)


# | -either or

txt="The rain in Spain falls mainly in the plain!"
#check if the string contains either "falls" or "stays"
x=re.findall("falls|stays",txt)
print(x)
if x:
    print("Yes,ther is at least one match")
else:
    print("no match")


#regax exercises
#1
txt=input()
x=re.search("^ab*$", txt)
if x:
    print("Match found")
else:
    print("No match")

#2
txt=input()
x=re.findall("^ab{2,3}$", txt)
if x:
    print("match found")
else:
    print("No match")
    
#3
txt=input()
pattern=r'\b[a-z]+(?:_[a-z]+)+\b'
matches=re.findall(pattern, txt)
print(matches)


#4
txt=input()
pat=r'\b[A-Z][a-z]+\b'
print(re.findall(pat,txt))


#5
txt=input()
m=re.findall("^a.+b$", txt)
print(m)


#6
txt=input()
r=re.sub(r'[ ,.]',':', txt)
print(r)


#7
txt=input()
res=re.sub(r'_([a-z])', lambda m: m.group(1).upper(), txt)
print(res)


#8
txt=input()
res=re.split(r'(?=[A-Z])',txt)
print(res)


#9
txt=input()
res=re.sub(r'(?=[A-Z])',' ',txt)
print(res.strip())


#10
txt=input()
res=re.sub(r'([a-z0-9])([A-Z])', r'\1_\2',txt).lower()
print(res)