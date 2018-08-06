# 6)String palindrome:
srt=input("Enter the string:")
i=0; j=len(srt)-1; cnt=0
while i<=len(srt) and j>=0:
  if srt[i]==srt[j]:
    cnt+=1;
  i+=1; j-=1;
print("{} palintrome".format('Yes' if cnt==len(srt) else 'Not')) 

