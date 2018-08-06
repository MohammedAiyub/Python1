# 1)concatinate multiple files

files=input("Enter the files(file1.txt,..) name with extension:")
if files!='':
    flst=files.split(',')
    fd=''
    
    for file in flst:
        
        try:
            with open(file,"r") as f:
                print(file,": ",f.read()+'\n')
        except FileNotFoundError:
            print("file name ",file," not exists\n")
            continue    
else:
    print("Enter the files to display")
