import sys

minNumber = sys.maxsize
maxNumber = -sys.maxsize - 1

while True:
    num = input('Eter a number:')
    if num.lower() == 'done':
        break
    try:
        value = int(num)        
    except Exception as e:
        print('Invalid input')
        continue

    minNumber = min(minNumber, value)
    maxNumber = max(maxNumber, value)

if minNumber == sys.maxsize:
    print('No numbers')
else:
    print('Maximum is', maxNumber)
    print('Minimum is', minNumber)
