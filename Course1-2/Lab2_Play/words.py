from os import path
import re

pathRoot =  path.abspath('.\data')
fileNames = ['mbox-short', 'romeo', 'words'] #Gets the files and counts unique words
for fileName in fileNames:
    
    fh = None
    try:
        fullPath = path.join(pathRoot, fileName + '.txt')
        fh = open(fullPath, 'r')
        dic = {}
        lineCount = 0
        for line in fh:
            for word in line.split(' '):
                word = word.strip()
                count = dic.get(word, 0)
                dic[word] = count + 1
            lineCount = lineCount + 1
        fh.close()

        print(f'File: "{path.basename(fullPath)}"  has  {lineCount} lines  and  {len(dic)}  unique words.')

        for item in sorted(list(dic.items()), key=lambda it: it[1], reverse = True):
            if item[1] >= 5:
                print(f'\t{item[0]} --> {item[1]}')
    except Exception as e:
        print(e)
        if fh is not None: fh.close()

    print()
    

vv = [2*k for k in range(1,50)]
print(vv.pop())
print((1, 2).index(2))

print((6,0,0) > (5,1,3))
print((4,100,200) > (5,1,3))
print((5,0,300) > (5,1,3))
print((0,1000,2000) > (5,1,3))

rr = re.compile('\d+:\d+:\d+')
print(rr.match('11:22:77').group())
