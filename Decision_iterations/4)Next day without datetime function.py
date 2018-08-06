# 4)Next day without datetime function

srt=input("Enter the date(yyyy-mm-dd):")
#md={1:"Jan",2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
mly=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','sep','Oct','Nov','Dec']
mnt={'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
le={'Feb':29}
l1=srt.split('-')
dd=int(l1[2]); mm=int(l1[1]); yy=int(l1[0])
if mm <= 12 and dd <= mnt.get(mly[mm-1]):
  if yy%4==0: mnt.update(le)
  if dd < mnt.get(mly[mm-1]):
    dd+=1;
  elif dd== mnt.get(mly[mm-1]) and mly[mm-1]!="Dec":
    dd=1; mm+=1
  elif dd == mnt.get(mly[mm-1]) and mly[mm-1]=="Dec":
    dd=1; mm=1; yy+=1;
  print("Next day is ",str(yy)+'-'+str(mm)+'-'+str(dd))  
else: print("Enter the proper Date")
