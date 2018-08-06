#16)Fromat function

srt=input("Enter your name:")
fn=srt.split(' ',1)
s1="Dear {},\n\t I am pleased to offer you our new platinum plus"\
    "\nRewards card at a special introductory APR of 47.99%. {} an offer"\
    "\nlike this does not come along every day,so I urge you to call"\
    "\nnow toll-free at 1-800-314-1592. We can not offer such a low "\
    "\nrate for long, {}, so call right now."
print(s1.format(srt,fn[0],fn[0]))
