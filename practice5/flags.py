# re.ASCII(re.A)-returns only ASCII matches
import re
txt="Eland"
#find all ASCII matches
print(re.findall("\w", txt , re.ASCII))
#without the flag, the example would return all character
print(re.findall("\w",txt))
#same result using the shorthand re.A flag
print(re.findall("\w",txt,re.A))


# re.DEBUG -returns debug information
import re
txt="The rain in Spain"
#use a case-insensitive search when finding a match for Spain in the text
print(re.findall("spain", txt, re.DEBUG))


# re.DOTALL(re.S) -makes the . character match all characters
txt="""Hi
my
name
is
Sally"""
#search for a sequence that starts with 'me',followed by one character,even a newline character, and continues with 'is'
print(re.findall("me.is",txt,re.DOTALL))
#this example would return no match without the re.DOTALL flag
print(re.findall("me.is", txt))
#same result with the shorthand re.S flag
print(re.findall("me.is", txt, re.S))



# re.IGNORECASE(re.I) - case-insensitive matching
txt="The rain in Spain"
#use a case-insensitive search when finding a match for Spain in the text
print(re.findall("spain",txt,re.IGNORECASE))
#same result using the shorthand re.I flag
print(re.findall("spain", txt, re.I))


#re.MULTILINE(re.M) - returns only matches at the beginning of each line
txt="""There
aint much
rain in
Spain"""
#Search for the sequence "ain", at the beginning of a line
print(re.findall("^ain",txt,re.MULTILINE))
#this example would return no matches without the re.MULTILINE flag, because the ^character without re.MULTILINE only get a match at the very beginning of the text
print(re.findall("^ain", txt))
#same result with using the shaothand re.M flag
print(re.findall("^ain", txt, re.M))


# re.VERBOSE(re.X) - allows whitespaces and comments inside patterns. Makes the pattern more readable
txt="The rain in Spain falls mainly on the plain"
#find and return words that contains the phrase "ain"
pattern="""
[A-Za-z]*#starts with any letter
ain+ #contins 'ain'
[a-z]* #followed by any small letter
"""
print(re.findall(pattern,txt,re.VERBOSE))
#the example would return nothing without the re.VERBOSE flag
print(re.findall(pattern, txt))
#same result with using the shorthand re.X flag
print(re.findall(pattern , txt, re.X))


# re.UNICODE(re.U) - returns Unicode matches. this is default from Python3
txt="Eland"
#find all UNICODE matches
print(re.findall("\w", txt, re.UNICODE))
#same result using the shorthand re.U flag
print(re.findall("\w", txt, re.U))