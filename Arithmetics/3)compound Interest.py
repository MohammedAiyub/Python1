# 3)compound Interest - cp= p[(1+r)pow(n)-1]
amt=int(input("Enter the Amount:"))
ri=4/100*amt
print("Compound interest of 1st year is %.2f and total amount is %.2f" \
       %( (amt*(pow(1+ri,1)-1)) , (amt*(pow(1+ri,1)-1))+amt))
print("Compound interest of 2st year is %.2f and total amount is %.2f" \
       %( (amt*(pow(1+ri,2)-1)) , (amt*(pow(1+ri,2)-1))+amt))
print("Compound interest of 3rd year is %.2f and total amount is %.2f" \
       %( (amt*(pow(1+ri,3)-1)) , (amt*(pow(1+ri,3)-1))+amt))
       
