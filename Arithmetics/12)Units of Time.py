# 12)Units of Time

d=int(input("Enter the day:")); h=int(input("Enter the Hour:"))
m=int(input("Enter the Minutes:"));s=int(input("Enter the Seconds:"))
print("Number of seconds b/w these durations:" ,s+m*60+h*3600+d*86400)
sec=int(input("Enter the seconds:"))
d1=sec/86400; temp=sec%86400;
h1=temp/3600; temp= temp%3600;
m1=temp/60; temp= temp%60
s1=temp;
print("This seconds contains(DD:HH:MM:SS) %0.2d:%0.2d:%0.2d:%0.2d" \
      %(d1,h1,m1,s1))
