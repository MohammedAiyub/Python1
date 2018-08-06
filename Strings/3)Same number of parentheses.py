# 3)Same number of parentheses

srt=input("Enter the formula:")
op=srt.count('('); cp=srt.count(')')
if op==cp:
    print("you entered correcct format")
elif op>cp:
    print(op-cp," ')' parentheses missing")
elif op<cp:
    print(cp-op, " ')' parentheses missing")
