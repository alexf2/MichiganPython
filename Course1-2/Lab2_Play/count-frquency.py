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
        fromEml = line[1]
        count = dicCount.get(fromEml, 0) + 1
        dicCount[fromEml] = count
        
        if maxCount < count:
            maxCount = count
            maxEml = fromEml
       
        
print(maxEml, maxCount)
