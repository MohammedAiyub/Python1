#25) Algebraic Expressios
srt=input("Enter the algebraic formula:")
sto=""; i=0; j=1
#for i in range(0,len(srt)), j in range(1,len(srt)):
while i<len(srt)-1 and j<=len(srt)-1:
  if srt[i].isalpha() and srt[j].isalpha():
    sto=sto+srt[i]+'*';
  elif srt[i].isnumeric() and srt[j].isnumeric():
    sto=sto+srt[i]
  elif srt[i].isalpha() and srt[j].isnumeric():
    sto=sto+srt[i]+'*'
  elif srt[i].isnumeric() and srt[j].isalpha():
    sto=sto+srt[i]+'*'
  elif srt[i] in [')',']','}'] and srt[j].isalpha():
    sto=sto+srt[i]+'*'
  elif srt[i].isalpha() and srt[j] in ['(','[','{']:
    sto=sto+srt[i]+'*'
  elif srt[i].isnumeric() and srt[j] in ['(','[','{']:
    sto=sto+srt[i]+'*'
  elif srt[i] in [')',']','}'] and srt[j].isnumeric():
    sto=sto+srt[i]+'*'
  elif srt[i] in [')',']','}'] and srt[j] in ['(','[','{']:
    sto=sto+srt[i]+'*'
  else:
    sto= sto+srt[i]
  i+=1; j+=1
sto=sto+srt[len(srt)-1]
print(sto)
