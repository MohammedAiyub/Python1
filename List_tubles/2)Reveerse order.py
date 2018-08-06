# 2)Reveerse order

l1=[]
while 1:
  num=int(input("Enter the value end with zero:"))
  if num==0:
    break;
  else:
    l1.append(num)
print(l1)
l1.reverse()
for i in l1:
  print(i,end='\n')
