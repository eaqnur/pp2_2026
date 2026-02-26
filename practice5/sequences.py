# \A -returns a match if the specified characters are at the beginning of the string
import re
txt="The rain in Spain"
#check if the string starts with "The"
x=re.findall("\AThe", txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("No match")


# \b -returns a match where the specified characters are at the begining or at the end of a word
#Check if "ain" is present at the beginning of a WORD
x=re.findall(r"\bain",txt)
print(x)
if x:
    print("Yes,there is at least one match")
else:
    print("no match")

# \d -returns a match where the string contains digits
#Check if the string contains any digits

x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match")
else:
  print("No match")


# \D -returns a match where the string DOES NOT contain digits
x=re.findall("\D", txt)
print(x)
if x:
   print("Yes, there is at least one match")
else:
   print("No match")



# \s -returns a match where the string contains a white space character
#return a match at every white-space character
x=re.findall("\s",txt)
print(x)
if x:
   print("Yes, there is at least one match")
else:
   print("No match")


# \S -returns a match where the string DOES NOT contain a white space character
x=re.findall("\S", txt)
print(x)
if x:
   print("Yes, there is at least one match")
else:
   print("No match")



# \w -returns a match where the string contains any word characters
#return a match at every word character
x=re.findall("\w",txt)
print(x)
if x:
   print("Yes, there is at least one match")
else:
   print("No match")


# \W -returns a match where the string DOES NOT contain any word characters
#return a match at every NON word character
x=re.findall("\W", txt)
print(x)
if x:
   print("Yes, there is at least one match")
else:
   print("no match")


# \Z -returns a match if the specified characters are at the end of the string
#check if the string ends with "Spain":
x=re.findall("Spain\Z", txt)
print(x)
if x:
   print("Yes, there is a match")
else:
   print("No match")


