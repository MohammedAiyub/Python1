# 8)E-mail id find

noe=int(input("How many E-mail you want to enter:"))
srt=input("Enter "+ str(noe) +" E-mails seperated with comma:")
pe=srt.count('@prof'); se=srt.count('@student')
print("These E-mail contains",pe," proffessors and ",se," student addresses")
