# 3)Avoiding Duplicates

l1=[]
while 1:
  num=input("Enter the words end with '':")
  if num=='':
    break;
  else:
    l1.append(num)
l2=set(l1)
print(l2)
