# 4)Below and above Average numbers

l1=[]
while 1:
  num=int(input("Enter the value end with zero:"))
  if num==0:
    break;
  else:
    l1.append(num)
print(l1);
sm=0; ba=''; av=''; abv=''
for i in l1:
  sm+=i
avg=sm/len(l1)
print("Avg:",avg)
for i in l1:
      if i<avg:
        ba=ba+' '+str(i)
      elif i==avg:
        av=av+' '+str(i)
      else:
        abv=abv+' '+str(i)
print("Below avg values:%s\nAvg values:%s\nAbove Avg values:%s"\
      %(ba,av,abv))
