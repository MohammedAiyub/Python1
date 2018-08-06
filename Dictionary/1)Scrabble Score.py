# 1)Scrabble Score

scr={'one':('AEILNORSTU'),'two':('DG'),'three':('BCMP'),'four':('FHVWY'),'five':('K'),'eight':('JX'),'ten':('QZ')}
srt=input("Enter the word:")
srt=srt.upper()
score=0
for i in srt:
  if i in scr['one']: score+=1
  elif i in scr['two']: score+=2
  elif i in scr['three']: score+=3
  elif i in scr['five']: score+=5
  elif i in scr['eight']: score+=8
  elif i in scr['ten']: score+=10
  else: print("Enter only alphabet")
print("Score:",score)
