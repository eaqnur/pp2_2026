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


#exersises
#1 subtract 5 days from current date
from datetime import datetime , timedelta
today=datetime.today()
new_date=today-timedelta(days=5)
print("Today:",today.date())
print("5 days ago:", new_date.date())

#2Write a Python program to print yesterday, today, tomorrow.
from datetime import date, timedelta
today=date.today()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)

print("Yesterday: ", yesterday)
print("Today: ", today)
print("Tomorrow: ", tomorrow)


#3 Write a Python program to drop microseconds from datetime.
from datetime import datetime
now=datetime.now()
micro=now.replace(microsecond=0)
print("With microseconds:",now)
print("Without microseconds:",micro)

#4 Write a Python program to calculate two date difference in seconds.
from datetime import datetime
d1=input()
d2=input()
dt1=datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
dt2=datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")

diff=abs((dt2-dt1).total_seconds())
print("DIfference in seconds:",diff)


