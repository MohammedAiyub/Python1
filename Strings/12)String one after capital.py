# 12)String one after capital

srt=input("Enter the word:"); i=1; s1="";
while i<len(srt)+1:
    if i%2==0: s1=s1+srt[i-1].upper()
    else: s1=s1+srt[i-1]
    i+=1;
print(s1)
