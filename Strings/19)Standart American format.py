#19)Standart American format

srt=input("Entr the long digits:")
sm=""
ln=len(srt)%3; i=0
smt1=""; lst=[]
while i<ln:
    sm=sm+srt[i]
    i+=1
if sm:
  lst.append(sm)
i1=0; ln1=int(len(srt)/3)+1
for i1 in range(1,ln1):
  for q in range(1,4):
    smt1=smt1+srt[i]
    i=i+1
  lst.append(smt1)
  smt1=""
print(str(','.join(lst)))
