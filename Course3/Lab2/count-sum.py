import re
from os import path

pathRoot = path.abspath('.\data')

def _withExtension(name, ext = '.txt'):
    return name if name is None or name.lower().endswith(ext) else name + ext

def countSum (fileName):
    if len(fileName) < 1: raise Exception('File name should not be empty')
    
    sum = 0

    handle = None
    regEx = re.compile(r'-?\d+')
    try:
        handle = open(path.join(pathRoot, _withExtension(fileName)))
        for line in handle:
            #print(line[0:10])
            
            line = line.strip()
            if len(line) < 1: continue

            #re.findall(line)
            for num in regEx.findall(line):
                sum = sum + int(num)

    finally:
        if handle is not None: handle.close()
    
    return sum


print( countSum('f1') )
print( countSum('f2') )