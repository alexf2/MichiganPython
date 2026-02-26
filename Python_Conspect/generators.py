def fibo(n):
  if n < 1:
    yield; return
    
  if n == 1:
    yield 0; return
    
  yield 0; yield 1
  if n == 2:
    return
    
  prev, curr = (0, 1); n -= 2
  while n > 0:
    prev, curr = (curr, prev + curr)
    yield curr
    n -= 1
    
    
for i in fibo(19):
  print(i)
    