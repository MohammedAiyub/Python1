# 10)Average on n mumbers

l1=[];
while True:
  srt=int(input("Enter the Number:"))
  if srt!=0: l1.append(srt)
  else:
    print("This is End of Input value:")
    break;
sm=0;
for i in l1:
  sm=sm+i
print("Average:",sm/len(l1))
