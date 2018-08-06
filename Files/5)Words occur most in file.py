# 5)Words occur most in file
import os
file_name=input("Enter the file name:")
if file_name:
    if os.path.isfile(file_name):
        wl=list();uwl=list();wd=dict()
        with open(file_name,'rt') as file:
            fd=file.read()
            wl=fd.split(' ')
            for word in wl:
                uwl.append((((word.strip('!')).strip('.')) .strip('\n')).lower())

            for word in uwl:
                keys=wd.keys()
                if word in keys:
                    wd[word]+=1
                else: wd[word]=1
            print(wd)
            wc = max(wd.values())
            print(wc)
            mow=''
            for i,j in wd.items():
               if j==wc:
                  mow=i
                  break
        print("Word ",mow,"only occured ",wc," times")       
    else: print("unable to find file in this name")
else: print("File name should not empty")
