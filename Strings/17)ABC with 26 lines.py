#17)ABC with 26 lines

srt="abcdefghijklmnopqrstuvwxyz"
sr="";  i=0;
for i in range(0,25):
  for j in range(0,25)
    sr= sr+srt[j]
  print(sr)
  srt=srt[1::1]+srt[0]
  sr=""
