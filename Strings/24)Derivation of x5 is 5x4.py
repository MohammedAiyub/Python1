# 24)Derivation of x5 is 5x4
srt=input("Enter pattern(x^n) to derive:")
l1=srt.split('^')
print(l1[1], l1[0], "^", int(l1[1])-1, sep='')
