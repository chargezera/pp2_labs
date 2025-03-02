import os 

path = r'/Users/zhonik99/Documents/KBTU/pp2_labs/lab6/dir_and_files/ex8.txt'
name = os.path.basename(path)

if os.path.exists(path):
    print(f'File "{name}" exists')
    if os.access(path, os.W_OK):
        print(f'File "{name}" can be deleted')
        os.remove(path)
        print(f'"{name}" is deleted')
    else:
        print(f'File "{name}" can\'t be deleted')
else:
    print(f'File "{name}" does\'t exist')