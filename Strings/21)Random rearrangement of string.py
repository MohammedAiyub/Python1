# 21)Random rearrangement of string

srt=input("Enter the string:")
import random
l1=list(srt)
random.shuffle(l1)
for i in l1:
  print(i,end='')
