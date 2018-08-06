#18)count,index with out function

srt=input("Entr the String:"); cnt=0; i='';
ltr=input("Enter any Alphabet letter:")
for i in srt:
  if i==ltr: cnt+=1;
print("{} the word appears {} times".\
      format('yes' if cnt>0 else 'No',cnt))          
s1='';tc=0
for i in srt:
    if i==ltr:
      s1=s1+i
      tc+=1
      break;
    else:
      s1=s1+i
      tc+=1
print("Splited string is:", s1,',',srt[tc:])
