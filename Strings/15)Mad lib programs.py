# 15)Mad lib programs

story="I changed my password everywhere to incorrect.That way when I forget it, it always reminds me,'Your password is incorrect.' 

s1=input("Enter security word:")
s2=input("Eenter opposite of sometimes:")
s3=input("Enter opposite of correct:")
stry="I changed my {0} everywhere to '{1}'. That way when I forget it, it {2}\
 reminds me, 'Your password is incorrect.'"
print(stry.format(s1,s3,s2))
