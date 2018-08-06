# 9)Retail Discount table

l1=[4.95,9.95,14.95,19.95,24.95]
l2=[]
for i in l1:
  l2.append(i*0.60)
print("Old price\tDiscount Amount\tNew price")
for (a,b) in zip(l1,l2):
  print("$%.2f\t\t$%.2f\t\t$%.2f" %(a,b,a-b))
