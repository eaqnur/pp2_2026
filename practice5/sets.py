# [arn]-returns a match where one of the specified characters (a, r, or n) is present
import re
txt="The rain in Spain"
#check if the string has any a,r,n characters
x=re.findall("[arn]", txt)
print(x)
if x:
    print("Yes")
else:
    print("No")



# [a-n]-returns a match for any lower case character, alphabetically between a and n
#check if the string has any characters between a nd n
x=re.findall("[a-n]", txt)
print(x)


# [^arn]-returns a match for any character EXCEPT a, r, and n
x=re.findall('[^arn]', txt)
print(x)

#The findall() function returns a list containing all matches.
import re
txt="The rain in Spain"
x=re.findall("ai", txt)
print(x)

x=re.findall("Portugal", txt)
print(x)


#The search() function searches the string for a match, and returns a Match object if there is a match.
txt="The rain in Spain"
x=re.search('\s', txt)
print(x.start())

x=re.search("Portugal", txt)
print(x)


#The split() function returns a list where the string has been split at each match
txt="The rain in Spain"
x=re.split("\s", txt)
print(x)


#The sub() function replaces the matches with the text of your choice
txt="The rain in Spain"
x=re.sub("\s", 'g', txt)
print(x)

x=re.sub("\s", "g", txt, 2)
print(x)


#.span() returns a tuple containing the start-, and end positions of the match.
txt="The rain in Spain"
x=re.search(r"\bS\w+", txt)
print(x.span())


#.string returns the string passed into the function
txt="The rain in Spain"
x=re.search(r"\bS\w+", txt)
print(x.string)

#.group() returns the part of the string where there was a match
txt="The rain in Spain"
x=re.search(r"\bS\w+", txt)
print(x.group())