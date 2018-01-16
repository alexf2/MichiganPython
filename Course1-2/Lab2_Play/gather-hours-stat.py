
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dicCount = {}
maxEml = None; maxCount = -1
for line in handle:
    line = line.strip()
    if len(line) < 1 or not line.lower().startswith('from '): continue
        
    line = line.split()
    
    if len(line) > 1:
        time = line[len(line) - 2].split(':')        
        if len(time) == 3:
            dicCount[time[0]] = dicCount.get(time[0], 0) + 1
       
        
#resultList = [(v, k) for (k, v) in dicCount.items()]
resultList = dicCount.items()
resultList.sort()
for h, cnt in resultList:
	print(h, cnt)
