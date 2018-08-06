# 3)Name that Triangle

s1=input("Enter the First side of Triangle:")
s2=input("Enter the Second side of Triangle:")
s3=input("Enter the Third side of Triangle:")
if s1==s2 and s1!=s3 and s2!=s3: print("This is ISOSCELES Triangle")
elif s1==s3 and s1!=s2 and s2!=s3: print("This is ISOSCELES Triangle")
elif s2==s3 and s1!=s2 and s1!=s3: print("This is ISOSCELES Triangle")
elif s1==s2==s3: print("This is EQUILATERAL Triangle")
else: print("This is SCALENE Triangle")
