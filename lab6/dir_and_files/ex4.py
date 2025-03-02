import os

path = '/Users/zhonik99/Documents/KBTU/pp2_labs/lab6/dir_and_files/ex4.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))