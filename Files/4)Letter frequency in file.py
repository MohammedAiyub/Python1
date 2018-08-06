#4)Letter frequency in file
import os
file_name=input("Enter the file name:")
if file_name:
    if os.path.isfile(file_name):
        tfd=dict()
        with open(file_name,'rt') as file:
            fd=file.read()
            for ltr in fd:
                if ltr.isalpha():
                    keys=tfd.keys()
                    if ltr.lower() in keys:
                        tfd[ltr.lower()]+=1
                    else: tfd[ltr.lower()]=1
            print(tfd)
                    
    else: print("Unable to find file in this name")    
else:
    print("File name should not empty")
