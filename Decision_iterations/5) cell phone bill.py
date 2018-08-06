# 5) cell phone bill

minutes=input("Enter the number of minutes spoke:")
txtmsg=input("Enter the numnber of text messages sent:")
crg= 15.00
print("Monthly Charges:$%.2f" %crg)
if int(minutes) > 50:
  atcrg = (int(minutes)-50)*0.25
  print("Aditional Air time charges:$%.2f" %atcrg)
else: atcrg=0
if int(txtmsg) > 50:
  tmcrg= (int(txtmsg)-50)*0.15
  print("Aditional Text Message Charges:$%.2f" %tmcrg)
else: tmcrg=0
adcrg=0.44
print("call center support charges:$%.2f" %adcrg)
totamt= crg+atcrg+tmcrg+adcrg;
print("Total amount:$%.2f" %totamt)
tx=0.05*totamt;
print("Tax Amount of 5 percent:$%.2f" %tx)
netamt=totamt+tx
print("Grand Total:$%.2f" %netamt)
