#20)Different TimeZont times
from datetime import datetime,time
from pytz import timezone
time=input("Enter the Time(H:M AM/PM):")
print("US timezone only such as Eastern/Central/Pacific/Mountain ...")
stz='US/'+input("Enter Starting Time zone:")
etz='US/'+input("Enter Ending Time Zone:")
fmt="%I:%M %p"
ct=timezone(stz)
tzt=ct.localize(datetime.strptime(time,'%I:%M %p'))
#print(tzt.strftime(fmt))
te = tzt.astimezone(timezone(etz))
print("Desired time is ",te.strftime(fmt)) 

