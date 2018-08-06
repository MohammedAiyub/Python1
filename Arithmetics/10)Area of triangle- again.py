# 10)Area of triangle- again

s1=float(input("Enter the 1st side of Triangle:"))
s2=float(input("Enter the 2nd side of triangle:"))
s3=float(input("Enter the 3rd side of triangle:"))
s=(s1+s2+s3)/2
import math
print("Area of triangle is", math.sqrt(s*(s-s1)*(s-s2)*(s-s3)))
