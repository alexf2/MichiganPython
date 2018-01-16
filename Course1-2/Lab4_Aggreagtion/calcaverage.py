fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:    
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.strip()
    idx = line.rindex('0.')
    if idx == -1 : continue
    total = total + float(line[idx:len(line)]); count = count + 1

if count == 0:    	
	print(0.0)
else:
    print('Average spam confidence:', total / count)

