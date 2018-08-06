# 22)Encrypt string with even and odd
def enc(srt):
    st=""
    for i in range(0,2):
        for j in range(i,len(srt),2):
          st=st+srt[j]
    return st
from math import ceil
def dec(srt):
    ds=""
    sp=ceil(len(srt)/2)
    sfh=srt[0:sp]
    ssh=srt[sp:]
    if len(sfh)> len(ssh):
        ssh=ssh+' '
    for i in range(0,len(sfh)):
        ds=ds+sfh[i]+ssh[i]
    return ds
    print(sfh,'\t',ssh)
srt=input("Entr the String:");
st=enc(srt)
print("Encrypted String is ", st)
st2=dec(st)
print("After decrption:",st2)
