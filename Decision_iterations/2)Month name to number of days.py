# 2)Month name to number of days
nmt=input("Enter the month(jan/may) in word:")
yr=int(input("Enter the year(yyyy):"))
if yr%4==0:
  mnt={'jan':31,'feb':29,'mar':31,'apr':30,'may':31,'jun':30,'jul':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
else:
  mnt={'jan':31,'feb':28,'mar':31,'apr':30,'may':31,'jun':30,'jul':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
print("This month contains %d days" %(mnt.get(nmt)))
