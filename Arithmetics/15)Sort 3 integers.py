# 15)Sort 3 integers

n1,n2,n3= float(input("Enter the First number:")),\
          float(input("Enter the second number:")),\
          float(input("Enter the third number:"))

print("Sorting order:",min(n1,n2,n3),(n1+n2+n3)-min(n1,n2,n3)-\
      max(n1,n2,n3),max(n1,n2,n3))
