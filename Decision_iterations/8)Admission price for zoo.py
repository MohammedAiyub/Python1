# 8)Admission price for zoo

l1=[];
while True:
  srt=input("Enter the parson and age:")
  if srt: l1.append(srt)
  else: break;
#print(l1)
l2=[]
for i in l1:
  l2=i.split(' ')
  if int(l2[1])<=2:
    print("person:",l2[0]," and age:",l2[1]," no cost")
  elif int(l2[1])>=3 and int(l2[1])<=12:
    print("person:",l2[0]," and age:",l2[1]," cost:$14.00")
  elif int(l2[1])>=13 and int(l2[1])<=64:
    print("person:",l2[0]," and age:",l2[1]," cost:$23.00")
  else: print("person:",l2[0]," and age:",l2[1]," cost:$18.00")
