import os 

def pathcheck(path):
        if os.path.exists(path):
            print('Filename:', os.path.basename(path))
            print('Directory:', os.path.dirname(path))
        else:
            print('The path ', path,' doesn\'t exist')

path = '/Users/zhonik99/Documents/KBTU/pp2_labs'

pathcheck(path)

path = '/Users/zhonik99/Documents/KBTU/pp2_labzzzz'

pathcheck(path)