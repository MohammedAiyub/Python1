#13)String capital and small

srt=input("Enter the string:")
srt1=input("Entr the second string with same lenth of 1st:")
if len(srt)!= len(srt1): print("string lenth are not same,\
                            Enter same lenth of string")
else:
    i=0; s="";
    while i<len(srt):
        s=s+srt[i]+srt1[i]
        i+=1
print(s)
