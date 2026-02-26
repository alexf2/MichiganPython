
### Use this space to try out ideas and free code ###

cortage = (1,2,5)
array=[5,10,15]

def test(*args):
  for a in args:
    if hasattr(a, '__iter__'):
      for b in a:
        print(b)
    else:
      print(a)
      

def test2(*args):
  for a in args:
    if hasattr(a, '__iter__'):
      cc = map(lambda x: print(x), a)
    else:
      print(a)

def test3(*args):
  for a in args:
    if hasattr(a, '__iter__'):
      test(*a)
    else:
      print(a)
    
test2(1,2,3,4,5)
print('---------------')
test2(cortage)
print('---------------')
test2(array)
