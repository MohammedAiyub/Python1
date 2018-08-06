# 11)Area of regular polygon

s,n = float(input("Enter the length of polygon:")), float(input("enter the number of " \
                                                               "sides of polygon:"))
import math
print("Area of regular polygon is", (n* math.pow(s,2))/(4*math.tan(math.pi/n))) 
