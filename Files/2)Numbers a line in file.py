# 2)Numbers the line in a file
file=input("Enter the file name:")
if file=="":
    print("Enter the file")
else:
    try:
        with open(file, 'w+') as f:
            while True:
                cnt=input("Enter content end with None:")
                if cnt!='':
                    f.writelines(cnt+'\n')
                else: break
                
        with open(file, 'r+') as f1:
            lines =f1.readlines()
            i=1
            for line in lines:
                print(i,": ",line)
                i+=1
    except IOError:
        print("Unable to write in this file")
    except FileNotFoundError:
        print("This file not Exist")
