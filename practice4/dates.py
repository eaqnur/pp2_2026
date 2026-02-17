#import the datetime module 
import datetime
x=datetime.datetime.now()
print(x)

#date output
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#creating date object
import datetime
x=datetime.datetime(2020,5,7)
print(x)

#the strftime() method
import datetime
x=datetime.datetime(2018,6,1)
print(x.strftime("%B"))
