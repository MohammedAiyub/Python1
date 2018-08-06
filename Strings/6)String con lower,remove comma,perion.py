# 6)string con lower,remove comma,perion

srt=input("Enter the string:"); s1=''
s2="";
for i in srt:
    if i!=' ' and i!=',': s2=s2+i
print("After removed , and ' ' :",s2)
print("Converted to lower:", s2.lower())
