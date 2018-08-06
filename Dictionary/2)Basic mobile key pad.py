# 2)Basic mobile key pad
pad={1:('.',',','?','!',':'),
     2:('A','B','C'),
     3:('D','E','F'),
     4:('G','H','I'),
     5:('J','K','L'),
     6:('M','N','O'),
     7:('P','Q','R','S'),
     8:('T','U','V'),
     9:('W','X','Y','Z'),
     0:(' ')}
srt=input("Enter the string:")
srt=srt.upper()
i=0; j=0;
for k in range(len(srt)):
  for i in range(len(pad)):
    for j in range(len(pad[i])):
      if srt[k]==pad[i][j]:
        print(srt[k],'is ' ,j+1,' press in key',i)
