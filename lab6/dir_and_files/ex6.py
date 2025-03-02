import string
import os

path = r'/Users/zhonik99/Documents/KBTU/pp2_labs/lab6/dir_and_files/ex6_a-z'
os.makedirs(path)

def create_text_files():
    for letter in string.ascii_uppercase: 
        filename = f"{letter}.txt"
        open(f"{path}/{filename}", 'w')
        print(f"Created: {filename}")

create_text_files()