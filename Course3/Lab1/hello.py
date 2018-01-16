import re

def sayHello(extraWord):
    print(f'Hello, {extraWord}!')

sayHello('Peter')

x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)