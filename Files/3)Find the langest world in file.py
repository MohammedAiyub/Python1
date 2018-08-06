# 3)Find the langest world in file
file=input("Enter the file name:")
if file=="":
    print("Enter the file")
else:
    try:
        with open(file, 'w+') as f:
           cnt=input("Enter content:")
           f.write(cnt)

        with open(file, 'r+') as f1:
            lines = (f1.read()).split(' ')
            max_len=len(max(lines,key=len))
            for line in lines:
                if len(line) == max_len: lw=line
                print("length of ",line,'is',len(line))
            print("largest word is",lw,",length is", max_len)    
    except IOError:
        print("Unable to write in this file")
    except FileNotFoundError:
        print("This file not Exist")
