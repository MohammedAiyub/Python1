# 7)Multiple word palindrome

srt=input("Enter the string:")
it=0; srt1=""
while it< len(srt):
  if srt[it].isalnum():
    srt1+=srt[it]
  it+=1
i=0; j=len(srt1)-1; cnt=0;
while i<len(srt1) and j>=0:
  if srt1[i]==srt1[j]:
    cnt+=1
  i+=1; j-=1
print("{} palintrome".format('Yes' if cnt==len(srt1) else 'Not')) 
