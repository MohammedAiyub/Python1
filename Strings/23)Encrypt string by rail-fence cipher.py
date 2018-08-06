# 23)Encrypt string by rail-fence cipher
from math import floor
def enc(srt,k):
    st=""
    for i in range(0,k):
        for j in range(i,len(srt),k):
          st=st+srt[j]
    return st
def dec(srt,k):
    ds='';dic=dict()
    sq=floor(len(srt)/k); rm=len(srt)%k
    for i in range(k):
        dic["r"+str(i)]=sq
    if rm > 0:
        for i in range(rm):
            dic["r"+str(i)]+=1
    ld=list();j=0
    for i in range(len(dic)):
        ld.append(list(srt[j:j+int(dic["r"+str(i)])]))
        j+=int(dic["r"+str(i)])
    
    for i in range(len(ld)):
        if len(ld[0])>len(ld[i]):
            ld[i].append(" ")

    for j in range(len(ld[0])):
        for i in range(len(ld)):
            ds=ds+ld[i][j]
    return ds;
srt=input("Enter the longest string:")
key=int(input("Enter the key to encrypt:"))
es=enc(srt,key)
print("Encrypted String:",es)
ds=dec(es,key)
print("After Decryption:",ds)
