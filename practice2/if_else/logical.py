#logical operators
'''
and-Returns True if both statements are true
or-Returns True if one of the statements is true
not-Reverses the result, returns False if the result is true
'''
#and
a=198
b=67
c=375
if a>b and c>a:
    print("Both conditions are true")

#or
a=198
b=67
c=375
if a>b or a>c:
    print("At least one of the conditions is True")

#not
a=56
b=198
if not a>b:
    print("a is not greater than b")


#and or not
age=25
is_student=False
has_discount_code=True
if(age<18 or age>65) and not is_student or has_discount_code:
    print("Discount applies!")

    

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")
